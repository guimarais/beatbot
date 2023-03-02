"""
Functions for randomized outputs
"""
from random import randrange


def sentiment_string():
    """
    Returns a random string with a quality (sentiment).
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


def cover_string():
    """
    Returns a random string with a type of cover art.
    """

    sentiment = "Nice"
    sentiment_int = randrange(0, 5)

    if sentiment_int == 0:
        sentiment = "Psychedelic"
    elif sentiment_int == 1:
        sentiment = "Abstract"
    elif sentiment_int == 2:
        sentiment = "Classic"
    elif sentiment_int == 3:
        sentiment = "Simple"
    else:
        sentiment = "positive"

    return sentiment


