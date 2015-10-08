# Simple example of inheritance and mixins

class Address(object):
    def __init__(self, street, civic, **kw):
        #print '\tAddress class'
        super(Address, self).__init__(**kw)
        self.street = street
        self.civic = civic

class Person(object):
    def __init__(self, name, surname, **kw):
        #print '\tPerson class'
        super(Person, self).__init__(**kw)
        self.name = name 
        self.surname = surname

class InfoMixin(object):
    def info(self):
        #print vars(self)
        for value in vars(self).values():
            print value, 
        print ''

class PersonWithResidence(Person, Address, InfoMixin):
    # implicit operation
    def __init__(self, **kw):
        #print '\tPersonWithResidence class'
        super(PersonWithResidence, self).__init__(**kw)

class AddressWithInfo(Address, InfoMixin):
    # is not necessary to call __init__, is automatic!
    pass


print "** Address With Residence"
a = PersonWithResidence(name='Alex', surname='Comu', street='Random Street', civic=3)
a.info()
print "** Address With Info"
ai = AddressWithInfo(street='Public Street', civic=3)
ai.info()


