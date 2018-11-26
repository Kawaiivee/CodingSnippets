import random
import math
import string

class Archer:
    def __init__(self, idNum, parentidNum=[-1,-1]):
        self.id = idNum
        self.fitness = -1
        self.position = (0,0)
        self.initialVelocity = round(random.uniform(1.1, 50.0), 1)     #Newtons nearest tenth
        self.angle = round(random.uniform(0.0, 90.0), 1)    #angle from +x axis to +y axis nearest tenth
        self.parentid = [parentidNum[0], parentidNum[1]]

    def shoot(self, endX):
        velocityX = self.initialVelocity*math.cos(math.radians(self.angle))
        velocityY = self.initialVelocity*math.sin(math.radians(self.angle))
        time = ((endX-self.position[0])/velocityX)                                   #time it takes to reach endX
        endY = (-4.9*(time**2)) + (velocityY*time) + self.position[1]
        impactVelocity = 0                                      #Implement impact velocity to increase fitness factor later
        return endY

    def __str__(self):
        creatureStr = 'ID: ' + str(self.id) + ' Fit: ' + str(self.fitness) + ' Vo,Angle: ' + str(self.initialVelocity) + ',' + str(self.angle) + ' ParentsID: ' + str(self.parentid[0]) + ',' + str(self.parentid[1])
        return creatureStr

targetX = 200            #with 'random.seed(2). a decent sized set is targetX = 10 and targetY = 5'
targetY = 10
marginY = .9*targetY    #you can be +- 90% from the target. all else, rawfit becomes 1
population = 16
generations = 10000
fit = 99.90     #threshold to termination
random.seed(3)  #deterministic
uniqueID = 0
tree = []

def geneAlgo():
    archers = bigBang(population)
    ancestors = []

    for generation in range(generations):   #potentially give each generation attributes of different areas to target
        print("Generation #" + str(generation))
        ancestors = track(ancestors, archers)
        archers = evaluate(archers)         #evaluates fitness of archers
        archers = selection(archers)        #kills of individuals with lowest fitness (to be replaced in crossover)
        archers = crossover(archers)        #parents pass genes down to children for next generation
        archers = mutation(archers)         #potential mutations per each individual per generation

        if any(archer.fitness >= fit for archer in archers):
            print('Found a creature with target fitness')
            print("\n" + "Our winner of science for the day is archer " + str(archers[0].id))
            print('\n' + str(archers[0]))
            input("\n\nHit Enter To Look At Whole Population\n\n")
            for archer in ancestors:
                print(archer)

            input("\n\nHit Enter To Look At Winner's Ancestor\n\n")
            ancestry(ancestors, archers[0])
            for ancestor in tree:
                print(str(ancestor))
            input("\n\nHit Enter To Exit")
            exit(0)

    print("Welp, the target was not able to be hit within " + str(generations) + " generations")

def track(ancestors, archers):    #basically appends all archers to the ancestors list while removing duplicates
    for archer in archers:
        if archer not in ancestors:
            ancestors.append(archer)
    return ancestors

def ancestry(ancestors, archer):
    global tree
    currParents = archer.parentid
    if currParents != [-1,-1]:
        if ancestors[archer.parentid[0]].id != -1 and ancestors[archer.parentid[1]].id != -1:
            if archer not in tree:
                tree.append(archer)
                ancestry(ancestors, ancestors[archer.parentid[0]])
                ancestry(ancestors, ancestors[archer.parentid[1]])
    else:
        pass

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
        print("Archer " + str(archer.id) + " shot at " + str(actualY))
        a = targetY - marginY
        b = targetY + marginY
        if actualY < 0:     #didn't even reach the target on the x-axis
            rawFit = -1
        elif actualY >= 0 and actualY < a:  #shot is low
            rawFit = 1
        elif actualY >= a and actualY <= b: #shot is close enough to actually be scored 'on the board'
            rawFit = 100-abs(100*((actualY-targetY)/(targetY)))
        elif actualY > b:                   #shot is high
            rawFit = 1
        else:                               #did I miss something?
            pass
        archer.fitness = round(rawFit, 2)
    print("\n")
    return archers

def selection(archers):
    archers = sorted(archers, key=lambda archer: archer.fitness, reverse=True)
    print('\n'.join(map(str, archers)))
    archers = archers[:int(.2 * len(archers))]
    return archers

def crossover(archers):
    global uniqueID
    offspring = []
    for _ in range((population - len(archers))//2):
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
    for archer in archers:
        mutVar = random.uniform(0.0, 1.0)
        if mutVar <= 0.05:
            print("INITVELOCITY Mutation for Archer " + str(archer.id))
            archer.initialVelocity = round(random.uniform(1.1, 50.0), 1)
        elif mutVar <= 0.10 and mutVar > 0.5:
            print("ANGLE Mutation for Archer " + str(archer.id))
            archer.angle = round(random.uniform(0.0, 90.0), 1)
        else:
            pass
    print("\n")
    return archers

if __name__ == '__main__':
    geneAlgo()
