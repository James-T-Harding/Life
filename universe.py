from planet import Planet
import markov_namemaker
import random

class Universe:
    def __init__(self) -> None:
        self.planets = []

    def generate(self, objectno) -> Planet:
        model = markov_namemaker.train("PlanetNames.txt")

        for i in range(objectno):
            newplanet = Planet(model.generate())
            newplanet.populate(random.randint(1, 50))

            self.planets.append(newplanet)

    def __repr__(self):
        return f"Universe({', '.join([repr(p) for p in self.planets])})"

    def __str__(self):
        names = [p.name for p in self.planets]

        return f"A universe of mystery and wonder, consisting of the planets {', '.join(names[:-1])} and {names[-1]}"

universe = Universe()
universe.generate(10)

print(universe)

for planet in universe.planets:
    planet.poplist()
