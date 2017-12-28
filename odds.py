#!/usr/bin/env python3

from fight import fight

def exact_attacker_odds(attacking_armies, defending_armies, \
    attacking_armies_to_use):

    return attacker_odds


def empirical_attacker_odds(attacking_armies, defending_armies, \
    attacking_armies_to_use, repeats=1000):

    attacker_wins = 0
    for i in range(repeats):
        # the '_' is a convention that means that we don't care about that
        # thing the function we are calling is returning.

        # functions can return more than one thing. you will see in fight.py
        # that it returns three things, which is why we have three things 
        # separated by commas here.

        # attacker_must_move is 0 if the defender wins, otherwise non-zero.
        _, _, attacker_must_move = fight(attacking_armies, defending_armies, \
            attacking_armies_to_use=attacking_armies_to_use, verbose=False)

        if attacker_must_move > 0:
            attacker_wins = attacker_wins + 1

    attacker_odds = attacker_wins / repeats
    return attacker_odds


def attacker_odds(attacking_armies, defending_armies, \
    attacking_armies_to_use, simulate=True):

    if simulate:
        return empirical_attacker_odds(attacking_armies, defending_armies, \
            attacking_armies_to_use)
    else:
        raise NotImplementedError('have not yet programmed exact odds calculation')


def defender_odds(attacking_armies, defending_armies, \
    attacking_armies_to_use, simulate=True):

    return 1 - attacker_odds(attacking_armies, defending_armies, \
        attacking_armies_to_use, simulate=simulate)


if __name__ == '__main__':
    attacking_armies = 32
    defending_armies = 24
    attacking_armies_to_use = 3

    attacker_odds = attacker_odds(attacking_armies, defending_armies, \
        attacking_armies_to_use)

    print('Odds of attacker winning with', attacking_armies, 'against', \
        defending_armies, 'using', attacking_armies_to_use, 'are:', \
        attacker_odds)

