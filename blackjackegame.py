import tkinter
from blackjack import loadcardsformdirectory


class BlackJackWindow:



    def __init__(self, geometry="640x480", title="Black Jack", text="Hand is on."):
        self.cards = []
        self.window = tkinter.Tk()
        self.window.geometry(geometry)
        self.window.title(title)
        self.window.configure(background="lightblue")
        loadcardsformdirectory.load_cards(self.cards)

        self.result_label = tkinter.Label(self.window, background="grey", text=text)
        self.result_label.grid(row=0, column=0, columnspan=2, sticky="we")
        self.score_frame = tkinter.Frame(self.window, relief="sunken")
        self.score_frame.grid(row=1, column=0, sticky="nw")

        self.label_player = tkinter.Label(self.score_frame, text="Player")
        self.label_player.grid(row=2, column=0, sticky="nw")
        self.player_points = tkinter.IntVar()
        self.player_points.set(self.calculate_player_points())
        self.lable_player_points = tkinter.Label(self.score_frame, textvariable=self.player_points)
        self.lable_player_points.grid(row=3, column=0)

        self.dealer_card_frame = tkinter.Frame(self.window)
        self.dealer_card_frame.grid(row=1, column=0)
        self.label_dealer = tkinter.Label(self.dealer_card_frame, text="Dealer")
        self.label_dealer.grid(row=0, column=0)
        self.dealer_points = tkinter.IntVar()
        self.dealer_points.set(self.calculate_dealer_points())
        self.lable_dealer_points = tkinter.Label(self.dealer_card_frame, textvariable=self.dealer_points)
        self.lable_dealer_points.grid(row=1, column=0)
        self.dealer_card_lable = tkinter.Label(self.dealer_card_frame, image=self.cards[1][1])
        self.dealer_card_lable.grid(row=0, column=1, rowspan=2)

        self.player_card_frame = tkinter.Frame(self.window)
        self.player_card_frame.grid(row=2, column=0)
        self.label_player = tkinter.Label(self.player_card_frame, text="Player")
        self.label_player.grid(row=2, column=0)
        self.player_points = tkinter.IntVar()
        self.player_points.set(self.calculate_player_points())
        self.lable_player_points = tkinter.Label(self.player_card_frame, textvariable=self.player_points)
        self.lable_player_points.grid(row=3, column=0)
        self.player_card_label = tkinter.Label(self.player_card_frame, image=self.cards[1][1])
        self.player_card_label.grid(row=0, column=1, rowspan=2)
        self.window.mainloop()

    def calculate_dealer_points(self):
        return 1
    def calculate_player_points(self):
        return 0

blackjack = BlackJackWindow()
