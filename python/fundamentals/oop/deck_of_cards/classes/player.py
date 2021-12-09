class Players:
    def __init__(self):
        self.player_list = []
        self.direction =1
        self.current_idx = 0

    def add(self, player):
        print(f"{player.name} joins the game.")
        self.player_list.append(player)
    
    def get(self):
        return self.player_list
    
    def show_all(self, top_card):
        for p in self.player_list:
            p.show_hands(top_card)

    def next(self):
        idx = self.current_idx + self.direction
        size = len(self.player_list)
        if idx < 0 or idx >= size:
            idx %= size
        self.current_idx = idx
        return self.current()

    def current(self):
        return self.player_list[self.current_idx]
        


class Player:
    def __init__(self, name, is_ai = False):
        self.name = name
        self.hands = []
        self.is_ai = is_ai

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

    def show_hands(self, top_card):
        h = self.name + "> "
        for i in range(len(self.hands)):
            h += "[ ]"
        print(h)
    
    def choose_card(self, top_card):
        idx = self.tactic.choose(top_card, self.hands)
        if idx != None:
            return self.down_card(idx)
        else :
            return None

class Tactic:
    def choose(self):
        pass

class SuitFirstTactic(Tactic):
    def choose(self, top_card, hands):
        for idx, card in enumerate(hands):
            if card.is_same_suit(top_card):
                return idx
        for idx, card in enumerate(hands):
            if card.is_same_number(top_card):
                return idx
        return None

class NumberFirstTactic(Tactic):
    def choose(self, top_card, hands):
        for idx, card in enumerate(hands):
            if card.is_same_number(top_card):
                return idx
        for idx, card in enumerate(hands):
            if card.is_same_suit(top_card):
                return idx
        return None

class CardFirstTactic(Tactic):
    def choose(self, top_card, hands):
        for idx, card in enumerate(hands):
            if card.is_same_number(top_card):
                return idx
            if card.is_same_suit(top_card):
                return idx
        return None