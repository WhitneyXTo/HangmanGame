from constants import LETTERS
from constants import WORD_BANKS
from constants import INIT_DRAWING
from constants import PATTERNS
import random
import copy

class Game():
    """A hangman game and its properties"""
    game_name = "Hangman"
    def __init__(self,player):
        self.__guess=0
        self.player=player
        self.letters=copy.deepcopy(LETTERS)
        self.word = self.__get_word(player.level)
        print(self.word)
        self.hword = self.__get_hword()

    def get_guess(self):
        return self.__guess
    def set_guess(self,guess):
        self.__guess=guess

    def __get_word(self,level:str):
        """gets random word from database based on game level"""
        word = ""
        try:
            wfile = open(WORD_BANKS[level.upper()])
        except FileNotFoundError:
            print(f'Error: file not found in directory!')
        else:
            words = wfile.readlines()
            word = words[random.randint(0,len(words)-1)]
            wfile.close()  
            return word.strip()
    
    def __get_hword(self):
        return list("-"*len(self.word))
    
    def draw_hangman(self,MESSAGES:list):
        """prints out hangman based on user's guesses"""
        drawing = copy.deepcopy(INIT_DRAWING)
        num_guesses =  PATTERNS.keys()
        for key in PATTERNS:
            if key <= self.__guess:
                list_i = PATTERNS.get(key)
                drawing[list_i[0]][list_i[1]]=list_i[2]
        for i in drawing:
            for j in i:
                print(j,end="")
            print("")
        print("")
        if self.__guess == 7:
            final_word = "".join(item for item in self.word).upper()
            print(MESSAGES[10].format(pname=self.player.name,\
                                    pword = final_word))
            self.player.set_score(0)                  
            return False
        return True
    
    def print_word(self,MESSAGES:list):
        """prints out hidden word and reference letters for user"""
        user_hword = " ".join(item for item in self.hword)
        letters_left = ["  ".join(letter for letter in\
                        sorted(self.letters))]
        print("Your word to guess: " + user_hword,end="\n\n")
        print(sorted(letters_left), end="\n\n")
        if("-" not in self.hword):
            print(MESSAGES[9].format(pname=self.player.name\
                                    .upper(),num_guess=self.__guess))
            return False
        return True
    