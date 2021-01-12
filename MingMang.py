board = []
def newborad():
    #creat a list for the board
    global n
    n = eval(input("How many rows do you want to creat?"))
    while n < 5 :
        n = eval(input("PLease creat a correct board with more than 5 rows:"))
    for i in range (1,n+1):
        board.append(list())
        for s in range (1,n+1):
            if i == 1:
                if s == 1:
                    board[i-1].append(-1) #black pawn
                elif 1 < s:
                    board[i-1].append(1) #white pawn
            elif 1 < i < n:
                if s == 1:
                    board[i-1].append(-1)
                elif 1 < s < n:
                    board[i-1].append(0) #have no pawn
                elif s == n:
                    board[i-1].append(1) 
            elif i == n:
                if s < n:
                    board[i-1].append(-1)
                elif s == n:
                    board[i-1].append(1)           
    return board

def Move():
    global mr,mc
    print("player",player,"'s turn")
    print("please select a pawn")
    r = eval(input("select a pawn (row) : ")) - 1
    c = eval(input("select a pawn (column) : ")) - 1 
    while r > n or c > n:
        print("please select a correct one")
        r = eval(input("select a pawn (row) : ")) -1
        c = eval(input("select a pawn (column) : ")) -1
    judge1R = r-1
    judge1C = c-1
    judge2R = r+1
    judge2C = c+1
    if judge1R < 0:
        judge1R = 0
    if judge1C < 0:
        judge1C = 0
    if judge2R > n-1:
        judge2R = n-1
    if judge2C > n-1:
        judge2C = n-1
    while r < 0 or c < 0 or board[r][c] != a or (board[judge1R][c] != 0 and board[r][judge1C] != 0 and board[judge2R][c] != 0 and board[r][judge2C] != 0):
        print("please select a correct one")
        r = eval(input("select a pawn (row) : ")) -1
        c = eval(input("select a pawn (column) : ")) -1   
    mr = eval(input("select a destination(row) : ")) - 1
    mc = eval(input("select a destination(column) : ")) - 1
    
    while mr > n or mc > n:
        print("please select a correct destination")
        mr = eval(input("select a destination(row) : ")) -1
        mc = eval(input("select a destination(column) : ")) -1

    del board[r][c]
    board[r].insert(c,0)    
    add = 0
    if r == mr and c < mc:
        for i in board[r][c:mc+1]:
            add = add + i
    elif r == mr and c > mc:
        for i in board[r][mc:c+1]:
            add = add + i
    elif r < mr and c == mc:
        x = r
        while x <= mr:
            add = add + board[x][c]
            x += 1
    elif r > mr and c == mc:
        x = mr
        while x <= r:
            add = add + board[x][c]
            x += 1  
    
    while board[mr][mc] == 1 or board[mr][mc] == -1 or (mr != r and mc != c) or add != 0 or (mr == r and mc == c):
        print("please select a correct destination")
        mr = eval(input("select a destination(row) : ")) -1
        mc = eval(input("select a destination(column) : ")) -1
        add = 0
        if r == mr and c < mc:
            for i in board[r][c:mc+1]:
                add = add + i
        elif r == mr and c > mc:
            for i in board[r][mc:c+1]:
                add = add + i
        elif r < mr and c == mc:
            x = r
            while x <= mr:
                add = add + board[x][c]
                x += 1
        elif r > mr and c == mc:
            x = mr
            while x <= r:
                add = add + board[x][c]
                x += 1

    
    del board[mr][mc]
    if player == 1:
        board[mr].insert(mc,1)
    elif player == 2:
        board[mr].insert(mc,-1) 
    
    
    return board
    


def DisplayBoard():   #use the list to creat the board

    for row in range(0,n):
        for i in board[row]:
            if i == -1:
                print(" ◉ ",end="")
            elif i == 1:
                print(" ○ ",end="")
            elif i == 0:
                print(" ▪ ",end="")
        print()           

def judge():
    x = 0                            
    for i in board[mr][mc+1:]:
        x += 1
        if i == 0:
            break
        elif i == a:
            for s in range(1,x):
                del board[mr][mc+s]
                board[mr].insert(mc+s,a)
    x = 0
    for i in board[mr][mc-1::-1]:
        x += 1
        if i == 0:
            break
        elif i == a:
            for s in range(1,x):
                del board[mr][mc-s]
                board[mr].insert(mc-s,a)
    x = 0
    while mr+x <= n:
        x += 1
        if mr+x == n:
            break
        if board[mr+x][mc] == 0:
            print(mr)
            print(x)
            break
        elif board[mr+x][mc] == a:
            for s in range(1,x):
                del board[mr+s][mc]
                board[mr+s].insert(mc,a)

    x = 0
    while mr-x >= 0:
        x += 1
        if board[mr-x][mc] == 0:
            break
        elif board[mr-x][mc] == a:
            for s in range(1,x):
                del board[mr-s][mc]
                board[mr-s].insert(mc,a)

#start the game
newborad() 
DisplayBoard()
#stop the game
stop = False
player = 2
while not stop:
    if player == 2:
        player = 1
        a = 1
    else:
        player = 2
        a = -1

    Move()
    judge()
    DisplayBoard()
    add = 0
    for l in range(0,n):
        for p in board[l]:
            add = add + p
    if add == ((n-1)*4-2):
        print("player 1 is winner!")
        stop = True
    elif add == -((n-1)*4-2):
        print("player 2 is winner!")
        stop = True

