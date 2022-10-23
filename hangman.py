"""
Name: Nguyet To
Class: CS 521 - Fall 1
Date: 10-19-2022
Project: Hangman Game
Current file: hangman.py
Description of current file:
    main source code file with few functions. it will call other
    files/codes to execute the program and run the game
"""

from constants import RANKING_FILE
from constants import MESSAGE_FILE
from constants import INSTRUCTION_FILE
from Player import Player
from Game import Game


def check_letter(letter: str, game: Game, MESSAGES: list):
    """checks letter that user input in"""
    if letter.upper() in game.word:
        i = 0
        while i < len(game.word):
            if game.word[i] == letter.upper():
                game.hword[i] = letter.upper()
            i += 1
        game.letters.remove(letter.upper())
        game.streak += 1
        game.update_score()
    else:
        game.set_guess(game.get_guess()+1)
        game.letters.remove(letter.upper())
        game.streak = 0
    return game.draw_hangman(MESSAGES) and\
        game.print_word(MESSAGES)


def user_guessing(MESSAGES, game):
    """lets user start guessing letter by letter"""
    # initial print out
    game.draw_hangman(MESSAGES)
    game.print_word(MESSAGES)

    # game goes on until user win or lose
    round_continue = True
    while round_continue:

        user_input = input(MESSAGES[11].strip()+" ")
        if len(user_input) > 1 or\
                user_input.upper() not in game.letters:
            print(MESSAGES[12])
            continue
        else:
            # if True this round is ended
            round_continue = check_letter(user_input,
                                          game, MESSAGES)
        print(game.player.__str__())
        print("-------------------------------------------------")

    # ask if user want to continue another round
    while True:
        user_continue = input(MESSAGES[13].strip()+" ")
        if user_continue.upper() == 'A':
            return False
        elif user_continue.upper() == 'Q':
            return True
        elif user_continue.upper() == 'R':
            rfile = open(RANKING_FILE, 'r')
            for line in rfile.readlines():
                print(line)
            rfile.close()
        else:
            print(MESSAGES[5])


def start_game(MESSAGES: str):
    """starts game and calls other functions to perform logics"""
    player = Player(MESSAGES)
    game = Game(player)
    end_game = user_guessing(MESSAGES, game)
    return end_game


if __name__ == '__main__':
    MESSAGES = ""
    try:
        # open file contains pre-written message
        mfile = open(MESSAGE_FILE, 'r')
    except FileNotFoundError:
        print(f'Error: file not found in directory!')
    else:
        # if open sucessful, print message
        MESSAGES = mfile.readlines()
        print(MESSAGES[0])
        start_msg = MESSAGES[1]

        # prompt user for input to start game
        while True:
            instruction = input(start_msg.strip()+" ")  # expect i or s

            # open instruction file, print instruction then close it
            if (instruction.upper() == 'I'):
                try:
                    ifile = open(INSTRUCTION_FILE, 'r')
                except FileNotFoundError:
                    print(f'Error: file not found in directory!')
                else:
                    instr = ("").join(line for line in ifile.readlines())
                    print(instr)
                    ifile.close()
                    start_msg = MESSAGES[2]+MESSAGES[3]
                    continue

            # start game
            elif (instruction.upper() == 'S'):
                end_game = False
                while not end_game:
                    end_game = start_game(MESSAGES)
                mfile.close()
                break

            # invalid input from user
            else:
                print('Invalid entry, accept \'i\' or \'s\' only!')


    ## Unit test

    # Test update_score method of Game object
    test_player = Player()  # Player object
    test_player.name = "TEST_NAME"
    test_player.level = "EASY"
    test_player.set_score(0)

    test_game = Game()  # Game object
    test_game.player = test_player
    test_game.streak = 5
    test_game.update_score()
    score = test_player.get_score()
    expect = 500
    assert score == expect,\
        f"Expected score to be \"{expect}\" but got \"{score}\" instead!"

    # test get_hword method of Game object
    test_game.word = "testing"  # 7 letters
    hword = test_game.get_hword()
    expect_hword = ['-', '-', '-', '-', '-', '-', '-']  # 7 dashes
    assert hword == expect_hword,\
        f"Expected to get: \"{expect_hword}\" but got \"{hword}\" instead!"

    print("All tests run successfully, program exited!")