import React, { useState, useEffect } from 'react';

function App() {
    const [gender, setGender] = useState("Listening...");

    useEffect(() => {
        // Replace 'localhost:8000' with your Render backend URL
        const backendUrl = "wss://real-time-gender-detection-web.onrender.com/detect_gender";  // Use "wss://" for WebSocket connection
        
        const ws = new WebSocket(backendUrl);
        
        ws.onmessage = (event) => {
            setGender(event.data);
        };
        
        ws.onerror = (error) => {
            console.error("WebSocket Error:", error);
        };

        return () => ws.close();
    }, []);

    return (
        <div style={{ textAlign: "center", marginTop: "20%" }}>
            <h1>🎤 Real-Time Gender Detection</h1>
            <h2>{gender}</h2>
        </div>
    );
}

export default App;
