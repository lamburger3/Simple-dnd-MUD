import random

#Player_Name_Input will be the function to name the character
def player_name_input():
    name = raw_input("What's your name? ")
    print("Then your legend will be the legend of " + name + ", Level 1 Fighter!")
player_name_input()

def player_stat_generation():
    sum_of_dice_rolls = 0
   
#Stats are then calculated with a for loop, rolling 4 six-sided die each stat
#For loop will not randomize and sum up four times each, which was the main goal
#Instead, it will by calculated by a single roll of a 20 sided die for now
    for x in xrange(0,4):
        STR = sum_of_dice_rolls + random.randint(1, 20)
        DEX = sum_of_dice_rolls + random.randint(1, 20)
        CON = sum_of_dice_rolls + random.randint(1, 20)
        INT = sum_of_dice_rolls + random.randint(1, 20)
        WIS = sum_of_dice_rolls + random.randint(1, 20)
        CHA = sum_of_dice_rolls + random.randint(1, 20)
#Results will then be printed
    print("Your STR is " + str(STR))
    print("Your DEX is " + str(DEX))
    print("Your CON is " + str(CON)) 
    print("Your INT is " + str(INT))
    print("Your WIS is " + str(WIS))
    print("Your CHA is " + str(CHA))
player_stat_generation()
