"""
Testcases for the html_parse module.
"""
from bs4 import BeautifulSoup
import html_parse

html = """
<doctype html>
<html>
  <body>
    <h1><a href="foo">This is a headline</a></h1>
    <h2><a href="bar">Also a headline</a></h2>
    <h3>Not a headline!</h3>
    <p><a>Not a headline</a></p>
    <code>code</code>
  </body>
</html>
"""

soup = BeautifulSoup(html)

def test_is_headline():
    assert html_parse.is_headline(soup.h1)
    assert html_parse.is_headline(soup.h2)
    assert not html_parse.is_headline(soup.h3)
    assert not html_parse.is_headline(soup.p)

def test_headline_text():
    assert html_parse.headline_text(soup.h1) == "This is a headline"
    assert html_parse.headline_text(soup.h2) == "Also a headline"

def test_all_headlines():
    assert html_parse.all_headlines(soup) == [
        'This is a headline',
        'Also a headline'
    ]