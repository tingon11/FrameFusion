@echo off
rem Avvia IdentiFrame senza finestra console.
cd /d "%~dp0"
if exist ".venv\Scripts\pythonw.exe" (
    start "" ".venv\Scripts\pythonw.exe" "IdentiFrame.py"
) else (
    start "" pythonw "IdentiFrame.py"
)
