import torch
import numpy as np
from model import HeartModel
from utils import load_scaler

# Load scaler
scaler = load_scaler()

# Load model
input_size = 13  # change if different
model = HeartModel(input_size)

model.load_state_dict(torch.load("saved_models/heart_model_final.pth"))
model.eval()

def predict(data):
    data = np.array(data).reshape(1, -1)
    
    # Scale
    data = scaler.transform(data)
    
    data_tensor = torch.tensor(data, dtype=torch.float32)
    
    with torch.no_grad():
        output = model(data_tensor)
        prediction = (output > 0.5).float().item()
    
    return int(prediction)