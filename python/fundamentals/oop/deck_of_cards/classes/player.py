
class Player:
    player_list = []
    direction = 1

    def __init__(self, name, is_ai = False):
        self.name = name
        self.hands = []
        self.is_ai = is_ai
        Player.player_list.append(self)

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

    def down_card(self, card_pos):
        card_idx = card_pos -1
        card = self.hands.pop(card_idx)
        print(f"{self.name} put down [ {card.show()} ]")
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


