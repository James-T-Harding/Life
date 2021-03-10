from enum import Enum
import random

class Size(Enum):
    x_small = "extra small"
    small = "small"
    medium = "medium"
    x_medium = "extra medium"
    large = "large"
    x_large = "extra large"


class Color(Enum):
    red = "red"
    green = "green"
    black = "black"
    grey = "grey"


class Material(Enum):
    cotton = "cotton"
    synthwool = "synthwool"
    hyperweave = "hyperweave"


class Clothing:
    def __init__(self, colour: Color, material: Material, size: Size):
        self.colour = colour
        self.material = material
        self.size = size


itemlist = [Clothing(Color.red, Material.cotton, Size.medium),
            Clothing(Color.black, Material.synthwool, Size.small),
            Clothing(Color.grey, Material.synthwool, Size.medium),
            Clothing(Color.green, Material.hyperweave, Size.x_medium),
            Clothing(Color.grey, Material.cotton, Size.large),
            ]