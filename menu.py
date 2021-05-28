import pygame 

menu_x = 720
menu_y = 480
menubg = pygame.display.s0et_mode((menu_x, menu_y))
image = pygame.image.load('assets/luis.coimbra_menu.png')
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(16, 56, 6) #phtaloh green
blue = pygame.Color(0, 0, 255)

def startgame():
    start_button = pygame.image.load()

def credits():
    credits_button = pygame.image.load()  

def quitgame():
    quitgame_button = pygame.image.load()

def menu:
    menu = True

    while menu:
        menubg.blit(menubg, (0 ,0))
        for event in pygame.event.get()
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        menubg = pygame.image.load("/assets/luis.coimbra_menuquit")
        
    pygame.draw.rect(menubg, )