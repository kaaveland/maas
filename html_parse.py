"""
Should extract things that look like headlines from html documents.
"""

import urllib
from bs4 import BeautifulSoup # http://www.crummy.com/software/BeautifulSoup/bs4/doc/

def is_headline(node):
    """False unless node is a h1-h6 node containing an anchor."""
    pass

def headline_text(node):
    """The text in headline node (text of anchor element)."""
    pass

def all_headlines(html_root_node):
    """A list of all headlines in html_root_node."""
    pass

def all_headlines_from(url):
    """Open url using `urlib` and extract all the headlines from it."""
    pass

def gather_headlines(webpages):
    """Return the aggregate list of every headline found in each webpage in `webpages`."""
    pass
