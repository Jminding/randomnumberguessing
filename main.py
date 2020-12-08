# Guess the number, using the random module in python
# I saw this on the assignments tab in Haiku, I decided to submit something for the first class
# This works well in the IDLE Python IDE.

from random import *

class guessARandomNumber:
    '''Represents a simple number guessing game'''

    def __init__(self):
        '''guessARandomNumber(lowerRange,upperRange) -> Random Number Guessing Game
    Takes a lower range, upper range, and generates a number between in the range
    Asks the user to guess, if the user guesses correctly, it returns that it is so
    If the user guesses incorrectly, it loops until the user guesses correctly'''
        self.lowerRange = int(input("\nWhat would you like to be the lower range of your guesses?  "))  # the lower range to guess
        self.upperRange = int(input("\nWhat would you like to be the upper range of your guesses?  "))  # the upper range to guess
        self.correctNumber = randint(self.lowerRange,self.upperRange)  # what the correct number is
        self.guessList = []  # the list of your guesses

    def playGame(self):
        '''playGame(guessARandomNumber) -> str
        str is whether the number the user inputted is correct or not'''
        while True:
            self.yourGuess = int(input("\nWhat's your guess?  "))  # Your Guess
            if self.yourGuess > self.upperRange:  # If the guess is above the maximum range
                self.guessList.append(self.yourGuess)
                print("\nYour guess was incorrect, but it was also above the maximum range you chose!  Try again!")
                elif self.yourGuess < self.lowerRange:  # If the guess is below the maximum range
                self.guessList.append(self.yourGuess)
                print("\nYour guess was incorrect, but it was also below the minimum range you chose!  Try again!")
                elif self.yourGuess != self.correctNumber:  # If the number isn't equal
                if self.yourGuess < self.correctNumber:  # If the number is lower
                    self.guessList.append(self.yourGuess)  # Make sure to append it to the list of guesses
                    print("\nOh no!  Your guess was too low.  Try again!")
                    elif self.yourGuess > self.correctNumber:  # If the number is higher
                    self.guessList.append(self.yourGuess)
                    print("\nOh no!  Your guess was too high.  Try again!")
            elif self.yourGuess == self.correctNumber:  # If the guess is correct
                self.guessList.append(self.yourGuess)
                if len(self.guessList) == 1:
                    print("\nCongratulations!  You got the number!  It was " + str(self.correctNumber) + ".  You took 1 try.  Here's the full list of your guesses:\n" + str(self.guessList) + "\nGreat job!")
                else:
                    print("\nCongratulations!  You got the number!  It was " + str(self.correctNumber) + ".  You took " + str(len(self.guessList)) + " tries.  Here's the full list of your guesses:\n" + str(self.guessList) + "\nGreat job!")
                break            
        return "\nThe correct answer was " + str(self.correctNumber) + "."


def playRandomNumberGuessingGame():
    print("Hi!  Welcome to a number guessing game.")
    print(guessARandomNumber().playGame())

playRandomNumberGuessingGame()