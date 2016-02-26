#! /usr/bin/env python

word_dict = {}

word_dict['nouns'] = []
word_dict['verbs'] = []
word_dict['stops'] = []
word_dict['directions'] = []
word_dict['numbers'] = []


def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(sentence):
    split_sentence = []
    for word in sentence:
        for key in word_dict:
            if convert_numbers(word):
                split_sentence.append((key, convert_numbers(word)))
            if word in word_dict[key]:
                split_sentence.append((key, word_dict[key]))
            else:
                split_sentence.append(('error', word))
    return split_sentence

