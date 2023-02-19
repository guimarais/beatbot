"""
Module review_write specifically asks for a review
"""

import os
import openai


def review_write(band_name, album_title, sentiment):
    """
    """
    openai.api_key = os.getenv("OPENAI_API_KEY")

    gpt_prompt = f'Make a {sentiment} short review for a music album called "{album_title}" from a band called "{band_name}" in under 280 characters.'

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=gpt_prompt,
        temperature=0.91,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    return response["choices"][0]["text"][2:]

if __name__ == "__main__":
    out_str = review_write("Underworld", "Born Slippy", "positive")
    print(out_str)
