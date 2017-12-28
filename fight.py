#!/usr/bin/env python3

import random

def roll():
    return 1 + random.choice(range(6))

# function for getting a sorted list with a given number of rolls in it
# input: the number of rolls you want in the list
# (will be used for handling case where where # attacker rolls < 3 
#  or # defender rolls < 2)
def nrolls(n):
    liz = []
    for i in range(n):
        liz.append(roll())
    return sorted(liz, reverse=True) 

# TODO include a minimum number of armies the attacker wants to move somewhere
# and if they can no longer move that many armies there, stop attacking early
# TODO make attacker still use 3 (or as many as possible) up until "last roll"
# (probabaly whenever they could even *possibly* conquer)

def fight(attacking_armies, defending_armies, attacking_armies_to_use=3, verbose=True):
    debug = False

    if verbose:
        print('Total attacking armies is', attacking_armies)
        print('Total defending armies is', defending_armies)

    # this will stay zero if the defender wins
    attacker_must_move = 0

    # minimum to attack
    while attacking_armies > 1:
        attacker_rolls = nrolls(min(attacking_armies-1, attacking_armies_to_use))
        defender_rolls = nrolls(min(defending_armies, 2))

        if debug:
            print('attacker_rolls', attacker_rolls)
            print('defender_rolls', defender_rolls)
        
        # loop over these two loops to compare from largest to smallest
        # you can use a while loop like above, or a for loop (look up how those work)
        # HINT: loop up to the *length* of the list of the defender rolls
        # there is a function in python that finds the length of a list (look up what it is)
        
        for i in range(min(len(attacker_rolls), len(defender_rolls))):
            if attacker_rolls[i] > defender_rolls[i]:
                defending_armies = defending_armies - 1
            else:
                attacking_armies = attacking_armies - 1
        # the loops might look *like* either:
        #i = 0
        #while i < length_of_list_function(defender_rolls):
        #   ... stuff comparing attacker_rolls[i] and defender_rolls[i]
        #   i = i + 1

        # or
        #for i in range(length_of_list_function(defender_rolls)):
        #   ... stuff comparing attacker_rolls[i] and defender_rolls[i]

        if debug:    
            print('attacking_armies', attacking_armies)
            print('defending_armies', defending_armies)
        
        if defending_armies == 0:
            attacker_must_move = len(attacker_rolls)
            if verbose:
                print('ATTACKER WAS SUCCESSFUL')
                print('Attacker must move at least', attacker_must_move, 'armies')
                print('Attacker may only move', attacking_armies - 1)
            break
        
    if attacking_armies == 1:
        if verbose:
            print('DEFENDER WAS SUCCESSFUL')
            print('Defending player has', defending_armies, 'armies')

    return attacking_armies, defending_armies, attacker_must_move
    
    
# this means "if you are actually running fight.py, and not just using parts of
# fight.py (like its functions) from elsewhere"
if __name__ == '__main__':
    attacking_armies = 32
    defending_armies = 24

    attacking_armies_to_use = 3

    attacking_armies, defending_armies, attacker_must_move = \
        fight(attacking_armies, defending_armies, \
        attacking_armies_to_use=attacking_armies_to_use)


