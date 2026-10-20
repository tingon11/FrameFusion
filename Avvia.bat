@echo off
rem Avvia FrameFusion senza finestra console.
cd /d "%~dp0"
if exist ".venv\Scripts\pythonw.exe" (
    start "" ".venv\Scripts\pythonw.exe" "FrameFusion.py"
) else (
    start "" pythonw "FrameFusion.py"
)
