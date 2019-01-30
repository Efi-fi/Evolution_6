"""
active_ens:
 0 - go
 1~9 - turn (5-sleeping)
|1|2|3|
|4| |6|
|7|8|9|
10 - photosinthesis

"""


import pygame
from pygame.sprite import Sprite
from random import randint


class Individ(Sprite):

    def __init__(self, x, y, active_gens, passive_gens, direction):

        super().__init__()

        self.active_gens = active_gens
        self.passive_gens = passive_gens
        self.direction = direction
        self.x = x
        self.y = y

        self.health = 4000
        self.count = 0
        self.age = 0

    def __str__(self):
        out_info = '='*10 + ' ORGANISM ' + 10*'=' + '\n'
        out_info += 'Age = ' + str(self.age) + '\nPassive gens: \n' + str(self.passive_gens) + '\nActive gens: '
        for gen in self.active_gens:
            out_info += str(gen) + ' '

        return out_info + '\n'

    def full_mutation(self, settings):
        self.health = 4000
        self.count = 0
        self.passive_gens.nutrition_mutation(settings)
        self.passive_gens.speed_protection_mutation()
        self.active_gens_mutation()

    def active_gens_mutation(self):
        change_length = randint(-1, 1)
        if change_length > 0:
            self.active_gens.append(randint(0, 10))
        elif change_length < 0 and len(self.active_gens) > 1:
            del self.active_gens[randint(0, len(self.active_gens) - 1)]
        else:
            self.active_gens[randint(0, len(self.active_gens) - 1)] = randint(0, 10)

    def get_color(self):
        color = []
        coefficient_health = self.health / 10000
        for spectrum in self.passive_gens.nutrition.values():
            color.append(int(spectrum * coefficient_health))
        return color

    def draw(self, screen, settings):
        pygame.draw.circle(screen, self.get_color(), [self.x, self.y],
                           self.passive_gens.protection//settings.size_smoothing+settings.size_smoothing)
