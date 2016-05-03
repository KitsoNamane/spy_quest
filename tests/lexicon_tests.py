from nose.tools import *
from spy_quest import lexicon


def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east west")
    assert_equal(result, [('direction', 'north'),
                           ('direction', 'south'),
                           ('direction', 'east'),
                           ('direction', 'west')])


def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go seduce kill torture")
    assert_equal(result, [('verb', 'go'),
                           ('verb', 'seduce'),
                           ('verb', 'kill'),
                           ('verb', 'torture')])


def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of out")
    assert_equal(result, [('stop', 'the'),
                           ('stop', 'in'),
                           ('stop', 'of'),
                           ('stop', 'out')])


def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess Dinah lounge")
    assert_equal(result, [('noun', 'bear'),
                           ('noun', 'princess'),
                           ('noun', 'dinah'),
                           ('noun', 'lounge')])


def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                           ('number', 91234)])


def test_errors():
    assert_equal(lexicon.scan("ASDEgh"), [('error', 'asdegh')])
    result = lexicon.scan("bear  princess IAS rung")
    assert_equal(result, [('noun', 'bear'),
                           ('noun', 'princess'),
                           ('error', 'ias'),
                           ('error', 'rung')])


