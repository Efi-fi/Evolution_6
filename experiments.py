from individ import Individ
from passive_gens import PassiveGens


passive_gens = PassiveGens()
individ = Individ(2, 3, [1, 2, 3, 4, 5, 6], passive_gens, 4)

print(individ)