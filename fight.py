#!/usr/bin/env python

import random

def roll():
    # TODO make idiomatic later
    r = random.choice(range(6))
    return r + 1

#TODO make it stop when defending armies is less than 0, make it so it doesnt
# rol more die than any player has , and choice of how many die    
attacking_armies = 10
defending_armies = 9

# minimum to attack
while attacking_armies > 1:
    attacker_rolls = sorted([roll(), roll(), roll()], reverse=True)
    print(attacker_rolls)

    deffender_rolls = sorted([roll(), roll()], reverse=True)
    print(deffender_rolls)
    
    if attacker_rolls[0] > deffender_rolls[0]:
        defending_armies = defending_armies - 1
    else:
        attacking_armies = attacking_armies - 1
        
    if attacker_rolls[1] > deffender_rolls[1]:
        defending_armies = defending_armies - 1
    else:
        attacking_armies = attacking_armies - 1
        
    print(attacking_armies)