import pygame
import time
import os
pygame.init()


def hard_menu():
    menu = True
    menu_x = 720
    menu_y = 480
    window = pygame.display.set_mode((menu_x, menu_y))
    menubg = pygame.image.load('assets/menu/luis.coimbra_menu_insane.png')
    clock = pygame.time.Clock()
    font = pygame.font.Font('assets/PressStart2P.ttf', 10)

    def credits():
        creditswindow = pygame.display.set_mode((720, 480))
        background = pygame.image.load('assets/menu/credits.png')
        creditswindow.blit(background, (0, 0))
        pygame.display.update()
        time.sleep(10)
        hard_menu()
    
    def options():
        os.system('python3 snake.py')
        quit()

    while menu:

        window.blit(menubg, (0, 0))
        pygame.display.set_caption('Snake Insane Mode')
        pygame.display.update()
        clock.tick(60)

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                quit()

            # Start button
            if 290 + 130 >= mouse[0] >= 290 and 180 + 50 >= mouse[1] >= 180:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run_game = True
                    menu = False
                    return menu

            # Options button
            if 290 + 130 >= mouse[0] >= 290 and 255 + 50 >= mouse[1] >= 255:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    options()
            # Credits button
            if 290 + 130 >= mouse[0] >= 290 and 325 + 50 >= mouse[1] >= 325:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    credits()
                
            # Quit button
            if 290 + 130 >= mouse[0] >= 290 and 395 + 50 >= mouse[1] >= 395:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    quit()


hard_menu()        