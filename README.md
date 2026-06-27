# Local AI Resume Analyzer

A fast, secure, and privacy-focused web application that analyzes resumes locally on your machine. This tool evaluates PDF resumes to generate an ATS compatibility score, detailed structural feedback, and optimization suggestions without sending data to external APIs.

## 🚀 Features
* **100% Local Execution:** Runs completely offline using Ollama, ensuring your personal resume data never leaves your device.
* **Intelligent ATS Scoring:** Provides immediate scoring, identifying missing critical skills and structural weaknesses.
* **Actionable Feedback:** Generates rewritten profile summaries and impact-driven project bullet points.
* **Clean Web UI:** A modern, minimal single-page interface for seamless file uploads and results viewing.

## 🛠️ Tech Stack
* **Frontend:** React.js, Tailwind CSS / HTML / JavaScript
* **Backend:** Python, FastAPI
* **AI Model:** Gemma 4 E4B (running locally via Ollama)

## 📦 Model Specifications (Gemma 4 E4B)
* **Parameters:** 4.5B effective parameters
* **Context Window:** 128K tokens
* **Execution Framework:** Ollama
