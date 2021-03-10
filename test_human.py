import unittest
from human import Human


class TestHuman(unittest.TestCase):

    def test_eat(self) -> None:
        # energy is full and try to eat
        human_prins = Human("Prins")
        self.assertEqual(human_prins.eat(20), 20, "Excess should be 20.")

        # energy is below 100 and eat more than required
        human_prins = Human("Prins", energy=90)
        self.assertEqual(human_prins.eat(20), 10, "Excess should 10.")

        # energy is below 100 and eat exactly what is required
        human_prins = Human("Prins", energy=80)
        self.assertEqual(human_prins.eat(20), 0, "Excess should be 0.")

        # energy is below 100 and eat less than required
        human_prins = Human("Prins", energy=70)
        self.assertEqual(human_prins.eat(20), -10, "Excess should be -10.")

    # Add additional tests here.
    def test_grow(self):
        test_human = Human("James", age=20)
        self.assertEqual(test_human.age, 20, "Age should be 20")
        test_human.grow()
        self.assertEqual(test_human.age, 21, "Age should be 21")

    def test_move(self):
        test_human = Human("James", energy=50)
        self.assertEqual(test_human.move(50), True, "Return should be true.")

        test_human = Human("James", energy=50)
        self.assertEqual(test_human.move(60), False, "Return should be false.")

        test_human = Human("James", energy=50)
        test_human.move(30)
        self.assertEqual(test_human.energy, 20, "Energy should be thirty.")

    def test_reproduce(self):
        test_human = Human("James", energy=50)
        self.assertEqual(test_human.reproduce(), True, "Should have enough energy to reproduce.")

        test_human = Human("James", energy=10)
        self.assertEqual(test_human.reproduce(), False, "Should be all tuckered out.")


if __name__ == '__main__':
    unittest.main()