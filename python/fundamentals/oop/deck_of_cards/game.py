from classes.deck import Deck
from classes.player import Player
import random
import re

top_card = None
dummy = None
deck = None

def show_hands(player_list):
    for p in player_list:
        p.show_hands()

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


def do_AI(npc):
    global top_card
    global deck, dummy

    for idx, card in enumerate(npc.hands):
        if card.suit == top_card.suit:
            the_card = npc.down_card(idx+1)
            dummy.add(the_card)
            top_card = the_card
            npc.uno()
            return npc.win()
    
    for idx, card in enumerate(npc.hands):
        if card.string_val == top_card.string_val:
            the_card = npc.down_card(idx+1)
            dummy.add(the_card)
            top_card = the_card

            npc.uno()
            return npc.win()
    
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
    npc1 = Player("Anna", is_ai = True)
    npc2 = Player("Elsa", is_ai = True)
    npc3 = Player("Sven", is_ai = True) 

    player_list =[]
    player_list.append(player)
    player_list.append(npc1)
    player_list.append(npc2)
    player_list.append(npc3)


    print("Welcome", user_name)


    initialize_game(player_list)
    print_option()
    p = re.compile("^[udqnost1-9]{1}$")
    # for debugging
    show_hands(player_list)

    top_card = deck.get()
    dummy = Deck(is_empty = True)
    dummy.add(top_card)

    Game = True
    while Game:

        print("top >>", top_card.show())
        player.show_hands()

        i = input("What will you do next?")
        if not p.match(i):
            print("wrong option")
            continue

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
                print(player.show_hands())
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
            player.show_hands()
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
            if int(i) > len(player.hands):
                print("You don't have the card :", i)
                continue

            # check validity of user input
            peek_card = player.hands[int(i)-1]
            if peek_card.string_val != top_card.string_val and peek_card.suit != top_card.suit:
                print("You couldn't put down : ", peek_card.show())
                continue
            top_card = player.down_card(int(i))
            dummy.add(top_card)
            if player.win():
                Game = False


        #AI's turn
        if do_AI(npc1) or do_AI(npc2) or do_AI(npc3):
            Game = False
        
        show_hands(player_list)

    # AI 를 다변화
    # 낼 수 있는 것만 표시해줘
    # 정규식 고쳐야됨.
    # 드로우를 많이 했을때 ? 덱도 더미도 없을때 => 더 많은 핸드카드를 낼 수 있게 바꿀것



    Game = False


