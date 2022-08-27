import os
from helper_func import *

def main_game(board):
    os.system('CLS')
    print("Game was played")
    player = True
    phase = True
    game_end = False
    pos = (0,0)
    p1_access,p2_access = access_check(board)
    print_game(board,player,phase)

    while(not game_end):
        next_key = input_without()
        while next_key not in ['a', 's', 'd', 'w', ' ']:
            next_key = input_without()
        
        print_game(board,player,phase)

    #return 0 -> player 1 wins return 1 -> player 2 wins
    return 1