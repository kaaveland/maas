"""
Testcases for the text module.
"""

import text

def test_prefix_has_length():
    assert len(text.null_prefix(3)) == 3
    assert len(text.null_prefix(9)) == 9

def test_after_shifting_null_prefix_shifted_word_is_last():
    initial = text.null_prefix(2)
    shifted = text.shift('foo', initial)
    assert text.last_word(shifted) == 'foo'

sentence = ["this", "is", "a", "test"]

def test_should_find_expected_prefix_mapping():
    expected = {}
    null_prefix = text.null_prefix(2)
    expected[null_prefix] = ["this"]
    shifted = text.shift("this", null_prefix)
    expected[shifted] = ["is"]
    shifted2 = text.shift("is", shifted)
    expected[shifted2] = ["a"]
    shifted3 = text.shift("a", shifted2)
    expected[shifted3] = ["test"]
    assert text.find_prefixes(sentence, 2) == expected

def test_merging_chains():
    null_prefix = text.null_prefix(1)
    left, right = {null_prefix: ["first", "second"]}, {null_prefix: ["third"]}
    assert text.merge(left, right) == {null_prefix: ["first", "second", "third"]}
    shifted = text.shift("test", null_prefix)
    left[shifted] = ["word"]
    assert text.merge(left, right) == {null_prefix: ["first", "second", "third"], shifted: ["word"]}

def test_choice_should_yield_element_from_sequence():
    numbers = range(20)
    for _ in numbers:
        assert text.choice(numbers) in numbers

def test_can_continue_requires_prefix_to_be_in_chain():
    prefix = text.null_prefix(3)
    chain = {}
    assert not text.can_continue(prefix, chain)
    chain[prefix] = [] # no possible choices
    assert not text.can_continue(prefix, chain)
    chain[prefix] = ["possible", "choices"]
    assert text.can_continue(prefix, chain)

def test_next_word_should_be_chosen_based_on_candidates():
    prefix = text.null_prefix(2)
    chain = {prefix: ["only_candidate"]}
    assert text.next_word(prefix, chain) == "only_candidate"

def test_generate_only_generates_until_it_can_not_continue():
    empty_chain = {}
    assert not text.generate(empty_chain)

def test_generate_always_starts_with_words_from_null_prefix_choices():
    chain = {text.null_prefix(2): ["choice"]}
    assert text.generate(chain, 2) == "choice"

def test_a_loop_in_the_chain_will_be_max_words_words_long():
    null_prefix = text.null_prefix(1)
    chain_with_loop = {null_prefix: ["foo"],
                       text.shift("foo", null_prefix): ["bar"],
                       text.shift("bar", null_prefix): ["foo"]}
    actual = text.generate(chain_with_loop, max_words=10)
    assert len(actual.split()) == 10
