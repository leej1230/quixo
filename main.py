#from file_name import function_name
from title import introduction
from game import main_game
from end import result

def main():
    
    introduction()
    replay = 1
    while replay:
        #Game Starts, returns winner -> either 0 or 1
        board = [[ 0 for _ in range(5)] for _ in range(5)]
        winner = main_game(board)

        #Result screen, give 0 when player 1 wins, 1 when player 2 wins -> r to replay, q to quit 
        replay = result(winner)

    return

if __name__ == "__main__":
    main()
else:
    print("Undefined error has occured")