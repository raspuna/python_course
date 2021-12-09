class Card:

    def __init__( self , suit , point_val , string_val ):
        
        self.suit = suit
        self.point_val = point_val
        self.string_val = string_val

    def card_info(self):
        print(f"{self.string_val} of {self.suit} : {self.point_val} points")
    
    def show(self):
        return f"{self.string_val} of {self.suit}"
    
    def is_same_suit(self, card):
        return self.suit == card.suit
    
    def is_same_number(self, card):
        return self.string_val == card.string_val
    
    def is_playable(self, card):
        return self.is_same_suit(card) or self.is_same_number(card)
