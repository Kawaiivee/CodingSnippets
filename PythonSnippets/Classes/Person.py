class Person(object):
    def __init__(self, fn="First Name", ln="Last Name", a="Age", g="Gender", i="ID"):
        self.firstname = fn
        self.lastname = ln
        self.age = a
        self.gender = g
        self.id = i

    def __repr__(self):
        return str(self.firstname + "/" + self.lastname + "/" + str(self.age) + "/" + self.gender + "/" + str(self.id))

    #selector uses a char to select which attribute to change
    #checks to see if the right data type is used per variable
    def setAtt(self, selector, att):
        if selector == 'f':
            assert isinstance(att, str)
            self.firstname = att
        elif selector == 'l':
            assert isinstance(att, str)
            self.lastname = att
        elif selector == 'a':
            assert isinstance(att, int)
            self.age = att
        elif selector == 'g':
            assert isinstance(att, str)
            self.gender = att
        elif selector == 'i':
            assert isinstance(att, int)
            self.id = att
        else:
            print("Please specify an attribute to modify")
            pass

    #selector uses a char to select which attribute to return
    def getAtt(self, selector):
        if selector == 'f':
            return self.firstname
        elif selector == 'l':
            return self.lastname
        elif selector == 'a':
            return self.age
        elif selector == 'g':
            return self.gender
        elif selector == 'i':
            return self.id
        else:
            print("Please specify an attribute to return\ncontinuing execution...")
            pass

person = Person()
person0 = Person("Haruki", "Marukami", 25, "Male", 1234)
person1 = Person("Noboru", "Watanabe", 30, "Male", 2345)
person2 = Person("May", "Kasahara", 15, "Female", 3456)
person3 = Person("Malta", "Kano", 25, "Female", 4657)

personDict = {}
personDict['p'] = person
personDict['p0'] = person0
personDict['p1'] = person1
personDict['p2'] = person2
personDict['p3'] = person3

print("\n" + person.__repr__() + "\n")
person.setAtt('f', "Marri")
person.setAtt('l', "Soliuga")
person.setAtt('a', 21)
person.setAtt('g', "Female")
person.setAtt('i', 9890)

#explicit use of __repr__ lets you concatenate with '+'
for p in personDict:
    print(p.__repr__() + " " + personDict[p].__repr__())
print("\n")

#implicit use of __repr__ means you can't concatenate
for p in personDict:
    print(p, personDict[p])

class Student(Person):
    def __init__(self,f="First Name", l="Last Name", a="Age", g="Gender", i="ID", m="Major"):
        super(Student, self).__init__(f, l, a, g, i)
        self.sid = 'A-' + str(i)
        self.major = m

    def __repr__(self):
        return super(Student, self).__repr__() + str("/" + self.major + "/" + self.sid)

student = Student()

#New Student Object
student0 = Student("Anadi", "Uw", 20, "Male", 2016, "ChE")

#Changing and existing person to student
student1 = Student(person.getAtt('f'), person.getAtt('l'), person.getAtt('a'), person.getAtt('g'), person.getAtt('i'), "ECE")

studentList = [student, student0, student1]

print("\n")
for s in studentList:
    print(s)
