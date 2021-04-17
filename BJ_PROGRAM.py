# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Programming Blackjack

#import chain
from itertools import chain

decks_in_shoe = int(input("Enter the number of decks in shoe."))

cheatsheet = {
    (5,6,7,8) : ["H","H","H","H","H","H","H","H","H","H"],
    (9,"A6") : ["H","D","D","D","D","H","H","H","H","H"],
    (10,"55") : ["D","D","D","D","D","D","D","D","H","H"],
    11 : ["D","D","D","D","D","D","D","D","D","H"],
    12 : ["H","H","S","S","S","H","H","H","H","H"],
    (13,14) : ["S","S","S","S","S","H","H","H","H","H"],
    15 : ["S","S","S","S","S","H","H","H","H/R","H"],
    16 : ["S","S","S","S","S","H","H","H/R","H/R","H/R"],
    (17,"A8""A9","TT") : ["S","S","S","S","S","S","S","S","S","S"],
    ("A2","A3") : ["H","H","H","D","D","H","H","H","H","H"],
    ("A4","A5") : ["H","H","D","D","D","H","H","H","H","H"],
    "A7" : ["S","D","D","D","D","S","S","H","H","H"],
    ("22","33") : ["H/P","H/P","P","P","P","P","H","H","H","H"],
    "44" : ["H","H","H","H/P","H/P","H","H","H","H","H"],
    "66" : ["H/P","P","P","P","P","H","H","H","H","H"],
    "77" : ["P","P","P","P","P","P","H","H","H","H"],
    ("88","AA") : ["P","P","P","P","P","P","P","P","P","P"],
    "99" : ["P","P","P","P","P","S","P","P","S","S"],
}

dict_cards_point = {(1,11) : "A",2 : "2",3 : "3",4 : "4",5 : "5",6 : "6",7 : "7",8 : "8",9 : "9",10 : ["T","J","Q","K"]}

cards = list(chain.from_iterable(list(dict_cards_point.values())))
deck = cards*4
shoe = deck*decks_in_shoe

#make a blackjack session