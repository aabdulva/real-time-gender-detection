import React, { useState, useEffect } from 'react';

function App() {
    const [gender, setGender] = useState("Listening...");
    
    useEffect(() => {
        const ws = new WebSocket("ws://localhost:8000/detect_gender");
        ws.onmessage = (event) => {
            setGender(event.data);
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