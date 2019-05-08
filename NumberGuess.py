"""This program is a game where the user tries to guess the sum of rolled die If the users guess is equal to the total value of the dice roll, the user wins! Otherwise, the computer wins."""

# Roll a pair of dice.
# Add the values of the roll.
# Ask the user to guess a number.
# Compare the users guess to the total value.
# Determine the winner (user or computer).

from random import randint
from time import sleep
from sys import exit

def get_dice_sides():
  sides = int(raw_input("Type number of dice sides: "))
  return(sides)

def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return(guess)
  
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  
  max_val = number_of_sides * 2
  
  print "The maximum value it could be is %d." % (max_val)
  
  guess = get_user_guess()
  
  if guess > max_val:
    print("Your guess is greater than the maximum possible value.")
  else:
    print "Rolling..."
    sleep(2)
    print "The value of the first roll is %d." % (first_roll)
    sleep(1)
    print "The value of the second roll is %d." % (second_roll)
    sleep(1)
    print "Result..."
    sleep(1)
    total_roll = first_roll + second_roll
    if guess == total_roll:
      print "You won! Congrats! You guessed the sum :D"
    else:
      print "Oh man, you lost! Sorry, but play again!"

def main_game():
  custom_sides = raw_input("Would you like to use a custom dice size? Y or N: ")
  if ((custom_sides == "Y") or (custom_sides == "y")):
    sides = get_dice_sides()
    roll_dice(sides)
  else:
    roll_dice(6)
  play_again = raw_input("Want to play again? Y or N: ")
  
  if ((play_again == "Y") or (play_again == "y")):
    replay = True
  else:
    replay = False
  while replay == True: 
  	main_game()
  print "Good-bye!"
  exit()
    
main_game()
