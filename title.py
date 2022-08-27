from helper_func import *

def introduction():
    #Rules
    # 1. From periphery, choose a blank cube or cube with your symbol on it
    # 2. Push the cube to end of the incomplete rows or columns made after you took a cube.
    # 3. When you made either horizontal, vertical or diagonal line with 5 cubes that has your symbol, it will be your victory

    #Control
    # asdw or arrow keys to move your cursor, press shift to choose, space to cancel your choice

    #Title

    print("Press y to start game")
    k = input_without()
    while k is not "y":
        k = input_without()

    #Show until y pressed
    return