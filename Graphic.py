import matplotlib.pyplot as plt
import random

def showBoard(bestNeurons, labels, neuronNumber):
    plt.figure(5)
    for i in range(len(bestNeurons)):
        x = bestNeurons[i][0] + random.random()
        y = bestNeurons[i][1] + random.random()
        plt.plot(x, y, 'ro')
        plt.text(x, y, labels[i])
    plt.axis([-1,neuronNumber+1,-1,neuronNumber+1])
    plt.show()

def showCost(cost):
    plt.plot(cost, "b-")
    plt.show()