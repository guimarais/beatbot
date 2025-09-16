# %%
from openai import OpenAI
from beatbot.get_random_album_title import get_random_album_title
from beatbot.get_random_artist_name import get_random_artist_name
from dotenv import load_dotenv
import requests
import datetime
import os
from atproto import Client as BskyClient
from atproto import models
from PIL import Image

load_dotenv()

bsky_client = BskyClient()
bsky_client.login(os.getenv('BSKY_USER'), os.getenv('BSKY_PASSWORD'))

openai_client = OpenAI() 

ARTIST_NAME = get_random_artist_name()
ALBUM_NAME = get_random_album_title()[0]
ARTIST_NAME, ALBUM_NAME

# %%
image_prompt = f"""
                Generate the cover art for an album called \"{ALBUM_NAME}\" from a band called \"{ARTIST_NAME}\"
                """

response = openai_client.images.generate(
    model="dall-e-3",
    prompt=image_prompt,
)

image_url = response.data[0].url
response = requests.get(image_url)

# Gets the filename with a timestamp
time_prefix = datetime.datetime.now().strftime("%Y%m%d%H%M")
image_filename = f"./images/{time_prefix}_album.jpg"

if response.status_code == 200:
    with open(image_filename, 'wb') as file:
        file.write(response.content)


# Resize in place
im = Image.open(image_filename)
im = im.resize((512, 512))
im.save(image_filename)

# Upload to bsky
with open(image_filename, "rb") as f:
    img_data = f.read()

# Add image aspect ratio to prevent default 1:1 aspect ratio
# Replace with your desired aspect ratio
aspect_ratio = models.AppBskyEmbedDefs.AspectRatio(height=100, width=100)

# Make the review
review_prompt = f"""
                 Make a short review about an imaginary music album named \'{ALBUM_NAME}\' by an imaginary musical artist called \'{ARTIST_NAME}\'.
                 Both the music album and the artist name do not really exist, this is for a fun experiment.
                 The review must be under 250 characters long.
                 Before presenting the review, double-check if it is under 250 characters
                 """

response = openai_client.responses.create(
  model="gpt-3.5-turbo",
  input=[
    {
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": review_prompt
        }
      ]
    }
  ],
  temperature=1,
  max_output_tokens=250
)

# Post to bluesky
alt_str = f"Album cover for \'{ALBUM_NAME}\' by \'{ARTIST_NAME}\'"

bsky_client.send_image(
    text=response.output_text,
    image=img_data,
    image_alt=alt_str,
    image_aspect_ratio=aspect_ratio,
)


