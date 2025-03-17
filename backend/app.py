from fastapi import FastAPI, WebSocket
import torch
import numpy as np
from model import classifier, record_audio, get_model
import os
import uvicorn

app = FastAPI()

# ✅ Add a root route to test if the backend is running
@app.get("/")
def read_root():
    return {"message": "Backend is running!"}

@app.websocket("/detect_gender")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    for mfccs in record_audio():
        features = torch.tensor(mfccs).unsqueeze(0)
        prediction = classifier(features).detach().numpy()
        gender = "Male" if prediction[0][0] > prediction[0][1] else "Female"
        await websocket.send_text(gender)
    
    await websocket.close()

# ✅ Ensure FastAPI Binds to Render's Dynamic Port


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Render assigns a dynamic port
    uvicorn.run
