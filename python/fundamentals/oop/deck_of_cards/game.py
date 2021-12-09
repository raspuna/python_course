from classes.deck import Deck
from classes.player import Player, AI
import random
import re

top_card = None
dummy = None
deck = None

def initialize_game(player_list):
    global deck 
    deck = Deck()
    for i in range(7):
        for p in player_list:
            card = deck.cards.pop()
            p.add_hand(card)

def draw():
    global deck
    card = deck.get()
    if not card:
        card = replace()
    return card 

def replace():
    global deck, dummy
    print("The deck is empty! Reshuffle dummy")
    deck = dummy.shuffle()
    return deck.get()

def play_card(player, card):
    global dummy, top_card
    top_card = card
    dummy.add(card)
    player.uno()
    return player.win()

def do_AI(npc):
    global top_card
    global deck, dummy

    # search suit first
    for idx, card in enumerate(npc.hands):
        if card.is_same_suit(top_card):
            return play_card(npc, npc.down_card(idx+1))
    
    for idx, card in enumerate(npc.hands):
        if card.is_same_number(top_card):
            return play_card(npc, npc.down_card(idx+1))

    npc.add_hand(draw())
    print(f"{npc.name} draws.")
    return False



def print_option():
    print ("option=============")
    print("[number] : let a card [number] down ")
    print("u: say Uno")
    print("d: draw a card from deck")
    print("q: quit the game")
    print("n: new game start")
    print("t: show top card again")
    print("s: show my hands")
    print("h: show option")
    print("="*15)

if __name__ == "__main__":

    user_name = str(input("Please let us know your name:   "))
    player = Player(user_name)
    npc1 = AI("Anna", 0)
    npc2 = AI("Elsa", 1)
    npc3 = AI("Sven", 2) 

    print(f"Welcome, {user_name}!")

    initialize_game(Player.players())
    print_option()
    p = re.compile("(^[udqnsht]$)|(^[0-9]+$)")
    # for debugging
    Player.show_all()

    top_card = deck.get()
    dummy = Deck(is_empty = True)
    dummy.add(top_card)

    Game = True
    while Game:

        player.show_hands(top_card)
        print("")
        print("top >>", top_card.show())
        print("")
        
        i = input("What will you do next?")
        matched = p.match(i)
        if not matched:
            print("Wrong option: ", i)
            print("Show option -> h")
            continue
        
        # numbers
        if matched.group(2):
            if int(i) > len(player.hands) or int(i) == 0:
                print(f"You don't have the card :[({i}) ... ]")
                continue

            # check validity of user input
            peek_card = player.hands[int(i)-1]
            if not peek_card.is_same_suit(top_card) and not peek_card.is_same_number(top_card):
                print(f"You couldn't put down : [({i}) {peek_card.show()}]")
                continue

            is_win = play_card(player, player.down_card(int(i)))
            if is_win:
                break

        # instruction
        else:
            if i == 'h':
                print_option()
                continue
            elif i == 'u':
                if len(player.hands) != 2:
                    print("You can't say Uno now. Only you can say uno when you have 2 cards.")
                    continue
                Uno = True
                while Uno:
                    i2 = input("You said Uno! which card put donw?")
                    print(player.show_hands(top_card))
                    if i2 == '1':
                        player.put(0)
                        Uno = False
                    elif i2 == '2':
                        player.put(1)
                        Uno = False
                    else:
                        print("you only have 2 cards!")
            elif i == 't':
                print(top_card.show())
                continue
            elif i == 's':
                player.show_hands(top_card)
                print(f"now top card is : {top_card.show()}")
                print("")
                continue
            elif i == 'q':
                print ("quit the game.")
                Game = False 
                continue
            elif i == 'n':
                i3 = input("you chose new game. do you want to quit this game?[y/n]")
                if i3 == 'y':
                    print("quit the game.")
                    Game = False
                    continue
                else:
                    print("keep going")
                    continue
            elif i == 'd':
                player.add_hand(draw())
            else:
                print("Uh-oh")
                continue

        #AI's turn
        if do_AI(npc1) or do_AI(npc2) or do_AI(npc3):
            Game = False
        
        Player.show_all()

    # AI 를 다변화
    # 덱도 더미도 없을때? 
    # 특수카드?

    Game = False


