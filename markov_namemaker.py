import random
from collections import defaultdict


class TrainedModel:
    def __init__(self, schars, nlengths, refdict):
        self.start_chars, self.char_weights = schars
        self.name_lengths, self.length_weights = nlengths

        self.model = refdict

    def generate(self):
        namelength = random.choices(self.name_lengths, weights=self.length_weights)[0]
        charlist = random.choices(self.start_chars, weights=self.char_weights)

        for i in range(namelength):
            char = charlist[i]

            if char in self.model:
                poschars, charweights = self.model[char]
                charlist.append(random.choices(poschars, weights=charweights)[0])
            else:
                charlist.append('a')

        return ''.join(charlist)

def get_weights(vlist:list):
    length = len(vlist)
    uniquevals = set(vlist)

    weights = [vlist.count(val)/length for val in uniquevals]

    return list(uniquevals), weights


def train(textfile):
    schars = []
    sizelist = []
    chardict = defaultdict(list)

    with open(textfile) as f:
        text = f.read()

    names = text.split('\n')

    for name in names:
        length = len(name)

        schars.append(name[0])
        sizelist.append(length)

        for i in range(1, length):
            lc, c = name[i-1], name[i]
            chardict[lc].append(c)

    start_chars = get_weights(schars)
    name_lengths = get_weights(sizelist)

    optdict = {char: get_weights(item) for char, item in chardict.items()}

    return TrainedModel(start_chars, name_lengths, optdict)