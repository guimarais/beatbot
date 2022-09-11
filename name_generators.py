"""
"""
import urllib
from xml.dom import minidom
from optparse import OptionParser
import subprocess
import re
from html.parser import HTMLParser
import requests
from random import randrange
from tenacity import retry

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.get_data = False;
        self.quotes = []

    def handle_starttag(self, tag, attrs):
        if tag == "dt":
            if attrs[0][0] == 'class' and attrs[0][1] == 'quote':
                self.get_data = True
        pass

    def handle_endtag(self, data):
        pass

    def handle_data(self, data):
        if self.get_data:
            self.quotes.append(data)
            self.get_data = False

@retry
def getBandName():
    """
    """
    random_wiki_url = "http://en.wikipedia.org/w/api.php?format=xml&action=query&list=random&rnnamespace=0&rnlimit=1"
    dom = minidom.parse(urllib.request.urlopen(random_wiki_url))

    btitle = []
    for line in dom.getElementsByTagName('page'):
        btitle.append(line.getAttributeNode('title').nodeValue)
    
    name_parsed = re.sub("[\(\[].*?[\)\]]", "", btitle[0])
    
    utf_name = bytes(name_parsed, 'utf-8').decode('utf-8', 'ignore')
    
    #Eliminate commas, so locations in wikipedia look more like a proper name
    utf_name = utf_name.replace(",","")
    
    # Return only the first three words and remove trailing and leading blankspaces
    return ' '.join(utf_name.split()[:3]).strip()
    

@retry
def getAlbumTitle():
    """
    """
    random_quote_url = "http://www.quotationspage.com/random.php"
    page = urllib.request.urlopen(random_quote_url).read()
    parser = MyHTMLParser()
    parser.feed(str(page))

    num_quotes = len(parser.quotes)
    quote = parser.quotes[randrange(0, num_quotes)].rstrip('.')

    last_set = randrange(3,5)
    words = quote.split()

    if last_set > len(words):
        last_set = len(words)

        
    title = (" ").join(words[-last_set:])
    parsed_title = re.sub("[\(\[].*?[\)\]]", "", title)
    
    # Convert to utf8 and remove leading and trailing whitespaces with .strip()
    utf_title = bytes(parsed_title, 'utf-8').decode('utf-8', 'ignore').strip()
    
    #Eliminate commas
    utf_title = utf_title.replace(",","")    
    
    return utf_title
