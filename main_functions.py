import math
from random import randint, choice

from individ import Individ
from passive_gens import PassiveGens


def perform_actions(organism, organisms, settings):
    num_step = organism.passive_gens.speed
    while num_step > 0:
        if do_action(organism, organisms, settings):
            break
        num_step -= 1

    organism.age += 1


def do_action(organism, organisms, settings):
    if organism.count > len(organism.active_gens) - 1:
        organism.count = 0

    action = organism.active_gens[organism.count]
    organism.count += 1

    if action == 0:
        if perform_move(organism, organisms, settings):
            return True
    elif action == 5:
        organism.health -= 5
    elif action == 10:
        organism.health += organism.passive_gens.nutrition['sun'] * settings.light
    else:
        organism.health -= 20
        organism.direction = choice([1, 2, 3, 4, 6, 7, 8, 9])

    for organism_b in organisms:
        if organism_b is not organism and get_collide(organism, organism_b):
                organism.health -= (4*get_strength(organism_b) - get_defense(organism))
                organism_b.health -= (4*get_strength(organism) - get_defense(organism_b))
                verify_organism(organism_b, organisms, settings)

    return verify_organism(organism, organisms, settings)


def verify_organism(organism, organisms, settings):
    if organism.health < 1:
        if len(organisms) > 1:
            organisms.remove(organism)
            return True
        else:
            organism.age = 0
            organism.full_mutation(settings)
    elif organism.health > 10000:
        organism.health = 4000
        passive_gens = PassiveGens()
        passive_gens.nutrition = organism.passive_gens.nutrition.copy()
        passive_gens.speed = organism.passive_gens.speed
        passive_gens.protection = 10-passive_gens.speed
        new_organism = Individ(organism.x + randint(-15, 15), organism.y + randint(-15, 15),
                               organism.active_gens[:], passive_gens, organism.direction)
        new_organism.full_mutation(settings)
        correct_place(new_organism, settings)
        organisms.append(new_organism)


def perform_move(organism, organisms, settings):

    if organism.direction < 4:
        organism.y -= 1
    elif organism.direction > 6:
        organism.y += 1

    if organism.direction % 3 == 0:
        organism.x += 1
    elif (organism.direction-1) % 3 == 0:
        organism.x -= 1

    correct_place(organism, settings)

    organism.health -= 50

    for organism_b in organisms:
        if organism_b is not organism and get_collide(organism, organism_b):
            if get_strength(organism) >= get_defense(organism_b):
                devouring(organism, organism_b, organisms)

            elif get_strength(organism_b) > get_defense(organism):
                devouring(organism_b, organism, organisms)
                return True


def get_collide(organism_a, organism_b):
    distance = math.sqrt((organism_a.x-organism_b.x)**2+(organism_a.y-organism_b.y)**2)
    if distance <= organism_a.passive_gens.protection+organism_b.passive_gens.protection+3:
        return True


def get_strength(organism):
    strength = 6 * organism.passive_gens.nutrition['meat'] + 3 * organism.passive_gens.nutrition['plant']
    strength += organism.health//4
    return strength


def get_defense(organism):
    defense = 2 * organism.passive_gens.nutrition['sun'] + organism.passive_gens.nutrition['plant']
    defense *= organism.passive_gens.protection
    defense += organism.health//4
    return defense


def devouring(organism_win, organism_lose, organisms):
    adding_health = organism_win.passive_gens.nutrition['plant'] * organism_lose.passive_gens.nutrition['sun'] + \
                    organism_win.passive_gens.nutrition['meat'] * organism_lose.passive_gens.nutrition['plant']
    organism_win.health += adding_health // 10
    organisms.remove(organism_lose)


def correct_place(organism, settings):

    if organism.x < 5:
        organism.x = 5
    elif organism.x > settings.screen_width-5:
        organism.x = settings.screen_width-5

    if organism.y < 5:
        organism.y = 5
    elif organism.y > settings.screen_height-65:
        organism.y = settings.screen_height-65

