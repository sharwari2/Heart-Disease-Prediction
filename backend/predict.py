import torch
import numpy as np
import os
from model import HeartModel
from utils import load_scaler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load scaler
scaler = load_scaler()

# Load model
input_size = 13
model = HeartModel(input_size)

model.load_state_dict(torch.load(
    os.path.join(BASE_DIR, "saved_models", "heart_model_final.pth"),
    map_location="cpu"
))
model.eval()

def predict(data):
    data = np.array(data).reshape(1, -1)
    data = scaler.transform(data)
    data_tensor = torch.tensor(data, dtype=torch.float32)
    
    with torch.no_grad():
        output = model(data_tensor)
        prediction = (output > 0.5).float().item()
    
    return int(prediction)