import sys

import pygame

from settings import Settings

from ship import Ship

import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    #screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    #background color.
    bg_color = (230, 230, 230)

    ship = Ship(screen)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #Make the most recent draw screen visible.
        pygame.display.flip()

run_game()