#!/usr/bin/env python3

import random
import math

# TODO load from risk-graph
#COUNTRIES = 
CARDS = {'horse', 'cannon', 'soldier'}
COLORS = {'red', 'black', 'green', 'pink', 'yellow', 'blue'}

# TODO define static method / function for Player calculating # of armies they can place

class Player:
    def __init__(self, board, color):
        self.color = color
        # players start with no cards, so an empty set
        self.cards = set()
        # maybe don't want this
        self.countries_controlled = dict()


class Risk:
    def __init__(self, num_players=3):
        """
        Initializes a Risk 'object'. Sets of the board for a given # of players.
        """
        if num_players < 2:
            print('Too few players. Need at least 2.')
        elif num_players > len(COLORS):
            print('Too many players. Only', len(COLORS), 'colors available.')

        # to keep track of number of armies in each country
        # and which color player owns them
        self.board = dict()

        # will pick num_players colors from COLORS, WITHOUT REPLACEMENT
        player_colors = random.sample(COLORS, num_players)
        self.players = []
        for color in player_colors:
            # make a new Player 'object' with the randomly chosen color
            # and given them a *reference* to the same board everyone uses
            self.players.append(Player(board, color))

        country_list = list(COUNTRIES)
        # this makes the order of the items in country_list random
        random.shuffle(country_list)

        # some players may get less. the number of cards (countries) available
        # may not evenly divide into the number of players.
        countries_per_player = int(math.ceil(len(COUNTRIES) / num_players))

        for i in range(num_players):
            # TODO check this is actually the right number of countries / no errors
            player_countries = country_list[i*countries_per_player:\
                (i+1)*countries_per_player]

            p = self.players[i]
            for c in player_countries:
                # players start with 1 army in each country
                self.board[c] = [p.color, 1]


if __name__ == '__main__':
    r = Risk()
