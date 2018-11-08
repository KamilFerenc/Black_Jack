import tkinter
import random
from blackjack import loadcardsfromdirectory


def deal_card(frame):
    # Pop the next card of the top of the desk (mixed card)
    next_card = cards.pop()
    cards.insert(0, next_card)
    # Add image to a display Label
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    # next_card[1] address of image
    # Now return the card face value
    return next_card


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    player_score = score_hand(player_hand)
    while 0 < dealer_score <= player_score:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
    if player_score > 21:
        result_text.set("Dealer wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
    else:
        result_text.set("Draw!")


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer wins!")
    return player_score


def score_hand(hand):
    # Calculate the total score off all cards in the list
    # Only one ace can have the value 11 and this will by reduce to 1 if the hand would bust
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            card_value = 11
            ace = True
        score += card_value
        if score > 21 and ace:
            score -= 10
    return score


def initial_deal():
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))

    deal_player()
    deal_player()


def new_game():
    global player_hand
    global dealer_hand
    global player_card_frame
    global dealer_card_frame

    # Clear the list
    dealer_hand.clear()
    player_hand.clear()
    # Destroy and next embedded frame to holds the dealer's cards images
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="we", rowspan=2)
    # Destroy and next embedded frame to holds the player's cards images
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="we", rowspan=2)

    # Change the result for the empty string
    result_text.set("")

    # Initialize first move of game
    initial_deal()


def shuffle_deck():
    random.shuffle(cards)


def play():
    # Initialize first move of game
    initial_deal()
    mainWindow.mainloop()


mainWindow = tkinter.Tk()
# Set upt the screen and frames for the dealer and player
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(background="green")

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)
card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=2, background="green")
card_frame.grid(row=1, column=0, sticky="we", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# Embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="we", rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# Embedded frame to hold cards images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="we", rowspan=2)

# Button
button_frame = tkinter.Frame(mainWindow, background="green")
button_frame.grid(row=3, column=0, columnspan=3, sticky="ew")
dealerButton = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealerButton.grid(row=0, column=0)
playerButton = tkinter.Button(button_frame, text="Player", command=deal_player)
playerButton.grid(row=0, column=1)
newgameButton = tkinter.Button(button_frame, text="New Game", command=new_game)
newgameButton.grid(row=0, column=2, sticky="we")
shuflleButton = tkinter.Button(button_frame, text="Shuflle Deck", command=shuffle_deck)
shuflleButton.grid(row=0, column=3, sticky="we")

# Load card
cards = loadcardsfromdirectory.load_cards()

# Create a new deck of cards and shuffle
shuffle_deck()

# Create list od dealer's and player's cards
dealer_hand = []
player_hand = []

if __name__ == "__main__":
    play()
