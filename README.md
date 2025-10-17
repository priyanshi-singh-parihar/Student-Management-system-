Student Management System (minimal Flask demo)

Quickstart

1. Create and activate the virtualenv or use the provided `.venv`.
2. Install dependencies:

   "C:/Users/Priyanshi/Desktop/Student Management System/.venv/Scripts/python.exe" -m pip install -r requirements.txt

3. Run the app:

   "C:/Users/Priyanshi/Desktop/Student Management System/.venv/Scripts/python.exe" app.py

Notes

- `ai_model/predictor.py` will attempt to load `ai_model/at_risk_model.pkl`. If missing, a dummy prediction is returned.
- This is a frontend-focused scaffold; connect a real database and authentication for production use.
