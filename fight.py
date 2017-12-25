#!/usr/bin/env python

import random

def roll():
    # TODO make idiomatic later
    r = random.choice(range(6))
    return r

attacking_armies = 10
defending_armies = 9

# minimum to attack
while attacking_armies > 1:
    print sorted(list([roll(), roll(), roll()]))


