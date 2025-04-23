@echo off
setlocal enabledelayedexpansion

for %%f in (*.py) do (
    python "%%f" > "%%~nf_result.txt"
    
    if !ERRORLEVEL! EQU 0 (
        echo Successfully finished processing %%f
    ) else (
        python "%%f" > "%%~nf_result.txt" 2> "%%~nf_error.log"
        echo Failed to process %%f. See %%~nf_error.log for details.
    )
)

endlocal
pause
