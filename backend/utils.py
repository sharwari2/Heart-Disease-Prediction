import joblib
import os

def load_scaler():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return joblib.load(os.path.join(BASE_DIR, "data", "scaler.pkl"))