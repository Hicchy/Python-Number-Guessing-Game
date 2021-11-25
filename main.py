#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import *
import random
import os
from clearScreen import cls

def randomNumber():
    answer = random.choice(range(1,100))
    return answer




def numberGuess():
    continues = True
    print (logo)
    print ("Welcome to the number guessing game!")
    if input("What difficult would you like to play in? 'easy' or 'hard' ") == "easy":
        lives = 10
        print ("You have 10 attempts!")
    else:
        lives = 5
        print ("You have 5 attempts!")
    answer = random.choice(range(1,100))    
    while continues:
        print ("I'm thinking of a number")
        guess = int(input("Which number am I thinking about?"))
        if lives == 1:
            cls()
            print (lost)
            print ("That was your last attempt, you lost.")
            continues = False
        elif guess < answer:
            cls()
            print (low)
            print ("Too Low")
            lives -=1
            print (f"Attempts left: {lives}")
        elif guess > answer:
            cls()
            print (high)
            print ("Too High")
            lives -=1
            print (f"Attempts left: {lives}")
        elif guess == answer:
            cls()
            print (won)
            print ("You got it right!")
            continues = False

numberGuess()

