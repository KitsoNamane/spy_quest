#! /usr/bin/env python

word_dict = {}

word_dict['noun'] = "bear princess lounge Dinah security-room bedroom bodyguard cook kitchen study"
word_dict['verb'] = "go eat kill run take seduce torture strangle sneak"
word_dict['stop'] = "the in of out and to yes no"
word_dict['direction'] = "north south east west up down left right"
word_dict['stop'] = "the in of out and to"


def handle_unknown(s):
    if s.isdigit():
        return ('number', int(s))
    else:
        return ('error', s)

def scan(sentence):
    split_sentence = []
    sentence = sentence.split()
    for word in sentence:
        for key in word_dict:
            found = False

            if word in word_dict[key]:
                split_sentence.append((key, word))
                found = True
                break

        if not found:
            split_sentence.append(handle_unknown(word))

    return split_sentence


