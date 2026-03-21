import joblib

def load_scaler():
    return joblib.load("data/scaler.pkl")