class Person:
    #uncalled instances of Person objects will have id zero
    #called instances of Person objects will get incremented id values
    #this can be like a system to check people in without neededing a flag!
    def __init__(self, fn, ln, age=0):
        self.firstname = fn
        self.lastname = ln
        self.age = age
        self.id = 0

    def __call__(self, newid):
        self.id = newid()

    def __repr__(self):
        return str(self.firstname + " " + self.lastname, str(self.age), str(self.id))


person0 = Person("Haruki","Marukami")
person1 = Person("Noboru", "Watanabe")
person2 = Person("May","Kasahara")
person3 = Person("Malta", "Kano")

currentid = 0
@person0
def function():
    return currentid + 1

@person1
def name():
    return currentid + 1

@person2
def doesnt():
    return currentid + 1

@person3
def matter():
    return currentid + 1

personList = [person0, person1, person2, person3]
for p in personList:
    print(p)
class Pizza(object):
    def __init__(self):
        self.toppings = []

    def __call__(self, topping):
        # When using '@instance_of_pizza' before a function definition
        # the function gets passed onto 'topping'.
        self.toppings.append(topping())

    def __repr__(self):
        return str(self.toppings)

pizza1 = Pizza()
pizza2 = Pizza()

@pizza1
def cheese():
    return 'cheese'
@pizza1
def sauce():
    return 'sauce'

@pizza2
def sausage():
    return 'sausage'
@pizza2
def pepperoni():
    return 'pepperoni'

print(pizza1)
print(pizza2)
# ['cheese', 'sauce']
