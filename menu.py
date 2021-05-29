import pygame

menu_x = 720
menu_y = 480
window = pygame.display.set_mode((menu_x, menu_y))
menubg = pygame.image.load('assets/menu/luis.coimbra_menu.png')
clock = pygame.time.Clock()
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

def quitgame():
    quitgame_button = pygame.image.load()

def Start_Menu():

    menu = True

    while menu:

        window.fill(black)
        pygame.draw.rect(window,(290, 180, 130, 50) )
while True:
    window.blit(menubg, (0, 0))

    '''pygame.draw.rect(window, )
    pygame.draw.rect(window, )
    pygame.draw.rect(window, )'''

    pygame.display.update()
    clock.tick(15) 