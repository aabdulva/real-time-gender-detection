import torch
from torchaudio.transforms import MFCC
import speech_recognition as sr
import numpy as np
import librosa
import torch
import os
from transformers import Wav2Vec2ForSequenceClassification

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")

# Load Wav2Vec2 model from Hugging Face (more stable than Fairseq)
def get_model():
    global model
    if "model" not in globals():
        model = Wav2Vec2ForSequenceClassification.from_pretrained("facebook/wav2vec2-large-960h-lv60")
    return model

# Define Gender Classification Model
class GenderClassifier(torch.nn.Module):
    def __init__(self):
        super(GenderClassifier, self).__init__()
        self.fc = torch.nn.Linear(512, 2)
    def forward(self, x):
        return torch.softmax(self.fc(x), dim=1)

classifier = GenderClassifier()

def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        return audio