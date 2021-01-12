from random import*
def Board():
        for y in range (0,n):
                print(board[y],"| ",end="")
        print()
        print("----"*n)
        #make the board number
        for p in range(1,n+1):
                print(p,"| ",end="") 
        print()      
def ChooseSquare():
        global x
        m = False
        while not m:
                try:
                        x = eval(input("Choose the square:"))
                        m = True
                except:
                        m = False   
        while x > n or x < 2:
                x =  eval(input("Please type correct number:"))
        s = board[x-1] - 1
        while s < 0:
                x =  eval(input("Please type correct number:"))
                s = board[x-1] - 1
        del board[x-1]
        board.insert(x-1,s)
        return board
def ChooseDestination():
        m = False
        while not m:
                try:
                        destination = eval(input("Choose the destination:"))
                        m = True
                except:
                        m = False
        while destination >= x:
                ChooseDestination()
        d = board[destination-1] + 1
        del board[destination-1]
        board.insert(destination-1,d)
        Board()
        
        return board

t = False
while not t:
        try:    
                n = int(input("How long do you want to play:"))
                t = True
        except:
                t = False
while n < 2:    #judge the length of board whether turn or false
        try:
                n = int(input("Please choose the length more then 2 :"))
        except:
                n = 0
 


a = randint(0,n)
board = [a]
b = 0
while b < n:
        a = randint(0,n)
        board.append(a)
        b += 1
Board()    
#start and stop the game

text = [0]
for i in range(1,n):
        numb = board[i] + text[i - 1]
        text.append(numb)

player = 2
while numb > 0:
        if player == 2:
                player = 1
        else:
                player = 2
        print("player",player,"'s turn")
        
        ChooseSquare()
        ChooseDestination()
        text = [0]
        for i in range(1,n):
                numb = board[i] + text[i - 1]
                text.append(numb)

#judge who is winner
if player == 2:
        player = 1
else:
        player = 2
print("player",player," is winner!")

        

