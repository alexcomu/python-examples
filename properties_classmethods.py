class Address(object):
    _cap = []

    def __init__(self):
        self._cap = []

    def append_cap(self, value):
        self._cap.append(value)

    # append to global, all classes
    def append_global_cap(self, value):
        self.__class__._cap.append(value)

    # property definition
    @property
    def cap(self):
        return self._cap + self.__class__._cap

    # class method example
    @classmethod
    def address_with_cap_100(self):
        a = Address()
        a.append_cap(100)
        return a

a = Address()
a.append_global_cap(5)
a.append_cap(1)

b = Address()
b.append_cap(3)
print a.cap, b.cap

c = Address.address_with_cap_100()
print c.cap