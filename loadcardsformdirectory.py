import tkinter
import random


def load_cards(place_to_hold):
    """Function which load card from the directory and save the tkintre image object in the guessed list.
    The list containe tuple, each tupel is one card and store (value of card, card object)
    The card can be use in differnet program.
    Args:
        place_to_hold - """
    colours = ["club", "diamond", "heart", "spade"]
    figures = ["jack", "queen", "king"]
    for number in range(1, 11):
        for colour in colours:
            adress = "blackjack\cards\{}_{}.png".format(str(number), colour)
            image = tkinter.PhotoImage(file=adress)
            place_to_hold.append((number, image))
    for figure in figures:
        for colour in colours:
            adress = "blackjack\cards\{}_{}.png".format(figure, colour)
            image = tkinter.PhotoImage(file=adress)
            place_to_hold.append((10, image))


def shufle_card(cards):
    return random.shuffle(cards)
