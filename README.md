Markov as a service
====================

Probably most people have been amused by some sort of computer program that
spews out nonsense-text at some point. It turns out that these are relatively
simple to create. This workshop is all about implementing a program like that
and exposing it as a service over http. To create the nonsense-text we will
use a technique I know as markov chains. The workshop has several parts:

- Learning from text to generate "plausible" text
- Scraping web pages for text to use for training
- Publishing a service that combines the two, as in go to
  http://foo.com/bbc.co.uk to scrape from bbc.co.uk and generate nonsense-text
  from it.

Code
-----
Install the dependencies with:
```bash
pip install -r requirements.txt
```

The code has been organized into 3 main files:
- text.py for training and generation of text
- html_parse.py for scraping newspaper headlines from webpages
- webapp.py to expose it as an http service

For each of these files, there is a test_-file which contains test-cases that
specify the expected behaviour of the skeleton functions in the file.

To run the tests in a file, use the py.test executable:
```bash
$ py.test test_html_parse.py
```
To run the test cases for all files, simply omit the file name.

Algorithm
--------
The algorithm used to generate the text is very simple but a bit difficult to
explain without an example. There are 2 phases; training and generating. Both of
these share a parameter called `order` that will determine how closely the
output will match the input. The training phase creates a data structure (I call
this the markov chain) that the generating phase uses to create text. It is a
mapping from a "prefix" of length `order` to a list of words that have been
known to follow the prefix.

With `order = 2`, the following could be a mapping:
```
The algorithm => [used]
algorithm used => [to]
used to => [generate]
```
There's also a special prefix that denotes the start of a text:
```
null null => [The, There's]
null The => [algorithm]
null There's => [also]
```

To create this structure, follow this recipe:
* Start with the null prefix as the current prefix
* For each word in the input text:
  - Append it to the list of words that can follow the current prefix
  - Shift the current word to the end of the current prefix and remove the first
    part of the current prefix.

To generate text from this structure:
* Start with the null prefix as the current prefix
* While there are any words known to follow the current prefix
  - Choose a random word that has followed the current prefix
  - Append it to the generated text
  - Shift the current word to the end of the current prefix

Scraping
----------
It doesn't actually matter exactly what text source that's used, but I chose to
use norwegian newspapers db.no, ap.no and vg.no while developing this. I used
the text inside the anchor tags that were in h1-h6 tags. The crucial thing about
the scraping module is really just that it extracts the text you expect it
to. The tests reflect the structure on db.no, ap.no and vg.no.

Service
--------
I chose to use flask to expose this as a service. Flask is very well documented
and easy to deploy on e.g. heroku:
https://devcenter.heroku.com/articles/getting-started-with-python

The flask app is more or less empty and just waiting to hook up the scraping
code and text code. It is setup in debug-mode, don't run it like that in
production.

Improvements
----------
The straightforward app is very simple. Here are some ideas for making it more
excellenter:

- The basic app uses prefixes that consist of words. It is possible to use the
  same algorithm using character-based prefixes and suffixes. Written this way,
  you could possible generate code. It would be interesting to code generate
  based on its own code. Right? Can't be worse than xmlbeans anyway...
- Persistent state using sqlite3 to store the chain. This way, when something is
  trained it is never forgotten. This is tricky to do in a general way because
  using chains of different `order`s need to be handled intelligently.
- Persistent state using something more hipster than sqlite3, like mongodb.
- A GUI using twitter bootstrap and ajax to responsively train and generate
  text.
- Websockets. Because why not.
- Smarter text parsing - making the program understand punctuation and where
  sentences start and stop.
