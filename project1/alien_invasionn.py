import sys

import pygame

from ship import Ship

import game_function as gf

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    #For colour background
    bg_color = (230, 230, 230)

    ship = Ship(screen)
    
    while True:
        gf.check_event()
        gf.update_screen(ai_settings=, screen=, ship=)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        screen.fill(bg_color)

        ship.blitme()

        pygame.display.flip()

run_game()