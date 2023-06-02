import sys
import math

n = int(input())
p = [0] * n
for i in range(n):
    p[i] = int(input())

p.sort()
d = sys.maxsize


for i in range(1, n):
    d = min(d, p[i] - p[i - 1])

print(d)