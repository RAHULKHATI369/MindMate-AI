# backend/app.py
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

# local imports
from emotion_model import get_pipelines, analyze_text
from scoring import compute_mental_health_score
from llm_logic import get_assistant_message
from database import init_db, save_session, recent_negative_count

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"  # dev uses vite; production serve from build

app = Flask(__name__, static_folder=str(FRONTEND_DIR / "dist"), static_url_path="/")
CORS(app)  # Allow cross-origin dev requests

# initialize DB and pipelines
init_db()
sentiment_pipeline = get_pipelines()

@app.route("/")
def index():
    # In production, serve built frontend (frontend/dist). In dev, Vite dev server serves UI.
    if (FRONTEND_DIR / "dist" / "index.html").exists():
        return send_from_directory(str(FRONTEND_DIR / "dist"), 'index.html')
    return "Frontend not built. During development run `npm run dev` in frontend/"

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json() or {}
    user_text = data.get("text", "")
    if not isinstance(user_text, str) or not user_text.strip():
        return jsonify({"error": "empty text"}), 400

    analysis = analyze_text(user_text, sentiment_pipeline)
    history_neg = recent_negative_count(10)
    score = compute_mental_health_score(analysis, history_neg)
    reply = get_assistant_message(user_text, analysis, score)
    save_session(user_text, analysis.get('emotion'), analysis.get('sentiment_label'), score, reply)

    return jsonify({
        "analysis": analysis,
        "score": score,
        "reply": reply
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
