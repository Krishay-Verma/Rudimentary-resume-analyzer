import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [score, setScore] = useState(null);
  const [result, setResult] = useState("");

  const uploadResume = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    setResult("");

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/analyze",
        formData
      );

      setScore(res.data.score);
      setResult(res.data.analysis);
    } catch (err) {
      setResult("Error analyzing resume.");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>Resume Analyzer AI</h1>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={uploadResume}>
        Analyze Resume
      </button>

      {loading && <p>Analyzing...</p>}

      {score !== null && (
        <div className="score">
          ATS Score: {score}/100
        </div>
      )}

      <pre>{result}</pre>
    </div>
  );
}

export default App;

