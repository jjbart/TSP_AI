# Authors: Josiah Bartlett and Thomas Joyce
# Purpose: evolving weighted graphs to solve TSP

import random

class GeneticTSPGraph(object):

    # @param graph: a weighted graph with a randomly shuffled pathlist
    def __init__(self, graph):
        self.graph = graph
        self.pathlist = graph.vertices()
        random.shuffle(self.pathlist)
        self.fit = self.fitness()


    # @return: a fitness score for this weighted graph tour
    def fitness(self):
        return self.graph.pathlength(self.pathlist)


    # @param other: another GeneticTSPGraph
    # @return: a new GeneticTSPGraph generated via crossover
    def cross(self, other):
        if random.random() < 0.5:
            parent1 = self.pathlist
            parent2 = other.pathlist
        else:
            parent1 = other.pathlist
            parent2 = self.pathlist

        offspring = GeneticTSPGraph(self.graph)

        if random.random() < 0.5:
            offspring.pathlist[0:len(self.pathlist)/2] = parent1[0:len(self.pathlist)/2]

            count = len(self.pathlist)/2
            for i in parent2:
                if i not in parent1[0:len(self.pathlist)/2]:
                    offspring.pathlist[count] = i
                    count +=1

        else:
            offspring.pathlist[len(self.pathlist)/2:] = parent1[len(self.pathlist)/2:]

            count = 0
            for i in parent2:
                if i not in parent1[len(self.pathlist)/2:]:
                    offspring.pathlist[count] = i
                    count +=1

        return offspring


    # Make a small random change to this weighted graph tour
    #@param mutationRate: use the mutation rate set inside the evolve function
    def mutate(self, mutationRate):
        for i in range(len(self.pathlist)-1):
            if random.random() < mutationRate:
                temp = self.pathlist[i]
                self.pathlist[i] = self.pathlist[i+1]
                self.pathlist[i+1] = temp

        self.fit = self.fitness()

        '''
        swap = False
        vertexlistlength = len(self.pathlist)
        while swap == False:
            x = random.randrange(vertexlistlength)
            y = random.randrange(vertexlistlength)
            if x != y:
                temp = self.pathlist[x]
                self.pathlist[x] = self.pathlist[y]
                self.pathlist[y] = temp
                swap = True
        '''

class Population(object):

    # Set up an empty population
    def __init__(self):
        self.population = []

    # @param solution: to add to this population
    def addSolution(self, solution):
        for i in range(solution.fit):
            self.population.append(solution)


    # @return: a solution chosen randomly in proportion to fitness
    def select(self):
        rand = random.randint(0,len(self.population)-1)
        return self.population[rand]

    # @return: the current number of solutions
    def size(self):
        return len(self.population)

    # @return: the highest-fitness solution
    def best(self):
        bestfitness = self.population[0]
        for i in range(len(self.population)):
            if bestfitness.fit >= self.population[i].fit:
                bestfitness = self.population[i]

        return bestfitness

    # @return: the fitness of the best solution
    def score(self):
        best = self.best()
        return best.fit

# Genetic algorithm
# @param graph: a weighted graph
# @param target_score: the tour length that this algorithm is trying to achieve or beat (be less than)
def evolve(graph, target_score):

    # Parameters
    population_size = 100
    mutation_rate = 0.05

    # Initial population
    population = Population()

    # Fill up the population with GeneticTSPGraph objects
    while population.size() < population_size:
        population.addSolution(GeneticTSPGraph(graph))

    # Look for an acceptable solution
    generations = 1
    while population.score() > target_score:
        nextgen = Population()

        # Cutoff point for number of generations
        if generations > 100000:
            break

        # Fill the next generation
        while nextgen.size() < population_size:
            mother = population.select()
            father = population.select()
            child = mother.cross(father)
            child.mutate(mutation_rate)
            nextgen.addSolution(child)

        population = nextgen
        generations += 1

    return (population.best(), population.score())

"""
if __name__ == '__main__':
    evolve()
"""
