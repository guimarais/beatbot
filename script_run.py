"""
"""

from review_openai import review_write
from name_generators import getBandName
from name_generators import getAlbumTitle
from craiyon import image_craiyon
from sentiment import sentiment_string
from place_title import place_title
import os
import tweepy

# Brute force results
album_title = getAlbumTitle()        

band_name = getBandName()
    
prompt_image = f"Cover art for an album called \"{album_title}\" of an artist called \"{band_name}\""

output_image = image_craiyon(prompt_image)

place_title(band_name, album_title)

sentiment = sentiment_string()

review_text = review_write(band_name, album_title, sentiment)

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

stored_image = './output/cover.png'
result = api.update_status_with_media(review_text, stored_image)

