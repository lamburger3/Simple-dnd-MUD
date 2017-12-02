import random
import time
#Player_Name_Input will be the function to name the character
def player_name_input():
    name = raw_input("What's your name? ")
    print("Then your legend will be the legend of " + name + ", Level 1 Fighter!")
player_name_input()

    
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

def set_stats():
    STR = roll_stat()
    DEX = roll_stat()
    CON = roll_stat()
    INT = roll_stat()
    WIS = roll_stat()
    CHA = roll_stat()
    print("Your STR is " + str(STR))
    print("Your DEX is " + str(DEX))
    print("Your CON is " + str(CON)) 
    print("Your INT is " + str(INT))
    print("Your WIS is " + str(WIS))
    print("Your CHA is " + str(CHA))
set_stats()
#Function set to print the "story" and display the users choices
def story_one():
    print("You stand in front of a door forged of pure black steel. The possibility of whatcould be behind such a form tempts you to enter it.")
    print("What will you do?")
    print("1. Go to town.")
    print("2. Enter through the door.")
#New function to handle user input
def story_input():
    #This handles a user not inputting a valid integer. Like entering a string for example
    while True:
        try:
            choice = input("")
            break
        except:
            print("That's not a valid option.")
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
        print("1. Go to town.")
        print("2. Enter through the door.")
        story_input()
story_one()
story_input()


        
        
    
    




