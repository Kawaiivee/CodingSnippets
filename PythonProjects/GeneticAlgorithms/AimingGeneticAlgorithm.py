import random
import math
import string

class Archer:
    def __init__(self, idNum, fit=-1.0, parentidNum=[-1,-1]):
        self.id = idNum
        self.fitness = fit
        self.position = (0,0)
        self.initialVelocity = round(random.uniform(0.0, 50.0), 1)     #Newtons nearest tenth
        self.angle = round(random.uniform(0.0, 90.0), 1)    #angle from +x axis to +y axis nearest tenth
        self.parentid = [parentidNum[0], parentidNum[1]]

    def shoot(self, endX):
        velocityX = self.initialVelocity*math.cos(self.angle)
        velocityY = self.initialVelocity*math.sin(self.angle)
        time = endX/velocityX                                   #time it takes to reach endX
        endY = (-4.9*(time**2))+velocityY*time + self.position[1]
        impactVelocity = 0                                      #Implement impact velocity to increase fitness factor later
        return endY

    def __str__(self):
        creatureStr = 'ID: ' + str(self.id) + ' Fit: ' + str(self.fitness) + ' Vo,Angle: ' + str(self.initialVelocity) + ',' + str(self.angle) + ' ParentsID: ' + str(self.parentid[0]) + ',' + str(self.parentid[1])
        return creatureStr

targetX = 20.0
targetY = 12.0
population = 16
generations = 10000
fit = 90
random.seed(3)
uniqueID = 0

A1 = Archer(1)
print(A1)

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
        percentError = ((targetY-actualY)/(targetY))
        rawFit = 100*abs(1-percentError)                #fitness score is based on %error
        if rawFit > 100:
             rawFit = 0                                 #just die if you miss by too much
        elif rawFit < 0:
            rawFit = 0                                  #aka least fit will die
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
    offspring = []
    for _ in range((population - len(archers))/2):
        pass
    return archers

def mutation(archers):
    pass
    return archers

if __name__ == '__main__':
    geneAlgo()
