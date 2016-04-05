# -*- coding: utf-8 -*-
import numpy as np
import math
import Graphic
from Neuron import Neuron
import Persistence
from copy import deepcopy

def initBoard(Nneruon, size):
    board = [Neuron(size) for i in range(Nneruon)]
    return board

def euclideanDistance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def logicDistance(X, Y):
    sum = 0
    for j in range(len(X)):
        sum += (X[j] - Y[j])**2
    return math.sqrt(sum)

def distance(X, board):
    distances = []
    for i in range(len(board)):
        aux = logicDistance(X, board[i].getWeight())
        distances.append(aux)
    return distances

def getBest(distances):
    minDis = float("Inf")
    pos = 0
    for i in range(len(distances)):
        if(distances[i] < minDis):
            minDis = distances[i]
            pos = i
    return pos

def getCoordenate(neuronNumber):
    x = []
    y = []
    contX = -1
    contY = 0
    for i in range(neuronNumber*neuronNumber):
        if(i%neuronNumber == 0): contX += 1
        x.append(contX)
        y.append(contY)
        if(contY == neuronNumber-1):
            contY = 0
        else:
            contY += 1
    return x, y

def uptdateEthaSigma(S, N, n):
    S = S * (math.exp((-n/T1)))
    N = N * (math.exp((-n/T2)))
    if (N < N_limit): N = N_limit
    if (S < S_limit): S = S_limit

def difWeight(board1, board2):
    s = 0
    for i in range(len(board1)):
        s += logicDistance(board1[i].getWeight(), board2[i].getWeight())
    return s

def train(board, trX):
    [x, y] = getCoordenate(int(np.sqrt(len(board))))
    prev = deepcopy(board)
    costV = []
    for n in range(nIterations):
        print("Iteracion: {}".format(n))
        for i in range(len(trX)):
            distances = distance(trX[i], board)
            best = getBest(distances)
            uptdateEthaSigma(S, N, n)
            for j in range(len(board)):
                d = euclideanDistance(x[best], y[best], x[j], y[j])
                h = np.exp((-1*(d**2))/(2*(S**2)))
                board[j].setWeight(board[j].getWeight() + N*h*(trX[i]-board[j].getWeight()))
        cost = difWeight(prev, board)
        print("Cost: {}".format(cost))
        costV.append(cost)
        prev = deepcopy(board)
    bestNeurons = []
    for i in range(len(trX)):
        index = getBest(distance(trX[i], board))
        bestNeurons.append((x[index], y[index]))
    return bestNeurons, costV


trX, labels = Persistence.getTrxPaises()
# #Parameters
neuronNumber = 20    #neuronNumber^2
nIterations = 100
S = neuronNumber/2
N = 0.001
N_limit = 0.01
S_limit = 1
T1 = nIterations*len(trX)/math.log(S)
T2 = T1

board = initBoard(neuronNumber*neuronNumber, len(trX[0]))
bestNeurons, costV = train(board, trX)
Graphic.showCost(costV)
Graphic.showBoard(bestNeurons, labels, neuronNumber)

