# database.py
import sqlite3
from datetime import datetime
from pathlib import Path

DB_FILE = Path(__file__).parent / "mindmate_sessions.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        user_text TEXT,
        emotion TEXT,
        sentiment TEXT,
        score REAL,
        assistant_reply TEXT
    )
    ''')
    conn.commit()
    conn.close()

def save_session(user_text, emotion, sentiment, score, assistant_reply):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
    INSERT INTO sessions (timestamp, user_text, emotion, sentiment, score, assistant_reply)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (datetime.utcnow().isoformat(), user_text, emotion, sentiment, score, assistant_reply))
    conn.commit()
    conn.close()

def recent_negative_count(limit=10):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT sentiment FROM sessions ORDER BY id DESC LIMIT ?', (limit,))
    rows = c.fetchall()
    conn.close()
    return sum(1 for r in rows if (r[0] or '').lower() == 'negative')
