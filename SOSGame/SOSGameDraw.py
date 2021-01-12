import pygame

boardsize = 10
pieces = []
for column in range(1,boardsize):
    pieces.append(list())
    for row in range(1,boardsize):
        pieces[column-1].append(0)    
#init
pygame.init()
pygame.font.init()
# Configure pygame
pygame.key.set_repeat()   # use the keyboard
window = pygame.display.set_mode( (1080, 660) )
font1 = pygame.font.SysFont("comic sans ms",25)
# create a surface to draw uppon
background = pygame.Surface(  window.get_size()  )
background.fill( (255,255,255) )
window.blit(background, (0, 0)  )    # creat the background
pygame.display.set_caption('Welcome to play SOS game')


def DrawTable():
    boardsize = 10
    
    # draw a table
    for i in range(0,boardsize):
        pygame.draw.line(background,(0,0,0),(10, (boardsize-1)*50+10-i*50), ((boardsize-1)*50+10, (boardsize-1)*50+10-i*50), 3)
        pygame.draw.line(background,(0,0,0),(10+i*50, 10), (10+i*50,(boardsize-1)*50+10 ), 3)
        # (boardsize-1)*50+10 is the position of every line
    
    # write word

    player1turn = font1.render("Player 1 score:",False,(0,0,255))
    player2turn = font1.render("Player 2 score:",False,(255,0,0))
    point = font1.render("<==",False,(0,0,255))
    background.blit(point,(10+boardsize*50,72))
    background.blit(player1turn,(10+boardsize*60,72))
    background.blit(player2turn,(10+boardsize*60,372))
 

def DrawPieces():  # draw the text S, O, S|O and player
    boardsize = 10
    font2 = pygame.font.SysFont("comic sans ms",35)
    font3 = pygame.font.SysFont("arial",36)
    for column in range(0,boardsize-1):
        for row in range (0,boardsize-1): 
            for j in pieces[column]:        
                if j == 0:
                    textsurface = font3.render("s|o",False,(255,255,0))
                elif j == 1:    
                    textsurface = font2.render(" S ",False,(0,0,255))
                elif j == 2:
                    textsurface = font2.render(" O ",False,(0,0,255) )
                             
                background.blit(textsurface,(13 + column*50,13 + row*50))