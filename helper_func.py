import os
import msvcrt

def input_without():
    return msvcrt.getch().decode('ASCII')

def print_board(board):
    size = len(board[0])
    for x , i in zip(board , [x for x in range(size)]):
        for y , j in zip(x , [x for x in range(size)]):
            if j == 0:
                print(" ", end='')
            print(y, end='')
            if j is not size-1:
                print(" | ", end='')
        print("")
        if i == size-1:
            pass
        else:
            print(" ――  ――  ――  ――  ―― ")

def print_game(board,player,phase):
    #Clean up the previous board
    os.system('CLS')

    #Print player
    if player:
        print("Player 1's turn!" )
    else:
        print("Player 2's turn!")
    #Ask what to do: phase 0 -> need to choose block, phase 1 -> place block
    if phase:
        print("Push the cube!")
    else:
        print("Choose the cube!")

    #Print board with player cursor
    print_board(board)

def access_check(board):
    P1list_to_return = []
    P2list_to_return = []
    size = len(board[0])
    for x in range(size):
        for y in range(size):
            if x in [0, size-1] or y in [0,size-1]:
                if board[x][y] == 0:
                    P1list_to_return.append([x,y])
                    P2list_to_return.append([x,y])
                elif board[x][y] == 1:
                    P1list_to_return.append([x,y])
                else:
                    P2list_to_return.append([x,y])
    return P1list_to_return, P2list_to_return