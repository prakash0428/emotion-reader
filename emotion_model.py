from textblob import TextBlob

def predict_emotion(text):
    """
    Ye function user ke text ka sentiment analyze karta hai
    aur emotion return karta hai: Positive, Negative ya Neutral
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.1:
        return "Positive 😊"
    elif polarity < -0.1:
        return "Negative 😞"
    else:
        return "Neutral 😐"
