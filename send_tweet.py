"""
Send a tweet from the command line with just text to test the APIs.
If ran in stand alone you must provide a string as sys.argv[1]
"""

import sys
import os
import tweepy

# Reads relevant system variables
API_KEY = os.getenv("TWITTER_API_KEY")
API_KEY_SECRET = os.getenv("TWITTER_API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


def twitter_api(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    """
    Creates an api object that allows authentication
    """
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth)  # , wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

    return api


# Command line
if __name__ == "__main__":

    # Creates the api object
    tw_api = twitter_api(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Tries to authenticate
    try:
        tw_api.verify_credentials()
        print("Successful Authentication")
    except:
        print("Failed authentication")

    # Send the tweet if the argument for the run is a string
    # print(sys.argv[1])
    if isinstance(sys.argv[1], str):
        RESULT = tw_api.update_status(status=sys.argv[1])
        #RESULT = twitter_api.update_with_media("./output/cover.png",sys.argv[1])

    else:
        raise TypeError("You must tweet a string as the argument!")
