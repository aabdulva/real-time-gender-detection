# README.md (Project Overview)
```
# Real-Time Gender Detection from Audio

## Overview
This project detects the gender of a speaker in real-time from an audio stream. The backend runs on FastAPI, and the frontend is built with React.js.

## Features
- Real-time microphone audio processing
- AI-powered gender classification
- WebSockets for continuous updates

## Installation
### Backend

cd backend
pip install -r requirements.txt
uvicorn app:app --reload

### Frontend

cd frontend
npm install
npm start


## Deployment (Docker)

docker-compose up --build


## Challenges Faced
During development and deployment, several challenges were encountered:

### 1. **Missing Dependencies for PyAudio**
- PyAudio requires **PortAudio**, which was missing on many systems.
- Solution: Installed PortAudio manually via:
  - **Ubuntu:** `sudo apt install portaudio19-dev`
  - **macOS:** `brew install portaudio`
  - **Windows:** Installed precompiled binaries.

### 2. **GitHub Blocking Push Due to Secrets**
- GitHub **detected and blocked a push** because it found a private key.
- Solution:
  - Found the file using `git rev-list --objects --all | grep blobid`.
  - Removed sensitive files and used `.gitignore` to prevent future leaks.

### 3. **Missing `index.html` in React Build**
- The React build failed due to a missing `index.html`.
- Solution: Created `frontend/public/index.html` manually.

### 4. **`react-scripts` Not Found**
- Running `npm start` resulted in `react-scripts: not found`.
- Solution: Reinstalled it manually using `npm install react-scripts --save`.

### 5. **Heroku SSL Certificate Issue (`SELF_SIGNED_CERT_IN_CHAIN`)**
- Heroku login failed due to SSL certificate errors.
- Solution:
  - Set `heroku config:set SSL_CERT_FILE=/dev/null`.
  - Used `heroku login --interactive` as a workaround.

### 6. **Heroku Asking for a Credit Card**
- Heroku requires a credit card for all deployments.
- Solution: Switched to **Render.com** for free hosting.

### 7. **Git Ignoring Specific Files & Folders**
- Needed to ignore `frontend/node_modules/` and `package-lock.json`.
- Solution: Updated `.gitignore`:
  ```
  frontend/node_modules/
  backend/node_modules/
  frontend/package-lock.json
  .env
  ```

### 8. **PyAudio Not Supported on Render**
- Render deployment failed because **PyAudio depends on system libraries**.
- Solution:
  - Removed `pyaudio` from `requirements.txt`.
  - Used `soundfile` and `speechrecognition` as alternatives.