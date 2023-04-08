@echo off
mkdir selenium_enhancer\drivers
set LATEST_VERSION=
for /f "delims=" %%i in ('curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE') do set LATEST_VERSION=%%i
curl -o C:\Temp\chromedriver.zip https://chromedriver.storage.googleapis.com/%LATEST_VERSION%/chromedriver_win32.zip
runas /user:Administrator "powershell Expand-Archive -Path C:\Temp\chromedriver.zip -DestinationPath C:\selenium_enhancer\drivers\"