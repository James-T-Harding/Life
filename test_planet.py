import unittest
from human import Human
from planet import Planet


class TestPlanet(unittest.TestCase):

    def mkplanet(self):
        gibs = Planet("Gibson")
        gibs.add(h := Human("Golo"))

        return gibs, h

    def test_init(self):
        p = Planet("Gibson")

        self.assertEqual(p.name, "Gibson")
        self.assertEqual(p.humans, [])

    def test_add(self):
        p, h = self.mkplanet()
        self.assertEqual(p.humans, [h])

    def test_remove(self):
        p, h = self.mkplanet()
        p.remove(h)

        self.assertEqual(p.humans, [])

    def test_has(self):
        p, h = self.mkplanet()

        self.assertEqual(p.has(h), True)

    def test_population(self):
        p, h = self.mkplanet()

        self.assertEqual(p.population(), 1)

if __name__ == '__main__':
    unittest.main()