import pygame 

menu_x = 720
menu_y = 480
menu = pygame.display.set_mode((menu_x, menu_y))
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
        for event in pygame.event.get()
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        menu = pygame.image.load("/assets/luis.coimbra_menu")
        
    pygame.draw.rect(gameDisplay)