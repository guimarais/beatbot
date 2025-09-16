"""
Function to get a random quote fomr quotationspages.com
"""
import requests
from bs4 import BeautifulSoup
import random
import re

def get_random_album_title():
    """
    Fetches a random quote from quotationspage.com and returns 
    the first N words (where N is randomly chosen between 2-5).
    
    Returns:
        tuple: (selected_words, full_quote, author, N)
    """
    try:
        # Fetch the webpage
        url = "http://www.quotationspage.com/random.php"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse the HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the quote - typically in a <dt> tag with class "quote"
        quote_element = soup.find('dt', class_='quote')
        if not quote_element:
            # Fallback: look for any <dt> tag that might contain the quote
            quote_element = soup.find('dt')
        
        if not quote_element:
            raise ValueError("Could not find quote on the page")
        
        # Extract the quote text
        quote_text = quote_element.get_text().strip()
        
        # Clean up the quote text (remove extra whitespace, quotes, etc.)
        quote_text = re.sub(r'\s+', ' ', quote_text)
        quote_text = quote_text.strip('"\'')
        
        # Find the author (usually in the next <dd> tag)
        author_element = quote_element.find_next('dd')
        author = author_element.get_text().strip() if author_element else "Unknown"
        
        # Split quote into words
        words = quote_text.split()
        
        if len(words) == 0:
            raise ValueError("Quote contains no words")
        
        # Generate random N between 2 and 5
        N = random.randint(2, 5)
        
        # Take first N words (or all words if quote is shorter than N)
        selected_words = words[:min(N, len(words))]
        selected_text = ' '.join(selected_words)
        
        return selected_text, quote_text, author, N
        
    except requests.exceptions.RequestException as e:
        return f"Error fetching quote: {e}", "", "", 0
    except Exception as e:
        return f"Error processing quote: {e}", "", "", 0

# Example usage
if __name__ == "__main__":
    selected, full_quote, author, n = get_random_album_title()
    
    print(f"Random N chosen: {n}")
    print(f"First {n} words: '{selected}'")
    print(f"Full quote: '{full_quote}'")
    print(f"Author: {author}")
    
    # Run it a few more times to see different results
    print("\n" + "="*50)
    print("Running a few more times:")
    
    for i in range(3):
        selected, full_quote, author, n = get_random_album_title()
        print(f"\nAttempt {i+1}:")
        print(f"First {n} words: '{selected}'")
        print(f"Full quote: '{full_quote}' - {author}")

        