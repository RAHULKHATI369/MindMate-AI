# MindMate-AI
# MindMate AI – Emotional Wellness Assistant

MindMate AI is a lightweight, privacy‑friendly emotional support assistant built with **Flask (Backend)** + **React/Vite (Frontend)**, powered by **Google Gemini AI** for natural mental‑health style responses.

This project runs fully locally, includes a safe fallback offline mode, and keeps API keys secure.

---

## 🚀 Features

* Emotion‑aware CBT‑style responses
* Google Gemini (gemini-pro) integration
* Secure `.env` handling (backend)
* Local fallback AI responses (no internet needed)
* Clean modular backend structure
* Fully functional React frontend
* Professional API routing
* Easy GitHub deployment

---

## 📂 Project Structure

```
mindmate_ai/
│
├── backend/
│   ├── app.py
│   ├── llm_logic.py
│   ├── emotion_model.py
│   ├── scoring.py
│   ├── database.py
│   ├── requirements.txt
│   └── config/
│       └── .env  ← Google API key stored here
│
└── frontend/
    ├── index.html
    ├── src/
    ├── package.json
    └── vite.config.js
```

---

## 🔐 Environment Variables (Backend)

Create file:

```
backend/config/.env
```

Add:

```
GOOGLE_API_KEY=YOUR_GEMINI_KEY_HERE
```

Never push `.env` to GitHub.

Add to `.gitignore`:

```
backend/config/.env
*.env
```

---

## ⚙️ Backend Setup (Flask)

Create virtual environment:

```
cd backend
python3 -m venv venv
source venv/bin/activate
```

Install packages:

```
pip install -r requirements.txt
pip install google-generativeai python-dotenv
```

Run backend:

```
python app.py
```

Backend will run at:

```
http://localhost:8080
```

---

## 🎨 Frontend Setup (React + Vite)

```
cd frontend
npm install
npm run dev
```

Frontend will run at:

```
http://localhost:5173
```

---

## 🔗 Connecting Frontend to Backend

Create `frontend/.env`:

```
VITE_API_URL=http://localhost:8080
```

Restart frontend server.

---

## 📤 GitHub Push Instructions

### 1. Initialize Repo

```
git init
git add .
git commit -m "Initial MindMate AI commit"
```

### 2. Add GitHub Remote

```
git remote add origin https://github.com/USERNAME/REPO.git
```

### 3. Push Code

```
git branch -M main
git push -u origin main
```

---

## 📦 requirements.txt Example

```
flask
flask-cors
google-generativeai
python-dotenv
```

---

## 🧠 How Gemini AI Works in This Project

* Reads user message
* Reads emotion & sentiment analysis
* Reads wellness score
* Creates CBT-style structured prompt
* Gemini responds with:

  * empathic intro
  * grounding exercise
  * cognitive reframing
  * supportive question
  * safety note (if score ≤ 20)

---

## 🛡️ Safety & Privacy

* No user messages stored by default
* Local fallback ensures always-on support
* API key safely stored in backend/config/.env
* No sensitive logs stored

---

## 📝 Future Improvements

* User authentication
* Chat history saving
* Dark/Light UI mode
* Speech‑to‑Text input
* AI personality customization

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first.

---

## 📄 License

This project is open-source under the MIT License.

---

## ✨ Author

**Rahul Khati** — Full‑Stack & AI Developer.

MindMate AI is built with the aim of supporting emotional wellness with lightweight, accessible AI.
