import random

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



