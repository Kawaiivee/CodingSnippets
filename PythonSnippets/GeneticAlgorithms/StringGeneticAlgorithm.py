from fuzzywuzzy import fuzz
import random
import string
import time

class Creature:
    def __init__(self, length, id=-1, parents=[0, 0]):
        self.string = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        self.fitness = -1
        self.myParents = [parents[0], parents[1]]
        self.myid = id

    def __str__(self):
        return 'String: ' + str(self.string) + ' Fitness: ' + str(self.fitness) + ' ID: ' + str(self.myid) + ' My parents IDs are: ' + str(self.myParents[0]) + ' and ' + str(self.myParents[1])

in_str = None
in_str_len = None
population = 20
spawn = population
generations = 10000
fit = 95
random.seed(0)

def geneAlgo(spawn):
    creatures = init_creatures(population, in_str_len, spawn)

    for generation in range(generations):
        print('Generation: ' + str(generation))

        creatures = fitness(creatures)
        creatures = selection(creatures)
        creatures = crossover(creatures, spawn)
        creatures = mutation(creatures)

        spawn += population
        if any(creature.fitness >= fit for creature in creatures):
            print('Found a creature with target fitness')
            print('\n' + str(creatures[0]))
            exit(0)

def init_creatures(population, length, spawnNum):
    firstGenCreatures = []
    i = 0
    for _ in range(spawnNum):
        firstGenCreatures.append(Creature(length, i, [-1,-1]))
        i += 1
    return firstGenCreatures

def fitness(creatures):
    for creature in creatures:
        creature.fitness = fuzz.ratio(creature.string, in_str)
    return creatures

def selection(creatures):
    creatures = sorted(creatures, key=lambda creature: creature.fitness, reverse=True)
    print('\n'.join(map(str, creatures)))
    creatures = creatures[:int(0.2 * len(creatures))]
    return creatures

def crossover(creatures, spawnNum):
    offspring = []
    for _ in range((population - len(creatures)) // 2):
        parent0 = random.choice(creatures)
        parent1 = random.choice(creatures)
        while parent1 == parent0:
            parent1 = random.choice(creatures)
            print("Same parent chosen. Giving child second parent")

        child1 = Creature(in_str_len, spawnNum, [parent0.myid, parent1.myid])
        spawnNum += 1
        child2 = Creature(in_str_len, spawnNum, [parent0.myid, parent1.myid])
        spawnNum += 1

        split = random.randint(0, in_str_len)
        child1.string = parent0.string[0:split] + parent1.string[split:in_str_len]
        child2.string = parent1.string[0:split] + parent0.string[split:in_str_len]
        offspring.append(child1)
        offspring.append(child2)

    creatures.extend(offspring)
    return creatures

def mutation(creatures):
    for creature in creatures:
        for idx, param in enumerate(creature.string):
            if random.uniform(0.0, 1.0) <= 0.1:
                creature.string = creature.string[0:idx] + random.choice(string.ascii_letters) + creature.string[idx+1:in_str_len]
    return creatures

if __name__ == '__main__':
    in_str = 'aa'
    in_str_len = len(in_str)
    geneAlgo(spawn)
