@echo off

:: Checks the windows registry for Unreal Engine 4.27 installation directory and saves the path in a temp file
Powershell.exe -Command "& { (Get-ItemProperty 'Registry::HKEY_LOCAL_MACHINE\SOFTWARE\EpicGames\Unreal Engine\4.27' -Name 'InstalledDirectory' ).'InstalledDirectory' }" > gen_temp.txt

:: If temp file not empty, store contents
for /f %%i in ("gen_temp.txt") do set size=%%~zi
if %size% gtr 0 set /p UE4Path=<gen_temp.txt

:: Path to the executable (usually the same, but will try to remove hardcoded string)
set ExecutablePath=\Engine\Binaries\Win64\UE4Editor.exe

:: concatenate paths
set UnrealPath=%UE4Path%%ExecutablePath%

:: Current Directory
set CurrentDir=%cd%

:: Uproject file
for %%f in (*.uproject) do (
     set Uproject=%%f
)
if exist "%Uproject%" set EnvPath=%CurrentDir%\%Uproject%

:: settings.json
for %%f in (*.json) do (
     set Settingsjson=%%f
)
if exist "%Settingsjson%" set SettingsPath=%CurrentDir%\%Settingsjson%

:: Perform final checks
if exist "%UnrealPath%" (echo [INFO]:Unreal Engine Executable path : %UnrealPath%) else (echo [ERROR] Unreal Engine path could not be found! Please edit the .bat file manually with the correct path)
if exist "%EnvPath%" (echo [INFO]:Environment uproject_file path: %EnvPath%) else (echo [ERROR] YourEnvironmentName.uproject could not be found!! Please make sure file exists!)
if exist "%SettingsPath%" (echo [INFO]:Path to settings.json         : %SettingsPath%) else (echo [ERROR] settings.json could not be found!! Please make sure file exists!)

:: Prints final command to be executed
echo(
echo [EXEC]: %UnrealPath% %EnvPath% -settings=%SettingsPath%
echo(

:: Run
start "" "%UnrealPath%" "%EnvPath%" -settings="%SettingsPath%"

:: remove the temp file
del gen_temp.txt

pause