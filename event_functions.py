import pygame
from sys import exit


def check_events(settings, organisms):

    for event in pygame.event.get():
        check_exit(event, organisms)
        check_changes_settings(event, settings)


def check_exit(event, organisms):

    if event.type == pygame.QUIT:
        best_age = 0
        best_organism = None
        for organism in organisms:
            if organism.age > best_age:
                best_age = organism.age
                best_organism = organism

        print(best_organism)
        exit()


def check_changes_settings(event, settings):

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            settings.run *= -1

        elif event.key == pygame.K_LEFT and settings.light > -50:
            settings.light -= 1
            for i in range(0, 3):
                settings.screen_background[i] -= 1
        elif event.key == pygame.K_RIGHT and settings.light < 150:
            settings.light += 1
            for i in range(0, 3):
                settings.screen_background[i] += 1

        elif event.key == pygame.K_UP:
            settings.max_fps += 1
        elif event.key == pygame.K_DOWN:
            settings.max_fps -= 1

        elif event.key == pygame.K_0:
            settings.__init__()
