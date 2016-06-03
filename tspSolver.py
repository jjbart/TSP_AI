# Authors: Josiah Bartlett and Tom Joyce
# Purpose: Test and yield results for solving the TSP problem with 3 different algorithms

import random
import timeit
from graphGenerator import graphGenerator
from simannealing import SimAnnealingTSPGraph, SimAnnealingTSPAgent
from genetic import evolve


# Solving the Traveling Salesman problem with 3 different algorithms
def solve():

    # Create the weighted graph object used for all tests
    graphgen = graphGenerator(10, 20, 100)
    randomgraph = graphgen.wgraph


    # Greedy Algorithm testing
    # Does not require more than one run, as every run yields the same result and approximately the same time
    startgreedy = timeit.default_timer()
    greedyresult = randomgraph.greedytsp(0)
    elapsedgreedy = timeit.default_timer() - startgreedy
    print "Final length of Greedy TSP Tour:", greedyresult[1]
    # print "Final Greedy TSP Algorithm pathlist:", greedyresult[0]


    # Simulated Annealing Algorithm testing
    # Run 100 annealing sessions and return basic statistical
    # analysis of resulting tour lengths and time
    simannealdata = []
    simannealtimedata = []
    simnumruns = 100
    for i in range (simnumruns):
        startanneal = timeit.default_timer()
        graph = SimAnnealingTSPGraph(randomgraph)
        agent = SimAnnealingTSPAgent()
        bestgraph = graph
        count = 0
        shufflecount = 0
        while count < 10:
            if shufflecount >= 1:
                random.shuffle(tspgraph.pathlist)
            tspgraph = agent.anneal(graph)
            if tspgraph.graph.pathlength(tspgraph.pathlist) < bestgraph.graph.pathlength(bestgraph.pathlist):
                bestgraph = tspgraph
            count +=1
            shufflecount +=1
        simelapsed = timeit.default_timer() - startanneal
        simannealdata.append(bestgraph.graph.pathlength(bestgraph.pathlist))
        simannealtimedata.append(simelapsed)
        print "Final length of Simulated Annealing TSP Tour for run",i+1,":", bestgraph.graph.pathlength(bestgraph.pathlist)
        # print "Final Simulated Annealing TSP Algorithm path-list for run",i+1,":", bestgraph.pathlist


    # Genetic Algorithm testing
    # Run 100 instances of the genetic algorithm and return basic
    # statistical analysis of resulting tour lengths and time
    target_score = greedyresult[1]
    geneticdata = []
    genetictimedata = []
    gennumruns = 100
    for j in range (gennumruns):
        startgenetic = timeit.default_timer()
        genetictsp = evolve(randomgraph, target_score)
        print "Final length of Genetic TSP tour for run",j+1,":", genetictsp[1]
        # print "Final Genetic TSP tour path-list for run",j+1,":", genetictsp[0].pathlist
        geneticelapsed = timeit.default_timer() - startgenetic
        geneticdata.append(genetictsp[1])
        genetictimedata.append(geneticelapsed)


    print "========================================================"
    print "================== FINAL RESULTS ======================="
    print "========================================================"

    print "============= GREEDY ALGORITHM RESULTS ================="
    print "Minimum tour length:", greedyresult[1]
    print "Time elapsed:", elapsedgreedy, "seconds"
    print "========================================================"

    print "=========== SIMULATED ANNEALING RESULTS ================"
    print "Out of", simnumruns, "runs:"
    print "Minimum (best) value:", min(simannealdata)
    print "Mean value:", float(sum(simannealdata))/len(simannealdata)
    print "Range:", min(simannealdata), "to", max(simannealdata)
    print "Minimum (best) time:", min(simannealtimedata), "seconds"
    print "Mean time:", float(sum(simannealtimedata))/len(simannealtimedata), "seconds"
    print "Range of times:", min(simannealtimedata), "to", max(simannealtimedata), "seconds"
    print "========================================================"

    print "============== GENETIC ALGORITHM RESULTS ==============="
    print "Out of", gennumruns, "runs:"
    print "Minimum (best) value:", min(geneticdata)
    print "Mean value:", float(sum(geneticdata))/len(geneticdata)
    print "Range:", min(geneticdata), "to", max(geneticdata)
    print "Minimum (best) time:", min(genetictimedata), "seconds"
    print "Mean time:", float(sum(genetictimedata))/len(genetictimedata), "seconds"
    print "Range of times:", min(genetictimedata), "to", max(genetictimedata), "seconds"
    print "========================================================"

if __name__ == '__main__':
    solve()
