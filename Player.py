from constants import RANKING_FILE
from constants import LEVELS

class Player():
    """A Player who is playing hangman"""
    
    def __init__(self,MESSAGES):
        """initalize Player's properties"""
        self.__score = 0
        self.name = self.__get_player_name(MESSAGES)
        self.level = self.__get_player_level(MESSAGES)
    
    #getter and setter for private var score
    def get_score(self):
        """getter for score"""
        return self.__score
    def set_score(self,score):
        """setter for score"""
        self.__score=score
    
    #ask user for name
    def __get_player_name(self,MESSAGES):
        """returns player's name from asking user"""
        name = ""
        while True:
            name = input(MESSAGES[4].strip()+" ")
            if len(name)>8:
                print(MESSAGES[5].strip()+" ")
                continue
            else:
                break
        return name.upper()

    #ask user for game level
    def __get_player_level(self,MESSAGES):
        """returns player's level from asking user"""
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
        i = len(level)
        return level.upper()

    def __format_string(self,string,length):
        """fills string up to certain length with space"""
        i = len(string)
        while i < length:
            string += " "
            i += 1
        return string

    def player_ranking(self,MESSAGES):
        """checks and records player's score to ranking board"""
        try:
            rfile = open(RANKING_FILE,'r+')
        except FileNotFoundError:
            print(f'Error: file not found in directory!')
        else:
            ranking_info =  list(rfile.readlines())
            previous_highs = []
            if (len(ranking_info)==2):
                player_str = MESSAGES[16].format(\
                            prank = 1,\
                            pname = self.__format_string(self.name,8),\
                            plevel = self.__format_string(self.level,8),\
                            pscore = self.__score)
                rfile.write("\n")
                rfile.write(player_str)
            elif (len(ranking_info)>2):
                i = 2
                while i < len(ranking_info):
                    previous_highs.append((",".join(ranking_info[i].split()))\
                                            .split(","))
                    i += 1
                previous_scores = [int(item[3]) for item in previous_highs]     
                
                i = 0 #index for previous scores list
                while i < len(previous_scores):
                    if self.__score >= previous_scores[i]:
                        previous_highs.insert(i,[1,self.name,self.level,self.__score])
                        break
                    i += 1
                rfile.truncate(0)
                rfile.seek(0)
                rfile.write(MESSAGES[14])
                rfile.write(MESSAGES[15])
                j = 0
                while j < len(previous_highs):
                    previous_highs[j][0] = j+1
                    name = self.__format_string(previous_highs[j][1],8)
                    level = self.__format_string(previous_highs[j][2],6)
                    player_str = MESSAGES[16].format(\
                            prank=previous_highs[j][0],\
                            pname=name,\
                            plevel=level,\
                            pscore=previous_highs[j][3])
                    rfile.write(player_str)
                    j += 1
                    if j == 10:
                        break
            rfile.close()

    def __str__(self):
        return f"{self.name}'s current score is {self.__score}"
    
    def __copy__(self,MESSAGES):
        new_player = Player(MESSAGES)
        new_player.name = self.name
        new_player.level = self.level
        new_player.set_score(self.get__score)
        return new_player