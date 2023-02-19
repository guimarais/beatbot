"""
Send a tweet from the command line with just text to test the APIs.
If ran in stand alone you must provide a string as sys.argv[1]
"""

import sys
import os
import tweepy

# Reads relevant system variables
api_key = os.getenv("TWITTER_API_KEY")
api_key_secret = os.getenv("TWITTER_API_KEY_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


def twitter_api():
    """
    Creates an api object that allows authentication
    """
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth)  # , wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

    return api


# Command line 
if __name__ == "__main__":

    # Creates the api object
    api = twitter_api()

    # Tries to authenticate
    try:
        api.verify_credentials()
        print("Successful Authentication")
    except:
        print("Failed authentication")

    # Send the tweet if the argument for the run is a string
    # print(sys.argv[1])
    if type(sys.argv[1]) == str:
        result = api.update_status(status=sys.argv[1])
    else:
        raise TypeError("You must tweet a string as the argument!")
