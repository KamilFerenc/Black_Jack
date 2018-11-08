import tkinter


def load_cards():
    """Function which load card from the directory and save the tkinter image object in the guessed list.
    The list contain tuple, each tuple is one card and store (value of card, card object)
    The card can be use in different program.
    """

    colours = ["club", "diamond", "heart", "spade"]
    figures = ["jack", "queen", "king"]
    cards = []
    for number in range(1, 11):
        for colour in colours:
            address = "/home/kamil/PycharmProjects/blackjack/cards/{}_{}.png".format(str(number), colour)
            image = tkinter.PhotoImage(file=address)
            cards.append((number, image))
    for figure in figures:
        for colour in colours:
            address = "/home/kamil/PycharmProjects/blackjack/cards/{}_{}.png".format(figure, colour)
            image = tkinter.PhotoImage(file=address)
            cards.append((10, image))
    return cards
