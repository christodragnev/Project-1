#Christo Dragnev
#4/4/18
#tic-tac-toe without graphics

from random import *

a=1
b=2
c=3
d=4
e=5
f=6
g=7
h=8
i=9

print('Player 1 goes first and is X')
print(' ')
print('Player 2 goes second and is O')
print(' ')


def printBoard():    #board with numbers as variables (a-i)--> (1-9)
    print('|  ',a,'  |   ',b,'  |   ',c,'  |')
    print('__________________')
    print('|  ',d,'  |   ',e,'  |   ',f,'  |')
    print('__________________')
    print('|  ',g,'  |   ',h,'  |   ',i,'  |')
printBoard()

def isEmpty(square): #checking if square is empty or not
    if (a=='X' or a=='O') and square==1:
        return False
    elif (b=='X' or b=='O') and square==2:
        return False
    elif (c=='X' or c=='O') and square==3:
        return False
    elif (d=='X' or d=='O') and square==4:
        return False
    elif (e=='X' or e=='O') and square==5:
        return False
    elif (f=='X' or f=='O') and square==6:
        return False
    elif (g=='X' or g=='O') and square==7:
        return False
    elif (h=='X' or h=='O') and square==8:
        return False
    elif (i=='X' or i=='O') and square==9:
        return False
    else:
        return True
    
def fullBoard(): 
    if a!=1 and b!=2 and c!=3 and d!=4 and e!=5 and f!=6 and g!=7 and h!=8 and i!=9:
        return True

def winner():
    if a=='X' and e=='X' and i=='X':
        return True
    elif c=='X' and e=='X' and g=='X':
        return True
    elif a=='X' and b=='X' and c=='X':
        return True
    elif d=='X' and e=='X' and f=='X':
        return True
    elif g=='X' and h=='X' and i=='X':
        return True
    elif a=='X' and d=='X' and g=='X':
        return True
    elif b=='X' and e=='X' and h=='X':
        return True
    elif c=='X' and f=='X' and i=='X':
        return True
        
    if a=='O' and e=='O' and i=='O':
        return True
    elif c=='O' and e=='O' and g=='O':
        return True
    elif a=='O' and b=='O' and c=='O':
        return True
    elif d=='O' and e=='O' and f=='O':
        return True
    elif g=='O' and h=='O' and i=='O':
        return True
    elif a=='O' and d=='O' and g=='O':
        return True
    elif b=='O' and e=='O' and h=='O':
        return True
    elif c=='O' and f=='O' and i=='O':
        return True
    


if __name__ == '__main__':
    while True: 
        guess1 = int(input('Player 1, input the number in the place you want chosen: '))
        if guess1 == 1:
            a = 'X'
        elif guess1 == 2:
            b = 'X'
        elif guess1 == 3:
            c = 'X'
        elif guess1 == 4:
            d = 'X'
        elif guess1 == 5:
            e = 'X'
        elif guess1 == 6:
            f = 'X'
        elif guess1 == 7:
            g = 'X'
        elif guess1 == 8:
            h = 'X'
        elif guess1 == 9:
            i = 'X'
        printBoard()
        isEmpty(guess1)
        if winner():
            print('We have a winner!!')
            break
        if fullBoard() == True:
            print('It is a tie!')
            break
        guess2 = int(input('Player 2, input the number in the place you want chosen: '))
        if guess2 == 1:
            a = 'O'
        elif guess2 == 2:
            b = 'O'
        elif guess2 == 3:
            c = 'O'
        elif guess2 == 4:
            d = 'O'
        elif guess2 == 5:
            e = 'O'
        elif guess2 == 6:
            f = 'O'
        elif guess2 == 7:
            g = 'O'
        elif guess2 == 8:
            h = 'O'
        elif guess2 == 9:
            i = 'O'
        printBoard()
        isEmpty(guess2)
        if winner():
            print('We have a winner!!')
            break
       
        if fullBoard() == True:
            print('It is a tie!')
            break
       
        
        
        isEmpty(guess2)
        
        if winner():
            print('We have a winner!!')
            break
         


