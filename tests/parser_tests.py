#! /usr/bin/env python
from nose.tools import *
from spy_quest import parser
from spy_quest import lexicon

empty_word = lexicon.scan("")


def test_peek():
    word_list = lexicon.scan("go north and rescue the princess")

    # tests when we have a wordlist #
    assert_equal(parser.peek(word_list), word_list[0][0])
    # tests when we don't have a wordlist
    assert_equal(parser.peek(empty_word), None)


def test_match():
    word_list = lexicon.scan("go north and rescue 5 princess down")

    # tests when we have a wordlist #
    assert_equal(parser.match(word_list, "verb"), ('verb', 'go'))
    assert_equal(parser.match(word_list, "direction"), ('direction', 'north'))
    assert_equal(parser.match(word_list, "stop"), ('stop', 'and'))
    assert_equal(parser.match(word_list, "error"), ('error', 'rescue'))
    assert_equal(parser.match(word_list, "number"), ('number', 5))
    assert_equal(parser.match(word_list, "noun"), ('noun', 'princess'))
    # tests when we don't have a wordlist
    assert_equal(parser.match(empty_word, "direction"), None)
    # tests when we have a wordlist but it gives us a word we don't expect
    assert_equal(parser.match(word_list, "noun"), None)


def test_skip():
    word_list = lexicon.scan("go north and rescue 5 princess down")


    # tests when we have a wordlist #

    # skip the verb from wordlist
    assert_equal(parser.skip(word_list, "verb"), None)
    # check to if indeed we skiped the verb
    assert_not_in(('verb', 'go'), word_list)

    # skip the direction from wordlist
    assert_equal(parser.skip(word_list, "direction"), None)
    # check to if indeed we skiped the direction
    assert_not_in(('direction', 'north'), word_list)

    # skip the stop from wordlist
    assert_equal(parser.skip(word_list, "stop"), None)
    # check to if indeed we skiped stop
    assert_not_in(('stop', 'and'), word_list)

    # skip the error from wordlist
    assert_equal(parser.skip(word_list, "error"), None)
    # check to if indeed we skiped the error
    assert_not_in(('error', 'rescue'), word_list)

    # skip the number from wordlist
    assert_equal(parser.skip(word_list, "number"), None)
    # check to if indeed we skiped the number
    assert_not_in(('number', 5), word_list)

    # skip the noun from wordlist
    assert_equal(parser.skip(word_list, "noun"), None)
    # check to if indeed we skiped the noun
    assert_not_in(('noun', 'princess'), word_list)


    # tests when we don't have a wordlist
    assert_equal(parser.skip(empty_word, "direction"), None)
    # tests when we have a wordlist but it gives us a word we don't expect
    assert_equal(parser.skip(word_list, "noun"), None)


def test_parse_verb():
    word_list = lexicon.scan("to go north and rescue 5 princess down")

    # tests when we have a wordlist
    assert_equal(parser.parse_verb(word_list), ('verb', 'go'))
    # tests when we have a wordlist but next word is not a verb
    assert_raises(parser.ParserError, parser.parse_verb, word_list)

    # tests when we don't have a wordlist
    assert_raises(parser.ParserError, parser.parse_verb, empty_word)


def test_parse_object():
    word_list = lexicon.scan("to north and the princess eat")

    # tests when we have a wordlist
    assert_equal(parser.parse_object(word_list), ('direction', 'north'))
    assert_equal(parser.parse_object(word_list), ('noun', 'princess'))
    # tests when we have a wordlist but next word is not a noun or direction
    assert_raises(parser.ParserError, parser.parse_object, word_list)

    # tests when we don't have a wordlist
    assert_raises(parser.ParserError, parser.parse_object, empty_word)


def test_parse_subject():
    word_list = lexicon.scan("to go north and rescue 5 princess down")

    # tests when we have a wordlist
    sentence = parser.parse_subject(word_list, ('noun', 'player'))
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'go')
    assert_equal(sentence.object, 'north')

    # tests when we don't have a wordlist
    assert_raises(parser.ParserError, parser.parse_subject, empty_word, ('noun', 'player'))


def test_parse_sentence():
    word_list = lexicon.scan("to kill the bear the princess eat Dinah down")

    # tests when we have a wordlist
    # if first non-stop word is verb
    sentence = parser.parse_sentence(word_list)
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'kill')
    assert_equal(sentence.object, 'bear')
    assert_equal(sentence.get_sentence(), 'player kill bear')

    # tests when we have a wordlist
    # if first non-stop word is noun
    sentence = parser.parse_sentence(word_list)
    assert_equal(sentence.subject, 'princess')
    assert_equal(sentence.verb, 'eat')
    assert_equal(sentence.object, 'dinah')
    assert_equal(sentence.get_sentence(), 'princess eat dinah')

    # tests when we have a wordlist but next word is neither a verb or noun
    quick_word = lexicon.scan("the north bear")
    assert_raises(parser.ParserError, parser.parse_sentence, quick_word)

    # tests when we don't have a wordlist
    assert_raises(parser.ParserError, parser.parse_sentence, empty_word)


