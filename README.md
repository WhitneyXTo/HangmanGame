# HangmanGame
### Author: Whitney To
### Date: 10-18-2022
### Project: python program for 'hangman' game

## HERE IS THE PROGRAM STRUCTURE AND HOW TO RUN IT

To run the program on MAC OS: (run the hangman.py file)

    1. Open a terminal window at the directory with all file listed below
    2. Type in command 'python3 hangman.py'
    3. Follow the prompts appear once the program runs and have fun!
    4. When program first starts, you can select 'i' for instruction for more game's details
    4. If want to exit in middle of game, please use 'control+C' on keyboard

All source code files and utilities files/folders are included in
    this file called 'hangmangame'. They include:
    
    1. utlitily file:

        1.1 instruction.txt
            This file will be read and presented if the user who
            is playing the game need instruction

        1.2 messages.txt
            This file contains pre-written messages that the source
            files will import and use. 
            This is for the code to be more readable

        1.3 ranking.txt
            Game score will be recorded each round and sorted in order. File only contains upto 10 game rounds.
    
    2. wordbank file:

        The files below contains list of words with different lenths
        associate to different game level (easy,medium,hard). One word will be selected randomly by the program after user choose a game level.
        
        2.1 easywords.txt
        2.2 mediumwords.txt
        2.3 hardwords.txt
    
    3. constant.py
        
        This python file contains all the constant variables that will be used through out the program. Purpose of having a separate file for all constant is for better readability in source codes, better usability and maintainabity when modification has to be made.

    4. Player.py
        This python file is a Player class with attributes of player's name, player's game level, and player's score on the game. The Player class has methods to
            
            4.1 get/set private variable 'score'
            4.2 prompt user to enter player's name
            4.3 prompt user to enter game level 
            4.4 check player's score and ranking 
            4.5 modify and return a string input
            4.6 return a string infomation (__str__)
            4.7 return a copy of current Player object (__copy__)

    5. Game.py
        This python file is a Game class with attributes of number of guesses, correct guess streak, available letters, word to guess, hidden word to show user and a player object. The Game class has methods to
            
            5.1. get/set private variable 'guess'
            5.2 get word and hidden word
            5.3 update score
            5.4 draw hangman based on guesses
            5.5 print out letter guessed


    6. hangman.py
        This is the main source code file to be run to start the game.
        File contains code logic and few functions to call upon other codes/files to sucessfully execute the game.
        Main code will call 'start_game' function to start game. This function will call 'user_guessing' function to get user's input letter, which will be checked for validation with 'check_letter' function.