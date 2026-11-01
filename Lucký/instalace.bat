@echo off
cd /d "%~dp0"
set LOG="%~dp0instalace.log"
echo start > %LOG%
set PY=
where py >nul 2>&1 && set PY=py -3
if not defined PY (python --version >nul 2>&1 && set PY=python)
if not defined PY (echo PYTHON NENI NAINSTALOVANY >> %LOG% & goto konec)
if not exist .venv\Scripts\python.exe %PY% -m venv .venv >> %LOG% 2>&1
.venv\Scripts\python.exe -m pip install -r requirements.txt >> %LOG% 2>&1
.venv\Scripts\python.exe -c "import pygame; print(OK, pygame.version.ver)" >> %LOG% 2>&1
:konec
echo konec >> %LOG%
where code >nul 2>&1 && call code . main.py
