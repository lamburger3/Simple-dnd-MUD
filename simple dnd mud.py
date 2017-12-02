import random
import time

class Character:
  name = ""

  STR = 0
  DEX = 0
  CON = 0
  INT = 0
  WIS = 0
  CHA = 0

  def __init__(self, name):
    print("Then your legend will be the legend of " + name + ", Level 1 Fighter!")
    self.name = name

  def print_stats(self):
    print("{0}'s STR is {1}".format(self.name, self.STR))
    print("{0}'s DEX is {1}".format(self.name, self.DEX))
    print("{0}'s CON is {1}".format(self.name, self.CON))
    print("{0}'s INT is {1}".format(self.name, self.INT))
    print("{0}'s WIS is {1}".format(self.name, self.WIS))
    print("{0}'s CHA is {1}".format(self.name, self.CHA))

'''
Function to name the character.
'''
def player_name_input():
    name = raw_input("What's your name? ")
    return name

'''
Roll 4 6-sided dice, drops the lowest one, and returns the sum.
''' 
def roll_stat():
    die_rolls = []
    for x in range(0, 4):
    #Roll 4 dice, and append them to a list
        die_rolls.append(random.randint(1,6))

   #Sort the values
    die_rolls = sorted(die_rolls)

    #This is sorted in ascending order, so if we want to drop the lowest value, we ignore the first value
    die_rolls_drop_lowest = die_rolls[1:]

    #Return the sum
    return sum(die_rolls_drop_lowest)

'''
Sets the value for the 6 DND stats, and then prints them.
'''
def set_stats_for_character(character):
    character.STR = roll_stat()
    character.DEX = roll_stat()
    character.CON = roll_stat()
    character.INT = roll_stat()
    character.WIS = roll_stat()
    character.CHA = roll_stat()

    character.print_stats()

'''
Function set to print the "story" and display the users choices
''' 
def story_one():
    print("You stand in front of a door forged of pure black steel. The possibility of whatcould be behind such a form tempts you to enter it.")
    print("What will you do?")
    print("1. Go to town.")
    print("2. Enter through the door.")

'''
Function to handle user input.
'''
def story_input():
    #This handles a user not inputting a valid integer. Like entering a string for example
    while True:
      choice = input("")

      if choice == 1:
          print("You decide it's best to go back to town, and head home.")
          return
      elif choice == 2:
          goblin_exists = 1
          print("You encounter a sickly green, small figure. It's a goblin!")
          return
      #This recalls the input function if a user breaks the input system with invalid input
      else:
          print("That's not a valid option.")
          print("Please try again.")
          story_one()

def start_story():
  story_one()
  story_input()

def create_hero():
  player_name = player_name_input()
  hero = Character(player_name)
  set_stats_for_character(hero)

def main():
  create_hero()
  start_story()

if __name__ == "__main__":
  main()