import pygame       
pygame.init()
background=pygame.display.set_mode((1100,600))
font=pygame.font.Font(None,40)
font1=pygame.font.Font(None,50)
font3=pygame.font.Font(None,200)

PLAYER=0
SCORE1=0
SCORE2=0
COLOR=[(200,0,12),(0,255,0),(255,255,55)]       #COLOR CHANGE
time=0

def PLAYERS():                     #To store data of players 
    global PLAYERS
    PLAYERS=[[[],[],[[],[]]],[[],[],[[],[]]]]
PLAYERS()


def RuleABOUTs():                   #To make a rule about sos Game 
            global PLAYER,SCORE1,SCORE2
            score=0
            if (i>=2)and(Board[i-1][j]=="O"and Board[i-2][j]=="S"):
                PLAYERS[PLAYER][2][0].append((j*50+75,i*50-25))
                PLAYERS[PLAYER][2][1].append((j*50+75,i*50+75))
                score+=1

            if (j>=2)and(Board[i][j-1]=="O" and Board[i][j-2]=="S"):
                PLAYERS[PLAYER][2][0].append((j*50-25,i*50+75))
                PLAYERS[PLAYER][2][1].append((j*50+75,i*50+75))
                score+=1
            
            if (i<n-2)and Board[i+1][j]=="O" and Board[i+2][j]=="S":
                PLAYERS[PLAYER][2][0].append((j*50+75,i*50+75))
                PLAYERS[PLAYER][2][1].append((j*50+75,i*50+175))
                
                score+=1
            if (j<n-2)and Board[i][j+1]=="O" and Board[i][j+2]=="S": 
                PLAYERS[PLAYER][2][0].append((j*50+75,i*50+75))
                PLAYERS[PLAYER][2][1].append((j*50+175,i*50+75))
                
                score+=1
            if (i>=2 and j>=2)and Board[i-1][j-1]=="O" and Board[i-2][j-2]=="S":
                PLAYERS[PLAYER][2][0].append((j*50-25,i*50-25))
                PLAYERS[PLAYER][2][1].append((j*50+75,i*50+75))
                
                score+=1
            if (i<n-2 and j<n-2)and Board[i+1][j+1]=="O" and Board[i+2][j+2]=="S": 
                PLAYERS[PLAYER][2][0].append((j*50+75,i*50+75))
                PLAYERS[PLAYER][2][1].append((j*50+175,i*50+175))
                
                score+=1
            if (i>=2 and j<n-2)and Board[i-1][j+1]=="O" and Board[i-2][j+2]=="S": 
                PLAYERS[PLAYER][2][0].append((j*50+75,i*50+75))
                PLAYERS[PLAYER][2][1].append((j*50+175,i*50-25))
                
                score+=1
            if (i<n-2 and j>=2)and Board[i+1][j-1]=="O" and Board[i+2][j-2]=="S":
                PLAYERS[PLAYER][2][0].append((j*50-25,i*50+175))
                PLAYERS[PLAYER][2][1].append((j*50+75,i*50+75))
                
                score+=1

            if PLAYER==0:
                SCORE1+=score
            elif PLAYER==1:
                SCORE2+=score
            if score==0:
                PLAYERChange()


def RuleABOUTo():               #To make a rule about sos Game 
            global PLAYER,SCORE1,SCORE2
            score=0
            if (1<=i<n-1)and Board[i-1][j]=="S" and Board[i+1][j]=="S" :
                PLAYERS[PLAYER][2][0].append((j*50+75,i*50+125))
                PLAYERS[PLAYER][2][1].append((j*50+75,i*50+25))
                
                score+=1
            if (1<=j<n-1)and Board[i][j-1]=="S" and Board[i][j+1]=="S" :
                PLAYERS[PLAYER][2][0].append((j*50+25,i*50+75))
                PLAYERS[PLAYER][2][1].append((j*50+125,i*50+75))
                
                score+=1
            if (1<=i<n-1 and 1<=j<n-1)and Board[i-1][j-1]=="S" and Board[i+1][j+1]=="S":
                PLAYERS[PLAYER][2][0].append((j*50+25,i*50+25))
                PLAYERS[PLAYER][2][1].append((j*50+125,i*50+125))
                 
                score+=1
            if (1<=i<n-1 and 1<=j<n-1)and Board[i-1][j+1]=="S" and Board[i+1][j-1]=="S":
                PLAYERS[PLAYER][2][0].append((j*50+25,i*50+125))
                PLAYERS[PLAYER][2][1].append((j*50+125,i*50+25))

                
                score+=1
            
            if PLAYER==0:
                SCORE1+=score
            else:
                SCORE2+=score
            if score==0:
                PLAYERChange()




