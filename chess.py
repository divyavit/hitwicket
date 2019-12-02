'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def movea(k3,c):

    l6=c.split(':')
    a=l6[0]
    b=l6[1]
    for i in range(0,5):
        for j in range(0,5):
            l=k3[i][j].split('-')
            if(l[0]=='A'):
                if(l[1]==a):
                    if(l[1]=='F'):
                        k3[i-1][j]=k3[i][j]
                        k3[i][j]='-'
                    else:
                        k3[i+1][j]=k3[i][j]
                        k3[i][j]='-'
    return k3
                  
def moveb(k3,c):
    
    l6=c.split(':')
    a=l6[0]
    b=l6[1]
    for i in range(0,5):
        for j in range(0,5):
            l=k3[i][j].split('-')
            if(l[0]=='B'):
                if(l[1]==a):
                    if(l[1]=='F'):
                        k3[i+1][j]=k3[i][j]
                        k3[i][j]='-'
                    else:
                        k3[i-1][j]=k3[i][j]
                        k3[i][j]='-'
    return k3   
def moveh1a(k3,c):
    l6=c.split(':')
    a=l6[0]
    b=l6[1]
    for i in range(0,5):
        for j in range(0,5):
            l=k3[i][j].split('-')
            if(l[0]=='A'):
                if(l[1]==a):
                    if(l[1]=='F'):
                        k3[i-2][j]=k3[i][j]
                        k3[i][j]='-'
                        k[i-1][j]='-'
                    else:
                        k3[i+2][j]=k3[i][j]
                        k3[i][j]='-'
                        k3[i+1][j]='-'
    return k3
            
def matrix(m,li,k,c):
    for i in range(0,5):
        for j in range(0,5):
            if(i==m):
                if c%2==0:
                    k1='A-'
                else:
                    k1='B-'
                k[i][j]=k1+li[j]
            else:
                k[i][j]='-'
    
    return k   
def moveh1b(k3,c):
    
    l6=c.split(':')
    a=l6[0]
    b=l6[1]
    for i in range(0,5):
        for j in range(0,5):
            l=k3[i][j].split('-')
            if(l[0]=='B'):
                if(l[1]==a):
                    if(l[1]=='F'):
                        k3[i+2][j]=k3[i][j]
                        k3[i+1][j]='-'
                        k3[i][j]='-'
                    else:
                        k3[i-2][j]=k3[i][j]
                        k3[i-1][j]='-'
                        k3[i][j]='-'
    return k3 
def printmat(v):
    print("printed matrix: ")
    for i in range(0,5):
        for j in range(0,5):
            print(v[i][j],end='')
        print('')
def s(a):
    l=a.split(",")
    li=[]
    
    for i in l:
        li.append(i)
    return li
   
a=input("Player1 enter input: ")
c=0
li=s(a)
k3=[[]]
d='-'
for i in range(0,5):
    k3.append()
    for j in range(0,5):
        k3[i]j]='-'
printmat(k3)
k3=matrix(4,li,k3,c)
c=c+1
printmat(k3)
b=input("Player2 enter input: ")
li=s(b)
k3=matrix(0,li,k3,c)
printmat(k3)
while(1):
    c=input("enter input for player 1: ")
    l9=c.split(':')
    if 'P' in l9[0]:
        
        k3=movea(k3,c)
    else:
        if 'H1' in l9[0]:
            k3=moveh1a(k3,c)
        else:
            k3=moveh2a(k3,c)
    c=input("enter input for player 2")
    l9=c.split(':')
    if 'P' in l9[0]:
        
        k3=moveb(k3,c)
    else:
        if 'H1' in l9[0]:
            k3=moveh1b(k3,c)
        else:
            k3=moveh2b(k3,c)
    ans=input("do you want to continue y/n")
    if ans=='y':
        break

class chess_grid:
    public:
        
        
        


    