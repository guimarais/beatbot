import re
import wikipedia

def clean_title(title):
    """
    Clean the title by removing unwanted characters and phrases.
    
    Args:
        title (str): The original title
        
    Returns:
        str: The cleaned title
    """
    # Remove everything between brackets (including the brackets)
    # This handles (), {}, and []
    title = re.sub(r'\([^)]*\)', '', title)  # Remove (...)
    title = re.sub(r'\{[^}]*\}', '', title)  # Remove {...}
    title = re.sub(r'\[[^\]]*\]', '', title)  # Remove [...]
    
    # Remove "List of " from the beginning
    if title.startswith("List of "):
        title = title[8:]  # Remove first 8 characters
    
    # Remove air quotes (quotation marks)
    title = title.replace('"', '').replace('"', '').replace('"', '')
    title = title.replace("'", '').replace("'", '').replace("'", '')
    
    # Clears year ranges
    title = re.sub(r'\b\d{4}(?:[-–]\d{2,4})?\b', '', title)

    # Clean up extra whitespace
    title = ' '.join(title.split())
    
    return title.strip()

def get_random_artist_name():
    """
    Fetches a random Wikipedia page title and cleans it to produce a plausible artist name.

    This function uses the Wikipedia API to select a random page title, then processes
    the title to remove extraneous characters, phrases, and formatting that are unlikely
    to be part of an artist's name. The result is a string that can be used as a random
    artist name for testing or creative purposes.

    Returns:
        str: A cleaned, plausible artist name.
    """

    artist_name = clean_title(wikipedia.random())

    return artist_name

# Example usage
if __name__ == "__main__":
    ARTIST_NAME = get_random_artist_name()
    print(f"Random Artist Name: '{ARTIST_NAME}'")