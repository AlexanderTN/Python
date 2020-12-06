from nose.tools import *
from ex48 import lexicon

def test_direction():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [("direction", "north"),
                          ("direction", "south"),
                          ("direction", "east")])

def test_verbs():
    pass
    assert_equal(lexicon.scan("go"), [("verbs", "go")])

def test_stops():
    assert_equal(lexicon.scan("the"), [("stop_words", "the")])
    result = lexicon.scan("the in of")
    assert_equal(result, [("stop_words", "the"),
                          ("stop_words", "in"),
                          ("stop_words", "of")])

def tests_nouns():
    assert_equal(lexicon.scan("bear"), [("nouns", "bear")])
    result = lexicon.scan("bear princess")
    assert_equal(result, [("nouns", "bear"),
                          ("nouns", "princess")])

def tests_numbers():
    assert_equal(lexicon.scan("1234"), [("numbers", 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [("numbers", 3),
                          ("numbers", 91234)])

def test_error():
    assert_equal(lexicon.scan("AASDFASDFASDF"), [("errors", "AASDFASDFASDF")])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [("nouns", "bear"),
                          ("errors", "IAS"),
                          ("nouns", "princess")])


    