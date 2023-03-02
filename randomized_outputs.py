"""
Functions for randomized outputs
"""

from random import randrange
from random import choice

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


def random_genre():
    """
    Chooses a random music genre taken from:
    https://gist.githubusercontent.com/sampsyo/1241307/raw/208ab2e4b5b576ebc51d801b039f93ee2bbc33ea/genres.txt
    """

    # Remove the \n
    genre = choice(list(open('genres.txt')))[:-1]

    return genre


if __name__=="__main__":
    print(random_genre())

