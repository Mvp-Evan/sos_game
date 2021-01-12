import pygame
import SOSGameDraw
boardsize = 10
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


clock = pygame.time.Clock()

stop = False


while not stop:
    
    clock.tick(60)
    x,y = pygame.mouse.get_pos()    # have got the position of mouse and it need add the event into the mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 10 <= x <= 10 + (boardsize-1)*50 and 10 <= y <= 10 + (boardsize-1)*50: 
            # need a judgement to use it but before that have to creat a list to remenber the color of pieces
                print(x,y)
            if 10 <= x <= 10+25:
                del pieces[0][0]
                pieces[0].insert(0,1)
                print(pieces)
        
    SOSGameDraw.DrawTable()
    SOSGameDraw.DrawPieces()
    window.blit(background, (0, 0))
    pygame.display.flip()


pygame.quit()