# scoring.py
def compute_mental_health_score(analysis, history_count_negative=0):
    """
    Returns a wellness score between 0 (very poor) and 100 (excellent).
    analysis: dict from analyze_text
    history_count_negative: int, number of recent negative sessions
    """
    base = 70.0
    sentiment = analysis.get('sentiment_label', 'neutral')
    s = float(analysis.get('sentiment_score', 0.5))

    if sentiment == 'negative':
        penalty = s * 40.0  # up to -40
        base -= penalty
    elif sentiment == 'positive':
        add = s * 20.0
        base += add

    # penalize recent repeated negatives
    base -= min(history_count_negative * 5.0, 25.0)

    # clamp
    score = max(0.0, min(100.0, base))
    return round(score, 1)
