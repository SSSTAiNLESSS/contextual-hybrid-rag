@echo off
REM Activate the virtual environment
call .venv\Scripts\activate

REM Set PYTHONPATH to current directory
set PYTHONPATH=%cd%

REM Run Uvicorn with your FastAPI app
python -m uvicorn src.api.app:app --reload

pause
