from Player import Player
from Game import Game

MESSAGE_FILE = 'utilities/messages.txt'
INSTRUCTION_FILE = 'utilities/instruction.txt'

def check_letter(letter:str,game:Game,MESSAGES:list):
    """checks letter that user input in"""
    if letter.upper() in game.word:
        i = 0
        while i < len(game.word):
            if game.word[i] == letter.upper():
                game.hword[i] = letter.upper()
            i+=1      
        game.letters.remove(letter.upper())
    else:
        game.set_guess(game.get_guess()+1)
        game.letters.remove(letter.upper())

    return game.draw_hangman(MESSAGES) and\
            game.print_word(MESSAGES)

def user_guessing(MESSAGES,game):
    """lets user start guessing letter by letter"""

    #initial print out
    game.draw_hangman(MESSAGES) 
    game.print_word(MESSAGES)
    
    #game goes on until user win or lose
    round_continue = True
    while round_continue:
        
        user_input = input(MESSAGES[11].strip()+" ")
        if len(user_input)>1 or\
            user_input.upper() not in game.letters:
            print(MESSAGES[12])
            continue
        else:
            #if True this round is ended
            round_continue = check_letter(user_input,\
                                game,MESSAGES)
        print("-------------------------------------------------")
    
    #ask if user want to continue another round
    while True:
        user_continue = input(MESSAGES[13]) # expect 'y' or 'n'
        if user_continue.upper()=='Y':
            return False
        elif user_continue.upper()=='N':
            return True
        else:
            print(MESSAGES[5])

def start_game(MESSAGES:str):
    """starts game and calls other functions to perform logics"""
    player = Player(MESSAGES)
    game = Game(player)
    end_game=user_guessing(MESSAGES,game)
    return end_game

if __name__ == '__main__':
    try:
        #open file contains pre-written message
        mfile = open(MESSAGE_FILE,'r')
    except FileNotFoundError:
        print(f'Error: file not found in directory!')
    else:
        #if open sucessful, print message 
        MESSAGES = mfile.readlines()
        print(MESSAGES[0])
        start_msg = MESSAGES[1]
        
        #prompt user for input to start game
        while True:
            instruction = input(start_msg.strip()+" ") #expect y or n 
            
            #open instruction file, print instruction then close it
            if(instruction.upper()=='Y'):
                try:
                    ifile = open(INSTRUCTION_FILE,'r')
                except FileNotFoundError:
                    print(f'Error: file not found in directory!')
                else:
                    instr = ("").join(line for line in ifile.readlines())
                    print(instr)
                    ifile.close()
                    start_msg = MESSAGES[2]+MESSAGES[3]
                    continue
            
            #start game
            elif(instruction.upper() == 'N'):
                end_game = False
                while not end_game:
                    end_game = start_game(MESSAGES)
                mfile.close()
                break
            
            #invalid input from user
            else:
                print('Invalid entry, accept \'y\' or \'n\' only!')