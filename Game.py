class Game():
    """A hangman game and its properties"""
    game_name = "Hangman"
    def __init__(self,guess,word,hword,letters,player):
        self.guess=guess
        self.word=word
        self.hword=hword
        self.letters=letters
        self.player=player

    def get_guess(self):
        return self.guess
    def set_guess(self,guess):
        self.guess=guess

    def get_word(self):
        return self.word
    def set_word(self,word):
        self.word=word

    def get_hword(self):
        return self.hword
    def set_hword(self,hword):
        self.hword=hword

    def get_letters(self):
        return self.letters
    def set_letters(self,letters):
        self.letters=letters

    def get_player(self):
        return self.player
    def set_player(self,player):
        self.player=player