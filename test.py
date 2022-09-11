import tweepy
import os

api_key = os.getenv("TWITTER_API_KEY")
api_key_secret = os.getenv("TWITTER_API_KEY_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

def twitter_api():
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth)#, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

    return api

api = twitter_api()

 
try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')


stored_image = "/home/guimas/Documents/beatbot/output/cover.png"
result = api.update_with_media(stored_image, status="Test!")

