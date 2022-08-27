import os
from helper_func import *

def result(winner):
    print("Player ",winner," has won")
    print("Press r to replay, q to quit")
    k = input_without()
    while k is not "r" and k is not "q":
        k = input_without()
    if k is "r":
        os.system('CLS')  
        return 1
    os.system('CLS')  
    print("Game has ended")
    return 0