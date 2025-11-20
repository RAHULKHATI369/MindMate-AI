import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env from custom secure folder (recommended)
# If your .env is inside backend/config/.env:
load_dotenv("backend/config/.env")

# Read Google API key
GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
if GOOGLE_KEY:
    genai.configure(api_key=GOOGLE_KEY)
else:
    print("⚠️ GOOGLE_API_KEY not found, using local fallback mode only.")

# Choose Gemini Model
GEMINI_MODEL = "gemini-pro"   # Text model


# -------------------------------
# 1. Build Prompt
# -------------------------------
def build_prompt(user_text, analysis, score):
    prompt = f"""
You are a compassionate, non-judgmental mental health assistant that follows CBT-style micro-interventions.
User message: "{user_text}"
Detected emotion: {analysis.get('emotion')} (confidence: {analysis.get('emotion_confidence')})
Sentiment: {analysis.get('sentiment_label')} (score: {analysis.get('sentiment_score')})
Wellness score: {score} / 100

Rules:
- Start with a short empathic line (1-2 sentences).
- If sentiment is negative or score <= 40, include one grounding/breathing micro-exercise (max 2 steps).
- Provide one gentle cognitive reframe sentence.
- Ask one gentle question to learn more (if appropriate).
- If score <= 20, add a safety escalation line recommending professional help and emergency contacts (no judgement).
- Keep tone warm and concise, max 120 words.

Output ONLY the assistant message.
"""
    return prompt.strip()


# -------------------------------
# 2. Generate response using Gemini
# -------------------------------
def generate_response_gemini(prompt):
    try:
        model = genai.GenerativeModel(GEMINI_MODEL)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("Gemini API failed:", e)
        return generate_response_local(prompt)


# -------------------------------
# 3. Local fallback response (offline mode)
# -------------------------------
def generate_response_local(prompt):
    lines = []
    lines.append("I hear you — that sounds really tough right now. Thank you for sharing.")
    
    if "negative" in prompt or "score: 40" in prompt or "score: 20" in prompt:
        lines.append("Try this quick exercise: Breathe in for 4 seconds, hold for 2 seconds, and exhale slowly for 6 seconds.")

    lines.append("One way to reframe this is to consider what evidence supports your thought, and what evidence weakens it.")
    lines.append("Is there one small step you could take right now that might help you feel a little better?")
    
    if "score <= 20" in prompt or "score: 20" in prompt:
        lines.append("If you're feeling unsafe or thinking about harming yourself, please reach out to local emergency services or someone you trust immediately.")

    return "\n".join(lines)


# -------------------------------
# 4. Main function
# -------------------------------
def get_assistant_message(user_text, analysis, score):
    prompt = build_prompt(user_text, analysis, score)

    if GOOGLE_KEY:
        return generate_response_gemini(prompt)
    else:
        return generate_response_local(prompt)
