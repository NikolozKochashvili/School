from math import *

def check (a):
    if a <= 1: 
        return False
    a = int(a)
    pos = 2
    while pos <= int(sqrt(a)):
        if a % pos == 0:
            return False
        pos += 1
    return True  

cur = 2
cnt = 0
while cnt < 50:
    if (check(cur)):
        cnt += 1
        print (f"{cur:<4}",end = '  ')
    
    if (cnt%6==0 and check(cur)):
        print()
    cur += 1
