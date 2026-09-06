@echo off
REM Wayfinder bridge launcher.
REM Double-click this file to start the bridge manually any time.
REM Keeps a visible window open so you can see its status and any errors.

cd /d "%~dp0"

echo Starting Wayfinder bridge...
echo (Close this window to stop it.)
echo.

python wayfinder_bridge.py

REM If python.exe isn't on PATH, the line above fails silently and closes
REM immediately. The pause below keeps the window open so you can read
REM the error instead of losing it.
pause
