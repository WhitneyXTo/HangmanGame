import string

#constants used in hangman file
RANKING_FILE = 'utilities/ranking.txt'
MESSAGE_FILE = 'utilities/messages.txt'
INSTRUCTION_FILE = 'utilities/instruction.txt'

#constants used in Player.py
RANKING_FILE = 'utilities/ranking.txt'
LEVELS = ('EASY','MEDIUM','HARD') #tuple of game levels

#constants used in Game's methods
LETTERS = set(letter for letter in string.ascii_uppercase)

WORD_BANKS = {"EASY":"wordbank/easywords.txt",
                    "MEDIUM":"wordbank/mediumwords.txt",
                    "HARD":"wordbank/hardwords.txt"}

INIT_DRAWING=[
            [" "," "," "," ","_","_","_","_","_","_","_","_","_","_"," "],
            [" "," "," "," ","|"," "," "," "," "," "," "," "," ","|"," "],
            [" "," "," "," ","|"," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," ","|"," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," ","|"," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," ","|"," "," "," "," "," "," "," "," "," "," "],
            ["_","_","_","_","|","_","_","_","_","_","_"," "," "," "," "]
            ]

PATTERNS = { 
            1:[2,13,"O"],
            2:[3,13,"|"],
            3:[4,13,"|"],
            4:[3,12,"/"],
            5:[3,14,"\\"],
            6:[5,12,"/"],
            7:[5,14,"\\"]
            }
