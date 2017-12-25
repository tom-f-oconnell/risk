#!/usr/bin/env python

import random

def roll():
    r = random.choice(range(6))
    return r + 1

# TODO function for getting a sorted list with a given number of rolls in it
# input: the number of rolls you want in the list
# (will be used for handling case where where # attacker rolls < 3 
#  or # defender rolls < 2)

# TODO
# make it stop when defending armies is less than 0
# make it so it doesnt roll more die than any player has
# and choice of how many die    

attacking_armies = 10
defending_armies = 9

# TODO make this change the lengths of the list of attacker rolls
# should work for 1 and 2 as well
attacking_armies_to_use = 3

# minimum to attack
while attacking_armies > 1:
    # TODO use the function you wrote above to generate the lists of rolls here
    attacker_rolls = sorted([roll(), roll(), roll()], reverse=True)
    print(attacker_rolls)

    deffender_rolls = sorted([roll(), roll()], reverse=True)
    print(deffender_rolls)
    
    # TODO loop over these two loops to compare from largest to smallest
    # you can use a while loop like above, or a for loop (look up how those work)
    # HINT: loop up to the *length* of the list of the defender rolls
    # there is a function in python that finds the length of a list (look up what it is)
    

    # the loops might look *like* either:
    #i = 0
    #while i < length_of_list_function(defender_rolls):
    #   ... stuff comparing attacker_rolls[i] and defender_rolls[i]
    #   i = i + 1

    # or
    #for i in range(length_of_list_function(defender_rolls)):
    #   ... stuff comparing attacker_rolls[i] and defender_rolls[i]

    if attacker_rolls[0] > deffender_rolls[0]:
        defending_armies = defending_armies - 1
    else:
        attacking_armies = attacking_armies - 1
        
    if attacker_rolls[1] > deffender_rolls[1]:
        defending_armies = defending_armies - 1
    else:
        attacking_armies = attacking_armies - 1
        
    print(attacking_armies)
