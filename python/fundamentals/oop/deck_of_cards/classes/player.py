
class Player:
    def __init__(self, name, is_ai = False):
        self.name = name
        self.hands = []
        self.is_ai = is_ai

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


    def show_hands(self):
        if self.is_ai:
            self.show_hands_secret()
            return
        cards = []
        for idx, card in enumerate(self.hands):
            cards.append(f"[({idx+1}) {card.show()}]")
        
        string = ' '.join(cards) 
        print(string)

    def show_hands_secret(self):
        h = self.name + ">"
        for i in range(len(self.hands)):
            h += "[ ]"
        print(h)
