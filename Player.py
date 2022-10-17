RANKING_FILE = 'utilities/ranking.txt'
LEVELS = ('EASY','MEDIUM','HARD') #tuple of game levels

class Player():
    """A Player who is playing hangman"""
    
    def __init__(self,MESSAGES):
        self.__score = 0
        self.name = self.__get_player_name(MESSAGES)
        self.level = self.__get_player_level(MESSAGES)
    
    #getter and setter for private var score
    def get__score(self):
        return self.__score
    def set_score(self,score):
        self.__score=score
    
    #ask user for name
    def __get_player_name(self,MESSAGES):
        name = ""
        while True:
            self.name = input(MESSAGES[4].strip()+" ")
            if len(self.name)>8:
                print(MESSAGES[5].strip()+" ")
                continue
            else:
                i = len(self.name)
                while i < 8:
                    self.name+="-"
                    i+=1
                break
        return name

    #ask user for game level
    def __get_player_level(self,MESSAGES):
        msg = MESSAGES[6].format(playername=self.name.upper())
        level = "EASY"
        while True:
            level = input(msg.strip()+" ")
            if level.upper() not in LEVELS:
                print(MESSAGES[5].strip()+" ")
                msg = MESSAGES[7].format(playername=self.name.upper())
                continue
            else:
                break
        return level

    def player_ranking():
        return " "

    def __str__():
        return " "