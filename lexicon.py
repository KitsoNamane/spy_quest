#! /usr/bin/env python

word_dict = {}

word_dict['noun'] = {'bear', 'princess', 'her', 'him', 'lounge', 'dinah', 'security-room',
                     'bedroom', 'bodyguard', 'cook', 'kitchen', 'study', 'game'}
word_dict['verb'] = {'go', 'eat', 'kill', 'run', 'take', 'seduce', 'torture',
                     'strangle', 'sneak', 'start'}
word_dict['stop'] = {'the', 'in', 'of', 'out', 'and', 'to', 'yes', 'no'}
word_dict['direction'] = {'north', 'south', 'east', 'west', 'up', 'down',
                          'left', 'right'}
word_dict['negatives'] = {'not', 'dont', "don't"}


def handle_unknown(s):
    if s.isdigit():
        return ('number', int(s))
    else:
        return ('error', s)

def scan(sentence):
    sentence = sentence.lower()
    split_sentence = []
    sentence = sentence.split()
    for word in sentence:
        # this for-loop is implemented using advice from Raymond Hittenger
        for key in word_dict:
            if word in word_dict[key]:
                split_sentence.append((key, word))
                break
        else:
            split_sentence.append(handle_unknown(word))

    return split_sentence


