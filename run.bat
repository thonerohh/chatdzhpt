@REM move files from output to the ../responses folder and create folder if it doesn't exist
@echo off
setlocal
set "source=./output"
set "target=../responses"
if not exist "%target%" md "%target%"
for /f "delims=" %%F in ('dir /b /a-d "%source%\*"') do move /y "%source%\%%F" "%target%"
endlocal