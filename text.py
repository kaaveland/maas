"""
For learning from text and generating text.
"""
import random

# For a 'prefix'-type that is central to an easy markov-chain algorithm.
# It is used to index words into the markov chain, both for assignment and lookup.
# Needs to be an immutable type (a tuple or a namedtuple is most intuitive)

def shift(word, prefix):
    """Shift word onto prefix such that word is last and the current first word disappears."""
    pass

def last_word(prefix):
    """Returns the last word in prefix."""
    pass

def null_prefix(length=1):
    """A null-prefix is 'before' the start of a text, like ^ in a regex.

    It is 'empty' or not initialized."""

    pass

# Training algorithm to take a list of words and output a chain.
# A chain is a mapping from prefixes to all possible words that may follow a prefix.
# Prefixes have a length (order of the chain).

def find_prefixes(words, length=1):
    """A mapping from prefixes to their suffix in list of words.

    The structure of the returned key-value mapping is:
    {
      null_prefix: [first_word],
      shifted_null_prefix: [second_word],
      shifted_shifted_null_prefix: [words known to follow this prefix]
    }
    """
    pass

def merge(*chains):
    """Merge several chains into one chain containing the same data.

    The effect should be that the result contains the training data from all the chains
    provided as arguments.
    """
    pass

def chain_from(sentences, length=1):
    """Return a chain that has been built by using it on every sentence in sentences.

    Sentences is a list of strings."""
    pass

# Generating text

def choice(alternatives):
    """Choose a random alternative from alternatives."""
    pass

def can_continue(prefix, chain):
    """False when we don't know of any continuation for prefix."""
    pass

def next_word(prefix, chain):
    """Choose the next word based on our current prefix and chain.

    Only words that are known to follow prefix can be chosen."""
    pass

def generate(chain, length=1, max_words=100):
    """Generates up to `max_words` words of text based on `chain`, using a prefix of order `length`.

    We need to have a max_words to prevent infinite loops, a chain such as:
    {'foo': ['bar'], 'bar': ['foo']}
    Is entirely legal (and quite likely to happen at some point)."""
    pass
