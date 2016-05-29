#! /usr/bin/python
# -*- coding: utf-8 -*-
from random import randint
import parser
import lexicon

# generic endings
class Endings(object):

    def __init__(self):
        self.quips = ["mission over...obviously you're not good enough",
                      "Your mum would be proud...If she were smarter",
                      "Such a looser",
                      "I have a small puppy that's better at this",
                      "so saaad",
                      ]

    def random_death(self):
        return self.quips[randint(0, len(self.quips)-1)]


# handles all game components
class Engine(object):
    def __init__(self):
        self.paths = {}
        self.action_paths = {}

    def add_paths(self, paths):
        self.paths.update(paths)

    def add_action_paths(self, action):
        self.action_paths.update(action)

    def process_input(self, user_input):
        action = lexicon.scan(user_input)
        print(action)
        return parser.parse_sentence(action)

    def get_scene(self, get_path):
        return self.paths.get(get_path, None)

    def handle_scene(self, user_input):
        user_input = user_input.strip()
        if " " not in user_input:
            get_path  = self.action_paths.get(user_input, "game over")
            return get_path
        else:
            action = self.process_input(user_input)
            get_path  = self.action_paths.get(action.get_sentence(), "game over")
            return get_path

# base class for all scenes
class Scene(object):

    def __init__(self, name, description):
        self.legal_paths = {}
        self.name = name
        self.description = description


# load game data

the_pit = Scene('the pit',
"""
MISSION BRIEFING:
hello agent T-19, this is Diana, we're in need of your skills!

    *infiltrate the webster Mansion.
    *find and secure a disk (ATLANTIS-virus)

    they have a social function tonight i'v prepared a cover for you

our client would like this to be as clean as possible so don't leave a mess!,
we don't RIO all over again do we...see you soon!!!

    tools: lock-pick, flash-drive, tight-rope...

you arrive with your envoy at the main entrance but the door is only as far as
you can go...


choose your cover???
"""
)


the_front_door = Scene('the front door',
"""
you arrive as the body-guard of Mr Del Piero, but you can only go as far as the
main entrace of the mansion...


what's the plan???
"""
)

the_kitchen = Scene('the kitchen',
"""
with this disguise you sneak in the kitchen...steam soaring, stove hissing and
everybody passing around, they hardly notice you at all...you go about
inspecting each and every corner of the room you then notice familiar room,
the cold room! suddenly you get an idea...

a few minutes later you emerge out og the cold room as Josh, the a waiter!
just then the head Chef takes a load on you, pointing and telling you where you
should be, he then gives you an order, its for a VIP at the master bedroom


are you going to take it?
"""
)

the_lounge = Scene('the lounge',
"""
you pose as a steward, with special interest at the main table you serve them
wine, listening in to their conversation one thing that caught your attention:

    Webster: (with a cigar in his hand) I'm telling you she is a beauty, I took
             her for a runthe other day...it was fenominal
    Cage: (hahaha..) that's what you said about Dinah...now look at what trouble
          she's gotten you into...(all laughing)

deep in your thoughts:
{find Dinah, she must know one or two of his secrets}
you then go to the elevator...there is a guard there:

    Guard: hey you cant go up there..
    You: Oh special order for Mrs Webster..
    Guard: which Mrs Webster?
    You: the, boss's escort, look i don't get paid a lot and i need this job so
         unless you want both of us loosing our jobs!
    Guard: oh we don't want that do we, go on.

you are now in the elevator,
check time: 2105hrs
hm!!! not bad but time is running out.


where do you want to go now???
"""
)

the_study = Scene('the study',
"""
you are in the study, no one is there, you start to look around hoping to get
lucky...you first look in the drawers, you find nothing interesting except a
small speck of shine under some documents...its the key to the Farrari...you
take it and start to look around again, then you soon notice an old mural...
it proves to had hidden some secrets, its the safe it appears to have an old
combination lock about 3 digits
"""
)

the_bedroom = Scene('the bedroom',
"""
you enter the rooom, its candle lit, music playing softly in the background
and rose petals everywhere. You find Dinah on the bed waiting for you!!!


how are you going to get her to talk?!?
"""
)

the_security_room = Scene('the security-room', """
you enter security room to cover your tracks, there is no one here so the
computer is all yours fornow...Hurry!!!
"""
)

generic_end = Scene('game over', Endings().random_death())

the_end_winner = Scene('the end winner',
"""
yes you have the keys of the Ferrari now get outa here before they find you...
""")


the_end_looser = Scene('the end',
"""
you don't have the keys...you go back to find them only for you to get caught
the first instance you step inside the mansion...you are on you own!!!
"""
)

# load the game engine with scenes
game_engine = Engine()
game_engine.add_paths({
'the pit': the_pit,
'kitchen': the_kitchen,
'the front door': the_front_door,
'kitchen': the_kitchen,
'bedroom': the_bedroom,
'lounge': the_lounge,
'security-room':the_security_room,
'study': the_study,
'game over': generic_end,
'winner': the_end_winner,
'loose': the_end_looser})

# load legal paths of each scene
the_pit.legal_paths = ['kitchen', 'the front door', 'game over']
the_kitchen.legal_paths = ['bedroom', 'lounge']
the_front_door.legal_paths = ['kitchen', 'game over']
the_bedroom.legal_paths = ['study', 'game over']
the_lounge.legal_paths = ['study', 'bedroom']
the_security_room.legal_paths = ['game over', 'winner', 'loose']
the_study.legal_paths = ['security-room', 'game over']

# load the game engine with valid actions
game_engine.add_action_paths({
'cook': 'kitchen',
'bodyguard': 'the front door',
'player sneak back': 'kitchen',
'player go kitchen': 'kitchen',
'yes': 'bedroom',
'study': 'study',
'bedroom': 'bedroom',
'no': 'lounge',
'player torture her': 'study',
'player seduce her': 'study',
'678': 'security-room',
'ghostWarrior': 'winner'})
