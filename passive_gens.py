from random import randint, choice


class PassiveGens:

    def __init__(self):

        self.nutrition = {'meat': 85, 'sun': 80, 'plant': 85}
        self.speed = 5
        self.protection = 5

    def __str__(self):
        out_info = ''
        for key, value in self.nutrition.items():
            out_info += key + ': ' + str(value) + ', '
        out_info += '\n' + 'speed = ' + str(self.speed) + ', protection = ' + str(self.protection)
        return out_info

    def nutrition_mutation(self, settings):
        old_passive_nutrition_gens = self.nutrition.copy()
        type_nutrition = choice(list(self.nutrition))
        mutation_power = randint(-settings.strong_nutrition_mutation, settings.strong_nutrition_mutation)
        self.nutrition[type_nutrition] += mutation_power * 3
        for key in self.nutrition.keys():
            self.nutrition[key] -= mutation_power
            if self.nutrition[key] < 0 or self.nutrition[key] > 250:
                self.nutrition = old_passive_nutrition_gens
                break

    def speed_protection_mutation(self):
        change = randint(-1, 1)
        self.speed += change
        self.protection -= change
        if self.speed < 1 or self.speed > 9:
            self.speed -= change
            self.protection += change
