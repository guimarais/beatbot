"""
"""
from random import randrange
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def place_title(band_name, album_title):
    """
    """
    
    roulette = randrange(1,10)

    name = f"/home/guimas/Documents/beatbot/output/creation-{roulette}.png"

    img = Image.open(name)
    draw = ImageDraw.Draw(img)
    
    band_name_font = ImageFont.truetype(r'/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 20)
    album_name_font = ImageFont.truetype(r'/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 20)
    
    x_title = 10
    y_title = 20

    bg_color = (randrange(0, 256, 1), randrange(0, 256, 1), randrange(0, 256, 1))
    fg_color = (randrange(0, 256, 1), randrange(0, 256, 1), randrange(0, 256, 1))

    draw.text((x_title-1, y_title+1), band_name, font=band_name_font, fill=bg_color)
    draw.text((x_title-1, y_title-1), band_name, font=band_name_font, fill=bg_color)
    draw.text((x_title+1, y_title+1), band_name, font=band_name_font, fill=bg_color)
    draw.text((x_title+1, y_title-1), band_name, font=band_name_font, fill=bg_color)
    draw.text((x_title, y_title), band_name, font=band_name_font, fill=fg_color)
    
    x_title = 10
    y_title = 320
    
    bg_color = (randrange(0, 256, 1), randrange(0, 256, 1), randrange(0, 256, 1))
    fg_color = (randrange(0, 256, 1), randrange(0, 256, 1), randrange(0, 256, 1))

    draw.text((x_title-1, y_title+1), album_title, font=album_name_font, fill=bg_color)
    draw.text((x_title-1, y_title-1), album_title, font=album_name_font, fill=bg_color)
    draw.text((x_title+1, y_title+1), album_title, font=album_name_font, fill=bg_color)
    draw.text((x_title+1, y_title-1), album_title, font=album_name_font, fill=bg_color)
    draw.text((x_title, y_title), album_title, font=album_name_font, fill=fg_color)

    img.save("/home/guimas/Documents/beatbot/output/cover.png")
