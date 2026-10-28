# IdentiFrame — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
# SPDX-License-Identifier: GPL-3.0-only
# GNU GPL v3 con termini aggiuntivi (attribuzione dell'autore): vedi LICENSE e NOTICE.
"""Riproduzione dell'anteprima: un solo ffmpeg che decodifica in avanti, poco oltre il cursore.

Chiedere i fotogrammi a lotti (un processo e un seek per lotto) fa andare la
riproduzione a scatti: ogni lotto riparte dal keyframe. Qui un thread tiene
aperto un unico flusso dal fotogramma di partenza e riempie una piccola
riserva; l'interfaccia, al ritmo del video, prende il fotogramma piu' recente
non oltre l'orologio. Se la decodifica resta indietro l'orologio aspetta,
invece di saltare.
"""

from __future__ import annotations

import threading

from PIL import Image

from . import ffmpeg
from .ffmpeg import VideoInfo

AHEAD = 24   # fotogrammi decodificati in anticipo al massimo


class Player:
    def __init__(self, info: VideoInfo, first: int, width: int) -> None:
        self.width = width
        self.error: BaseException | None = None
        self._size = (width, max(2, int(round(info.height * width / info.width))))
        self._ready: dict[int, Image.Image] = {}
        self._cond = threading.Condition()
        self._stop = False
        self._finished = False
        threading.Thread(target=self._run, args=(info, first), name="if-player", daemon=True).start()

    def _run(self, info: VideoInfo, first: int) -> None:
        frames = ffmpeg.stream_frames(info, first, info.frames - first, "rgb24", size=self._size)
        try:
            for index, array in frames:
                image = Image.fromarray(array)
                with self._cond:
                    while not self._stop and len(self._ready) >= AHEAD:
                        self._cond.wait(0.05)
                    if self._stop:
                        break
                    self._ready[index] = image
        except Exception as exc:  # noqa: BLE001 - lo riporta l'interfaccia
            self.error = exc
        finally:
            frames.close()   # ferma ffmpeg se si e' smesso prima della fine
            with self._cond:
                self._finished = True

    def take(self, target: int) -> tuple[int, Image.Image] | None:
        """Il fotogramma piu' recente non oltre `target`, scartando i precedenti; None se non c'e' ancora."""
        with self._cond:
            ready = [index for index in self._ready if index <= target]
            if not ready:
                return None
            best = max(ready)
            image = self._ready[best]
            for index in ready:
                del self._ready[index]
            self._cond.notify_all()
            return best, image

    @property
    def exhausted(self) -> bool:
        """Il flusso e' finito (fine del video o errore) e non resta nulla da mostrare."""
        with self._cond:
            return self._finished and not self._ready

    def stop(self) -> None:
        with self._cond:
            self._stop = True
            self._cond.notify_all()
