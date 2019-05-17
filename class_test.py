#!/usr/bin/python

# Import the universe, or at least what is needed
import card_functions
import blk_jak_functions

# Setting up variables from card_functions and blk_jak_functions
card_func = card_functions.card_func_vars()
blk_jak_func = blk_jak_functions.blk_jak_vars()


def print_card_func():
    """Prints the current values of card_func's variables"""
    print("Card_func")
    print(card_func.fulldeck)
    print(card_func.deck_size)
    print(card_func.player_hand)
    print(card_func.ph_total)
    print(card_func.dealer_hand)
    print(card_func.dh_total)


def print_blk_jak_func():
    """Prints the current values of blk_jak_func's variables"""
    print("blk_jak_func")
    print(blk_jak_func.count)
    print(blk_jak_func.elevens)


while True:
    # Simple code to test changes to class variables
    print_card_func()
    print_blk_jak_func()
    card_func.fulldeck.append('A')
    card_func.ph_total += 1
    blk_jak_func.count += 2
    blk_jak_func.elevens += 3
