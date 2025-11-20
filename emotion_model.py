# emotion_model.py
# Simple, reliable sentiment -> basic emotion mapping using transformers pipeline.
import torch
from transformers import pipeline

def get_pipelines():
    """
    Returns a sentiment-analysis pipeline.
    This will download a small model on first run (internet needed).
    """
    sentiment = pipeline("sentiment-analysis")  # default model: distilbert-base-uncased-finetuned-sst-2-english
    return sentiment

def analyze_text(text, sentiment_pipeline):
    """
    Returns a simple analysis dict:
    - emotion: basic label ('sadness' or 'joy' fallback)
    - emotion_confidence: same as sentiment confidence
    - sentiment_label: 'positive'/'negative'
    - sentiment_score: probability
    """
    # ensure text is not too long for the pipeline
    short_text = text.strip()[:1000]
    try:
        res = sentiment_pipeline(short_text, truncation=True)[0]
    except Exception as e:
        # fallback minimal analysis
        return {
            "emotion": "neutral",
            "emotion_confidence": 0.5,
            "sentiment_label": "neutral",
            "sentiment_score": 0.5
        }

    label = res.get("label", "").lower()
    score = float(res.get("score", 0.0))
    # Map label names to simple emotions
    if "neg" in label:
        emotion = "sadness"
    elif "pos" in label:
        emotion = "joy"
    else:
        emotion = "neutral"

    return {
        "emotion": emotion,
        "emotion_confidence": round(score, 3),
        "sentiment_label": "negative" if "neg" in label else ("positive" if "pos" in label else "neutral"),
        "sentiment_score": round(score, 3)
    }