def display():                      #To display board 
    global PLAYER
    
    for i in range(1,n+2):
            pygame.draw.line(background,(0,0,0),(50*i,50),(50*i,(n+1)*50),1)
            pygame.draw.line(background,(0,0,0),(50,50*i),(50*(n+1),50*i),1)
    if (SCORE1 or SCORE2)>0:
        for i in range(2):          # draw a line
            for j in range(len(PLAYERS[i][2][0])):
                pygame.draw.line(background,COLOR[i],PLAYERS[i][2][0][j],PLAYERS[i][2][1][j],1)
    for a in range(1,n+1):
        for b in range(1,n+1):
                so=Board[b-1][a-1]   
                if so=="s|o" or so=="s|o\n" :
                    text=font.render("s|o",1,(0,200,184))
                    textpos=(50*a+5,50*b+10)
                    background.blit(text,textpos)
                else:
                        for s in range(2):
                            for i in range(len(PLAYERS[s][0])):
                                    textpos=PLAYERS[s][1][i]
                                    text=font.render(PLAYERS[s][0][i],1,COLOR[s])
                                    background.blit(text,textpos)
                                    
    S=0
    for i in range(n):
        if Board[i].count("s|o")==0:
            S+=1
    if S==n:
        if SCORE1>SCORE2:
            PLAYER=0
        elif SCORE1<SCORE2:
            PLAYER=1
        else:
            PLAYER=2
        if PLAYER<2:
          whowin="The winner is PLAYER "+ str(PLAYER+1)+"!"
        else:
            whowin="NOBODY IS WINNER!"
        text=font.render(whowin,1,COLOR[PLAYER])
        background.blit(text,(700,300))
        
    if time==1 or PLAYER==0:
            TheArrow=font1.render("<---",1,COLOR[0])
            background.blit(TheArrow,(900,100))
    else:
        TheArrow=font1.render("<---",1,COLOR[1])
        background.blit(TheArrow,(900,200))

    scor1=font1.render("Red: "+str(SCORE1),1,COLOR[0])
    scor2=font1.render("Green:  "+str(SCORE2),1,COLOR[1])
    background.blit(scor1,(700,100))
    background.blit(scor2,(700,200))



def PLAYERChange():                           # To change player
    global PLAYER
    if PLAYER==0:
        PLAYER=1
    else:
        PLAYER=0

def Ready():                     #Give you a chance to choose n*n board from 3*3 to 10*10 
    global n,Board,time
    for i in range(1,5):
        if 200*i<x<200*i+50 and 50<y<100:
            n=i+2
            time=1
        elif 200*i<x<200*i+50 and 100<y<150:
            n=i+6
            time=1
    if time==1:
        Board=[["s|o" for i in range(n)]for i in range(n)]
        background.fill((15,10,100))
    
         
        
clock=pygame.time.Clock()
stop=False
while not stop:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            stop=True
        if event.type==pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            if time==0:
                 Ready()
            else:
                time+=1
                for a in range(1,n+1):
                    for b in range(1,n+1):
                            if 50*a<x<50*a+25 and 50*b+50>y>50*b and Board[b-1][a-1]=="s|o":
                                Board[b-1][a-1]="S"
                                j=a-1
                                i=b-1
                                PLAYERS[PLAYER][0].append("S")
                                PLAYERS[PLAYER][1].append((a*50+15,b*50+10))
                                RuleABOUTs()
                            elif 50*a+25<x<50*a+50 and 50*b+50>y>50*b and Board[b-1][a-1]=="s|o":
                                Board[b-1][a-1]="O"
                                j=a-1
                                i=b-1
                                PLAYERS[PLAYER][0].append("O")
                                PLAYERS[PLAYER][1].append((a*50+15,b*50+10))
                                RuleABOUTo()
                            
    background.fill((255,255,255))
    if time==0:
        for i in range(1,5):
            pygame.draw.rect(background,(0,0,0),(200*i,50,50,50),2)
            pygame.draw.rect(background,(0,0,0),(200*i,100,50,50),2)
            text=font.render(str(i+2),1,(255,0,25))
            background.blit(text,(200*i+10,60))
            text=font.render(str(i+6),1,(255,0,25))
            background.blit(text,(200*i+10,110))
            text=font.render("PLEASE CHOOSE A N*N BOARD YOU WANT",1,(255,0,25))
            background.blit(text,(250,400))

    else:
        display()
    pygame.display.flip()
pygame.quit()