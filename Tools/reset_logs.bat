@echo off
echo === Resetting Sentinel Vector logs ===
if exist logs (
    del /q logs\*.log
) else (
    mkdir logs
)
echo Logs reset complete. Ready for a fresh run.
pause
