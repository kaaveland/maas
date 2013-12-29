"""
For learning from text and generating text.
"""
import random
from collections import defaultdict

# For a 'prefix'-type that is central to an easy markov-chain algorithm.
# It is used to index words into the markov chain, both for assignment and lookup.
# Needs to be an immutable type (a tuple or a namedtuple is most intuitive)

def shift(word, prefix):
    """Shift word onto prefix such that word is last and the current first word disappears."""
    return prefix[1:] + (word,)

def last_word(prefix):
    """Returns the last word in prefix."""
    return prefix[-1]

def null_prefix(length=1):
    """A null-prefix is 'before' the start of a text, like ^ in a regex.

    It is 'empty' or not initialized."""
    return tuple([None for _ in range(length)])

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
    chain = defaultdict(list)
    prefix = null_prefix(length)
    for word in words:
        chain[prefix].append(word)
        prefix = shift(word, prefix)
    return chain

def find_prefixes(words, length=1):
    """Alternate solution using regular dict instead of defaultdict."""
    chain = {}
    prefix = null_prefix(length)
    for word in words:
        # Set chain[prefix] = [] if it not prefix in chain then append to chain[prefix]
        chain.setdefault(prefix, []).append(word)
        prefix = shift(word, prefix)
    return chain

def merge(*chains):
    """Merge several chains into one chain containing the same data.

    The effect should be that the result contains the training data from all the chains
    provided as arguments.
    """
    merged_chain = defaultdict(list)
    for chain in chains:
        for prefix, suffixes in chain.items():
            merged_chain[prefix].extend(suffixes)
    return merged_chain

def chain_from(sentences, length=1):
    """Return a chain that has been built by using it on every sentence in sentences.

    Sentences is a list of strings."""
    return merge(*[find_prefixes(sentence, length) for sentence in sentences])

# Generating text

def choice(alternatives):
    """Choose a random alternative from alternatives."""
    return random.choice(alternatives)

def can_continue(prefix, chain):
    """False when we don't know of any continuation for prefix."""
    return chain.get(prefix)

def next_word(prefix, chain):
    """Choose the next word based on our current prefix and chain.

    Only words that are known to follow prefix can be chosen."""
    return choice(chain[prefix])

def generate(chain, length=1, max_words=100):
    """Generates up to `max_words` words of text based on `chain`, using a prefix of order `length`.

    We need to have a max_words to prevent infinite loops, a chain such as:
    {'foo': ['bar'], 'bar': ['foo']}
    Is entirely legal (and quite likely to happen at some point)."""
    words = []
    prefix = null_prefix(length)
    for _ in range(max_words):
        if can_continue(prefix, chain):
            word = next_word(prefix, chain)
            words.append(word)
            prefix = shift(word, prefix)
    return ' '.join(words)

# When run with $ python text.py
if __name__ == '__main__':
    with open('dracula_chapter1.txt') as book:
        text = book.read()
        sentences = [[word.strip() for word in sentence.split()]
                     for sentence in text.split('.')]
        chain = chain_from(sentences, 2)
        print generate(chain, 2)
