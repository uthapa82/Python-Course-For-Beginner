import sys

import pygame

#from ship import Ship

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    bg_color = (0, 0, 230) #creation blue screen only.

    #ship = Ship(screen)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        screen.fill(bg_color)

        #ship.blitme()

        pygame.display.flip()

run_game()