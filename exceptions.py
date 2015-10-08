# Simple example of Exceptions usage

class RandomClass(object):
    def __init__(self):
        self.randomness = "Random"
        self.justvariable = "Random"

    def __str__(self):
        return " ".join([self.randomness, self.justvariable])

    def set_randomness(self, value):
        if not isinstance(value, str):
            raise Exception('randomness can only be a string')

        self.randomness = value
        return self

    def set_justvariable(self, value):
        if not isinstance(value, str):
            raise Exception('justvariable can only be a string')

        self.justvariable = value
        return self


r = RandomClass()
r.set_randomness('Hola').set_justvariable("Chica!")
print r


some_randomness = [5, 3, 'Another']
for rn in some_randomness:
    try:
        r.set_randomness(rn)
        break
    except Exception as e:
        print e
        continue

print r