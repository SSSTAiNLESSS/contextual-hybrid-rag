@echo off
REM Activate the virtual environment
call .venv\Scripts\activate

REM Run Uvicorn with your FastAPI app
python -m uvicorn api.app:app --reload

pause
