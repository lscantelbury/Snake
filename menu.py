import pygame

menu_x = 720
menu_y = 480
window = pygame.display.set_mode((menu_x, menu_y))
menu_bg = pygame.image.load('assets/menu/luis.coimbra_menu.png')
clock = pygame.time.Clock()
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(16, 56, 6)  # phtaloh green
blue = pygame.Color(0, 0, 255)


'''def start_game():
    start_button = pygame.image.load()


def credits():
    credits_button = pygame.image.load()


def quit_game():
    quit_game_button = pygame.image.load()'''


def start_menu():
    menu = True

    while menu:

        window.blit(menu_bg, (0, 0))
        pygame.display.update()
        clock.tick(60)
        

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()

            if 290 + 130 >= mouse[0] >= 290 and 180 + 50 >= mouse[1] >= 180:
                menubg = pygame.image.load('assets/menu/luis.coimbra_menustart.png')
                window.blit(menubg, (0, 0))
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run_game = True
                    menu = False

start_menu()        

