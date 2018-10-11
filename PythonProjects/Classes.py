class Person:
    def __init__(self, fn, ln, age):
        self.firstname = fn
        self.lastname = ln
        self.age = age
        self.id = 0
        self.currentid = self.id +1

    def __call__(self, id):
        self.id = self.currentid
        self.currentid = self.currentid + 1

    def __repr__(self):
        return str(self.id)
        
person = Person("Bob","Smith", 20)

@person
def nextid():
    return person.id

@person
def nextid():
    return person.id

print(person)
print(person)

class Pizza(object):
    def __init__(self):
        self.toppings = []

    def __call__(self, topping):
        # When using '@instance_of_pizza' before a function definition
        # the function gets passed onto 'topping'.
        self.toppings.append(topping())

    def __repr__(self):
        return str(self.toppings)

pizza = Pizza()

@pizza
def cheese():
    return 'cheese'
@pizza
def sauce():
    return 'sauce'

print(pizza)
# ['cheese', 'sauce']
