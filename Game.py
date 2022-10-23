"""
Name: Nguyet To
Class: CS 521 - Fall 1
Date: 10-19-2022
Project: Hangman Game
Current file: Game.py
Description of current file:
    class Game and its attributes, methods for the logic
    of the hangman game
"""

from constants import LETTERS
from constants import WORD_BANKS
from constants import INIT_DRAWING
from constants import PATTERNS
import random
import copy


class Game():
    """A hangman game and its properties"""
    game_name = "Hangman"

    def __init__(self, player=None):
        """initialize # guesses, letters to guess, word, hidden word"""
        if player != None:
            self.__guess = 0
            self.streak = 0  # consecutive correct answer
            self.player = player
            # copy of set of all uppercase letter
            self.letters = copy.deepcopy(LETTERS)
            # call private method to get random word in uppercase
            self.word = self.__get_word(player.level)
            # set hidden word with "-" based on word's length
            self.hword = self.get_hword()

    # getter and setter for private var guess
    def get_guess(self):
        """method returns number of guesses user took"""
        return self.__guess

    def set_guess(self, guess):
        """method to set number of guesses"""
        self.__guess = guess

    def __get_word(self, level: str):
        """gets random word from database based on game level"""
        word = ""
        try:
            wfile = open(WORD_BANKS[level.upper()])
        except FileNotFoundError:
            print(f'Error: file not found in directory!')
        else:
            words = wfile.readlines()
            word = words[random.randint(0, len(words)-1)]
            wfile.close()
            return word.upper().strip()

    def get_hword(self):
        """set hidden word with "-" based on word's length"""
        return list("-"*len(self.word))

    def update_score(self):
        """updates player's score"""
        current_score = self.player.get_score()
        base_score = 100
        if self.player.level == "MEDIUM":
            base_score = 200
        elif self.player.level == "HARD":
            base_score = 300
        self.player.set_score(current_score
                              + self.streak*base_score)

    def draw_hangman(self, MESSAGES: list):
        """prints out hangman based on user's guesses"""
        drawing = copy.deepcopy(INIT_DRAWING)
        num_guesses = PATTERNS.keys()
        for key in PATTERNS:
            if key <= self.__guess:
                list_i = PATTERNS.get(key)
                drawing[list_i[0]][list_i[1]] = list_i[2]
        for i in drawing:
            for j in i:
                print(j, end="")
            print("")
        print("")
        if self.__guess == 7:
            final_word = "".join(item for item in self.word).upper()
            print(MESSAGES[10].format(pname=self.player.name,
                                      pword=final_word))
            self.player.player_ranking(MESSAGES)
            return False
        return True

    def print_word(self, MESSAGES: list):
        """prints out hidden word and reference letters for user"""
        user_hword = " ".join(item for item in self.hword)
        letters_left = ["  ".join(letter for letter in
                        sorted(self.letters))]
        print("Your word to guess: " + user_hword, end="\n\n")
        print(sorted(letters_left), end="\n\n")
        if ("-" not in self.hword):
            print(MESSAGES[9].format(pname=self.player.name
                                     .upper(), num_guess=self.__guess))
            self.player.player_ranking(MESSAGES)
            return False
        return True
