@echo off
:loop
cls
python C:\script\script.py
echo.
echo Нажмите любую клавишу для запуска сканирования снова...
pause >nul
goto loop
