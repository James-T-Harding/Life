from clothing import Clothing


class Human:
    MAX_ENERGY = 100
    MOVE_ENERGY = 10
    REPRODUCE_ENERGY = 20

    def __init__(self, name: str, age: int = 0, energy: int = 100):
        self.name = name
        self.age = age
        self.energy = energy

        self.clothes = []

    def __str__(self):
        return f'{self.name} is {self.age} years old and currently has {self.energy}'

    def __repr__(self) -> str:
        return f'human(name={self.name}, age={self.age}, energy={self.energy})'

    def grow(self) -> None:
        self.age += 1

    def eat(self, amount: int) -> int:
        energy = self.energy + amount

        self.energy = min(energy, self.MAX_ENERGY)

        return energy-self.MAX_ENERGY

    def reproduce(self) -> bool:
        if result := self.energy >= self.REPRODUCE_ENERGY:
            self.energy -= self.REPRODUCE_ENERGY

        return result

    def move(self, distance: int) -> bool:
        if result := self.energy >= distance:
            self.energy -= distance

        return result

    def dress(self, clothing: Clothing):
        self.clothes.append(clothing)

    def undress(self, clothing: Clothing):
        self.clothes.remove(clothing)
