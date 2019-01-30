import pygame
from pygame.sprite import Group


from individ import Individ
from passive_gens import PassiveGens
from event_functions import check_events
from main_functions import perform_actions
from settings import Settings


def start():

    settings = Settings()

    pygame.init()
    screen = pygame.display.set_mode([settings.screen_width, settings.screen_height])
    pygame.display.set_caption('My_World')

    organisms = [Individ(settings.screen_width//2, settings.screen_height//2,
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], PassiveGens(), 6)]

    cycle_count = 0
    font = pygame.font.Font(None, 30)
    clock = pygame.time.Clock()

    while True:

        check_events(settings, organisms)
        screen.fill(settings.screen_background)
        add_text(screen, cycle_count, settings, font, organisms)
        pygame.draw.rect(screen, [40, 40, 40], [0, 0, settings.screen_width, settings.screen_height - 60], 5)

        if settings.run == 1:
            for organism in organisms:
                organism.draw(screen, settings)
                perform_actions(organism, organisms, settings)
            cycle_count += 1

        pygame.display.flip()
        clock.tick(settings.max_fps)


def add_text(screen, cycle_count, settings, font, organisms):
    light_text = font.render('light = ' + str(settings.light), True, [0, 0, 0])
    cycles_text = font.render('cycles = ' + str(cycle_count), True, [0, 0, 0])
    fps_text = font.render('max FPS = ' + str(settings.max_fps), True, [0, 0, 0])
    num_organisms_text = font.render('number org-s = ' + str(len(organisms)), True, [0, 0, 0])
    screen.blit(light_text, [10, settings.screen_height - 50])
    screen.blit(cycles_text, [10, settings.screen_height - 20])
    screen.blit(fps_text, [settings.screen_width-210, settings.screen_height - 20])
    screen.blit(num_organisms_text, [settings.screen_width - 210, settings.screen_height - 50])


start()
