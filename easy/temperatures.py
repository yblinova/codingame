import sys
import math


n = int(input())  
min = float('inf')

for i in input().split():
    t = int(i)
    if abs(0-t) < abs(0-min):
        min = t
    elif abs(min) == abs(t):
        if min >= t :
            min = min
        elif t > min : 
            min = t
         
    

if (min == float('inf')):
    print(0)
else:
    print(min)