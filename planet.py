import random
import names
from human import Human


class Planet:
    def __init__(self, name: str):
        self.name = name
        self.humans = []

    def __repr__(self):
        return f"Planet(name = {self.name}, humans = {self.humans})"

    def __str__(self):
        return f"{self.name} contains {self.population()} humans."

    def add(self, human: Human):
        self.humans.append(human)

    def remove(self, human: Human):
        if ret := human in self.humans:
            self.humans.remove(human)

        return ret

    def has(self, human: Human):
        return human in self.humans

    def poplist(self):

        print(f"{self.name}: \n")
        fstr = "{0:25}{1:<5}{2:<8}"

        print(fstr.format("Name", "Age", "Energy"), '\n')

        for p in self.humans:
            print(fstr.format(p.name, p.age, p.energy))

        print(f"\nTotal population: {self.population()}\n")

    def populate(self, no):
        for i in range(no):
            name = names.get_full_name()
            age = random.randint(1, 93)
            energy = random.randint(0, 100)

            human = Human(name, age, energy)

            self.add(human)

    def population(self):
        return len(self.humans)