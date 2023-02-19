"""
"""
from random import randrange


def sentiment_string():
    """
    """

    sentiment = "positive"
    sentiment_int = randrange(0, 6)

    if sentiment_int == 0:
        sentiment = "negative"
    elif sentiment_int == 1:
        sentiment = "mixed"
    elif sentiment_int == 2:
        sentiment = "dubious"
    elif sentiment_int == 3:
        sentiment = "nice"
    else:
        sentiment = "positive"

    return sentiment
