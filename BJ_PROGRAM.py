# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Programming Blackjack

#import chain
from itertools import chain

# decks_in_shoe = int(input("Enter the number of decks in shoe."))
decks_in_shoe = 6

# Cheatsheet provide as basic strategy to win in blackjack. Keys are the cards_points by me and values are 2 to A card held by the dealer.
cheatsheet = {
    (5,6,7,8) : ["H","H","H","H","H","H","H","H","H","H"],
    (9,"A6",[7,17]) : ["H","D","D","D","D","H","H","H","H","H"],
    (10,"55") : ["D","D","D","D","D","D","D","D","H","H"],
    11 : ["D","D","D","D","D","D","D","D","D","H"],
    12 : ["H","H","S","S","S","H","H","H","H","H"],
    (13,14) : ["S","S","S","S","S","H","H","H","H","H"],
    15 : ["S","S","S","S","S","H","H","H","H/R","H"],
    16 : ["S","S","S","S","S","H","H","H/R","H/R","H/R"],
    (17,"A8""A9","TT",[9,19],[10,20]) : ["S","S","S","S","S","S","S","S","S","S"],
    ("A2","A3",[3,13],[4,14]) : ["H","H","H","D","D","H","H","H","H","H"],
    ("A4","A5",[5,15],[6,16]) : ["H","H","D","D","D","H","H","H","H","H"],
    ("A7",[8,18]) : ["S","D","D","D","D","S","S","H","H","H"],
    ("22","33") : ["H/P","H/P","P","P","P","P","H","H","H","H"],
    "44" : ["H","H","H","H/P","H/P","H","H","H","H","H"],
    "66" : ["H/P","P","P","P","P","H","H","H","H","H"],
    "77" : ["P","P","P","P","P","P","H","H","H","H"],
    ("88","AA",[2,12]) : ["P","P","P","P","P","P","P","P","P","P"],
    "99" : ["P","P","P","P","P","S","P","P","S","S"],
}

# Setting up the deck and shoe. In blackjack suites doesn't matter.
cards = ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]
deck = cards*4
shoe = deck*decks_in_shoe

# Now I have to code a blackjack session.
# Enter the cards dealt.
cards_dealt = input()

# crards dealt to me and dealer
dealer_card = cards_dealt[1]
dealer_hand = cards_dealt[1] + cards_dealt[2] #not visible in real-game
my_hand = cards_dealt[0] + cards_dealt[1]

#funtion to return hand value:
def return_card_value(hand):
    sum = 0
    for card in hand:
        if isinstance(sum,list):
            if card is "A":
                sum = sum[0]+1
            elif card is in ("T","J","Q","K"):
                sum = sum[0] + 10
            elif:
                if sum[1] + int(card) > 21:
                    sum = sum[0] + int(card)
                elif sum[1] + int(card) == 21:
                    sum = 21
                elif:
                    sum = [sum[0]+int(card), sum[1]+int(card)]
        else:
            if card is "A":
                if sum + 11 > 21:
                    sum += 1
                elif:
                    sum = [sum+1, sum+11]
            elif card is in ("T","J","Q","K"):
                sum = sum+10
            elif:
                sum = sum + int(card)
    return sum

#checking for blackjack
def check_blackjack(hand):
    return len(hand) == 2 and return_card_value(hand) == 21

if len(my_hand) == 2 and return_card_value(my_hand) == 21:
    if len(dealer_hand) == 2 and return_card_value(dealer_hand) == 21:
        #push
    else:
        #win

#follow cheatsheet if not blackjack
def what_to_do(dealer_card, myhand):
    if len(my_hand) == 2:
        if "A" in my_hand or myhand[1]==my_hand[0]:
            y = my_hand
        else:
            y = return_card_value(my_hand)
    else:
        y = return_card_value(my_hand)
    
    x = return_card_value(dealer_card)
    
    if isinstance(x, list):
        x = 11

  return cheatsheet[y][x-2]



# If I get 21 or blackjack
#   If I get blackjack.
#     If dealer has a blackjack - push
#     else win
#   If I get 21.
#     If dealer has a blackjack - loss
#     If dealer has 21 - push
#     else win
# elseIf I bust - loss

# elseIf I stand or double
#   If dealer has a blackjack - loss
#   elseIf dealer bust - win
#   elseIf dealer has < me - win
#   elseIf dealer has > me - loss
#   elseIf dealer has = me - push

