import random
import math
import string

class Archer:
    def __init__(self, idNum, parentidNum=[-1,-1]):
        self.id = idNum
        self.fitness = -1
        self.position = (0,0)
        self.initialVelocity = round(random.uniform(0.0, 50.0), 1)     #Newtons nearest tenth
        self.angle = round(random.uniform(0.0, 90.0), 1)    #angle from +x axis to +y axis nearest tenth
        self.parentid = [parentidNum[0], parentidNum[1]]

    def shoot(self, endX):
        velocityX = self.initialVelocity*math.cos(self.angle)
        velocityY = self.initialVelocity*math.sin(self.angle)
        time = endX/velocityX                                   #time it takes to reach endX
        endY = (-4.9*(time**2)) + (velocityY*time) + self.position[1]
        impactVelocity = 0                                      #Implement impact velocity to increase fitness factor later
        return endY

    def __str__(self):
        creatureStr = 'ID: ' + str(self.id) + ' Fit: ' + str(self.fitness) + ' Vo,Angle: ' + str(self.initialVelocity) + ',' + str(self.angle) + ' ParentsID: ' + str(self.parentid[0]) + ',' + str(self.parentid[1])
        return creatureStr

targetX = 100
targetY = 35
marginY = 20
population = 16
generations = 10000
fit = 99
random.seed(2)
uniqueID = 0

def geneAlgo():
    archers = bigBang(population)

    for generation in range(generations):   #potentially give each generation attributes of different areas to target
        archers = evaluate(archers)         #evaluates fitness of archers
        archers = selection(archers)        #kills of individuals with lowest fitness (to be replaced in crossover)
        archers = crossover(archers)        #parents pass genes down to children for next generation
        archers = mutation(archers)         #potential mutations per each individual per generation

        if any(archer.fitness >= fit for archer in archers):
            print('Found a creature with target fitness')
            print('\n' + str(archers[0]))
            exit(0)

def bigBang(pop):
    firstGenArchers = []
    global uniqueID

    for _ in range(population):
        firstGenArchers.append(Archer(uniqueID))
        uniqueID += 1
    return firstGenArchers

def evaluate(archers):
    global targetX
    global targetY

    for archer in archers:
        actualY = archer.shoot(targetX)
        print("ActualY is " + str(actualY))
        a = targetY - marginY
        b = targetY + marginY
        if actualY < 0:
            rawFit = -1
        elif actualY >= 0 and actualY <= a:
            rawFit = 1
        elif actualY >= a and actualY <= b:
            rawFit = 100-abs(100*((actualY-targetY)/(targetY)))
        elif actualY >= b:
            rawFit = -1
        else:
            pass
        archer.fitness = round(rawFit, 2)
    return archers

def selection(archers):
    archers = sorted(archers, key=lambda archer: archer.fitness, reverse=True)
    print('\n'.join(map(str, archers)))
    archers = archers[:int(.2 * len(archers))]
    return archers

def crossover(archers):
    global uniqueID
    offspring = []
    for _ in range((population - len(archers))/2):
        parent1 = random.choice(archers)
        parent2 = random.choice(archers)
        while parent1.id == parent2.id:
            print("Same Parent Detected! with ID: " + str(parent1.id))
            parent2 = random.choice(archers)
        child1 = Archer(uniqueID, [parent1.id, parent2.id])
        uniqueID += 1
        child2 = Archer(uniqueID, [parent1.id, parent2.id])
        uniqueID += 1

        #child1 gets the initial velocity of the parent with random angle
        #child2 gets the angle of the parent with random initial velocity
        child1.initialVelocity = parent1.initialVelocity
        child2.angle = parent2.angle
        offspring.append(child1)
        offspring.append(child2)
    archers.extend(offspring)
    return archers

def mutation(archers):
    #right now all the traits being passed down are not erased
    #set mutations to occur at probablity p for any trait of the children
    pass
    return archers

if __name__ == '__main__':
    geneAlgo()
