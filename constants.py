"""
Name: Nguyet To
Class: CS 521 - Fall 1
Date: 10-19-2022
Project: Hangman Game
Current file: constants.py
Description of current file:
    this file contains all constant variables that other files/codes
    will need to successfully run the program.
"""

import string

#constants used in hangman file
RANKING_FILE = 'utilities/ranking.txt'
MESSAGE_FILE = 'utilities/messages.txt'
INSTRUCTION_FILE = 'utilities/instruction.txt'

#constants used in Player.py
RANKING_FILE = 'utilities/ranking.txt'
LEVELS = ('EASY', 'MEDIUM', 'HARD')  # tuple

#constants used in Game's methods
LETTERS = set(letter for letter in string.ascii_uppercase)  # set

WORD_BANKS = {"EASY": "wordbank/easywords.txt",
              "MEDIUM": "wordbank/mediumwords.txt",
              "HARD": "wordbank/hardwords.txt"}

#template for drawing out hangman
INIT_DRAWING=[ 
    [" "," "," "," ","_","_","_","_","_","_","_","_","_","_"," "],
    [" "," "," "," ","|"," "," "," "," "," "," "," "," ","|"," "],
    [" "," "," "," ","|"," "," "," "," "," "," "," "," "," "," "],
    [" "," "," "," ","|"," "," "," "," "," "," "," "," "," "," "],
    [" "," "," "," ","|"," "," "," "," "," "," "," "," "," "," "],
    [" "," "," "," ","|"," "," "," "," "," "," "," "," "," "," "],
    ["_","_","_","_","|","_","_","_","_","_","_"," "," "," "," "]
    ] # list

#pattern to input to template above
PATTERNS = { 
            1:[2,13,"O"],
            2:[3,13,"|"],
            3:[4,13,"|"],
            4:[3,12,"/"],
            5:[3,14,"\\"],
            6:[5,12,"/"],
            7:[5,14,"\\"]
            } # dictionary
