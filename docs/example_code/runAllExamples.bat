@echo off
for %%f in (*.py) do (
  python "%%f" > "%%~nf_result.txt"
)
pause
