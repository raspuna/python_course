
class Player:
    player_list = []
    direction = 1
    current_idx = 0

    def __init__(self, name, is_ai = False):
        self.name = name
        self.hands = []
        self.is_ai = is_ai
        Player.player_list.append(self)

    @classmethod
    def next_player(cls):
        current_idx = current_idx + direction

        
    @classmethod
    def players(cls):
        return cls.player_list
    
    @classmethod
    def show_all(cls):
        for p in cls.player_list:
            if p.is_ai:
                p.show_hands()

    def add_hand(self, card):
        card.show()
        self.hands.append(card)

    def down_card(self, card_idx):
        card = self.hands.pop(card_idx)
        print(f"{self.name} puts down [ {card.show()} ]")
        return card 

    def uno(self):
        if len(self.hands) == 1:
            print(f"{self.name} says \"Uno!!!\"")

    def win(self):
        if len(self.hands) == 0:
            print(f"{self.name} wins the game!!!!")
            return True
        else :
            return False


    def show_hands(self, top_card = None):
        cards = [self.name+"> "]
        for idx, card in enumerate(self.hands):
            if card.is_playable(top_card):
                cards.append(f"[({str(idx+1).rjust(2)}) {card.show()}]")
            else:
                cards.append(f"[(  ) {card.show()}]")
        
        string = '\n'.join(cards) 
        print(string)

        
class AI(Player):
    def __init__(self, name, tactic):
        super().__init__(name, True)
        self.tactic = tactic

    def show_hands(self):
        h = self.name + "> "
        for i in range(len(self.hands)):
            h += "[ ]"
        print(h)
    
    def choose_card(self, top_card):
        if self.tactic == 0:
            for idx, card in enumerate(self.hands):
                if card.is_same_suit(top_card):
                    return self.down_card(idx)
            for idx, card in enumerate(self.hands):
                if card.is_same_number(top_card):
                    return self.down_card(idx)
        elif self.tactic == 1:
            for idx, card in enumerate(self.hands):
                if card.is_same_number(top_card):
                    return self.down_card(idx)
            for idx, card in enumerate(self.hands):
                if card.is_same_suit(top_card):
                    return self.down_card(idx)
        elif self.tactic == 2:
            for idx, card in enumerate(self.hands):
                if card.is_same_number(top_card):
                    return self.down_card(idx)
                if card.is_same_suit(top_card):
                    return self.down_card(idx)
        return None


