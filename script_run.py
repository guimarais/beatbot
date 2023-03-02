"""
"""

from send_tweet import twitter_api
# from review_openai import review_write
from name_generators import get_band_name
from name_generators import get_album_title
from craiyon_image import craiyon_image
from place_title import place_title
from randomized_outputs import sentiment_string
from randomized_outputs import cover_string
import os
import tweepy

# Brute force results
album_title = get_album_title()

band_name = get_band_name()

sentiment = sentiment_string()

type_of_cover = cover_string()

prompt_image = (
    f'{type_of_cover} cover art for a music album called "{album_title}" of a music band called "{band_name}"'
)

output_image = craiyon_image(prompt_image, output_dir="/home/guimas/Documents/beatbot/output/")

place_title(band_name, album_title)

review_text = prompt_image  # review_write(band_name, album_title, sentiment)a
# print(review_text)# = "Test!"

API_KEY = os.getenv("TWITTER_API_KEY")
API_KEY_SECRET = os.getenv("TWITTER_API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Initialize API
tw_api = twitter_api(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

try:
    tw_api.verify_credentials()
    print("Successful Authentication")
except:
    print("Failed authentication")

stored_image = "/home/guimas/Documents/beatbot/output/cover.png"
# result = api.update_status_with_media(review_text, stored_image)

# result = api.update_status(status='Blip blop!')
result = tw_api.update_with_media(stored_image, review_text)

