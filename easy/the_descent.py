import sys
import math



while 1:
    max = 0
    imax = 0
    for i in range(8):
        mountain_h = int(input()) 
        if mountain_h > max:
            max = mountain_h
            imax = i

    print(imax)