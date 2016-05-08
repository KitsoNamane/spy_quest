#! /usr/bin/env python


class ParserError(Exception):
    pass

class Sentence(object):
    def __init__(self, subject, negates, verb, object):
        # remember we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]
        self.negates = negates

    def get_sentence(self):
        if self.negates == None:
            self.sentence = ' '.join([self.subject, self.verb, self.object])
        else:
            self.sentence = 'game over'
        return self.sentence

def peek(word_list):
    if word_list:
       word = word_list[0]
       return word[0]
    else:
       return None


def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    skip(word_list, 'stop')
    print(word_list)

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_negates(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'negatives':
        return match(word_list, 'negatives')
    else:
        return None

def parse_object(word_list):
    skip(word_list, 'stop')
    next = peek(word_list)

    if next == 'noun':
        return match(word_list, 'noun')
    elif next == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")


def parse_subject(word_list, subj):
    negate = parse_negates(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, negate, verb, obj)


def parse_sentence(word_list):
    skip(word_list, 'stop')

    start = peek(word_list)

    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'negatives':
        # assume the subject is the player then
        return parse_subject(word_list, ('noun', 'player'))
    elif start == 'verb' and len(word_list) != 0:
        # assume the subject is the player then
        return parse_subject(word_list, ('noun', 'player'))
    else:
        raise ParserError("Must start with subject, object or verb not: %s" % start)


