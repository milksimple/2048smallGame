#coding:utf8
import random

li = [
       [0,0,0,0],   
       [2,0,0,0],   
       [0,0,0,0],   
       [2,0,4,0]    
     ]

def change(s):
    t = [[],[],[],[]]
    for i in range(0,len(s)):
        for j in range(0,len(s[i])):
            t[i].append(s[j][i])
    return t


def left(s):
                     
    for i in range(0,len(s)):
        for j in range(len(s[i])-1,-1,-1):
            if s[i][j] == 0:
                s[i].pop(j)
                s[i].append(0)
                
    for i in range(0,len(s)):
        j = len(s[i])-1
        while j > 0:
            if s[i][j] == s[i][j-1]:
                s[i][j-1] = 2*s[i][j]
                s[i][j] = 0
                j -= 1
            j -= 1

    for i in range(0,len(s)):
        for j in range(len(s[i])-1,-1,-1):
            if s[i][j] == 0:
                s[i].pop(j)
                s[i].append(0)
    
    return s


def right(s):
    for i in range(0,len(s)):
        for j in range(0,len(s[i])):
            if s[i][j] == 0:
                s[i].pop(j)
                s[i].insert(0,0)
                
    for i in range(0,len(s)):
        j = 0
        while j < len(s[i])-1:
            if s[i][j] == s[i][j+1]:
                s[i][j+1] = 2*s[i][j]
                s[i][j] = 0
                j += 1
            j += 1
    for i in range(0,len(s)):
        for j in range(0,len(s[i])):
            if s[i][j] == 0:
                s[i].pop(j)
                s[i].insert(0,0)
    
    return s
    
def up(s):
    ch1 = change(s)       
    le1 = left(ch1)
    ch2 = change(le1)
    return ch2

def down(s):
    ch1 = change(s)       
    rh1 = right(ch1)
    ch2 = change(rh1)
    return ch2

def rand(t):
    a= random.randint(0,3)
    b = random.randint(0,3)
    number = random.choice([2,4])
    while t[a][b] != 0:
        a= random.randint(0,3)
        b = random.randint(0,3)
        number = random.choice([2,4])
    return a,b,number
while(1):
    key = raw_input("plz input:")
    if key == "a":
        li = left(li)
        a,b,number = rand(li)
        li[a][b] = number
        for x in li:
            print x
            
    elif key == "d":
        li = right(li)
        a,b,number = rand(li)
        li[a][b] = number
        for x in li:
            print x
            
    elif key == "w":
        li = up(li)
        a,b,number = rand(li)
        li[a][b] = number
        for x in li:
            print x
            
    elif key == "s":
        li = down(li)
        a,b,number = rand(li)
        li[a][b] = number
        for x in li:
            print x
    for i in range(0,len(li)):
        for j in range(0,len(li[i])):
            if li[i][j] == 2048:
                print "you win!"
                exit
    

    
