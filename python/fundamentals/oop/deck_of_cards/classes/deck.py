from . import card
import random

class Deck:
    def __init__( self, is_empty = False ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        if is_empty:
            self.cards = []
        else:
            self.cards = []
            for s in suits:
                for i in range(1,14):
                    str_val = ""
                    if i == 1:
                        str_val = "Ace"
                    elif i == 11:
                        str_val = "Jack"
                    elif i == 12:
                        str_val = "Queen"
                    elif i == 13:
                        str_val = "King"
                    else:
                        str_val = str(i)
                    self.cards.append( card.Card( s , i , str_val ) )

            self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)
        return self

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    
    def add(self, card):
        self.cards.append(card)

    def get(self):
        if len(self.cards) < 1:
            return False
        else :
            return self.cards.pop()
