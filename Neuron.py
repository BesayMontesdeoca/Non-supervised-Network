import numpy as np

class Neuron:
    weight = []
    size = -1

    def __init__(self, size):
        self.weight = np.random.rand(size)
        self.size = size

    def getWeight(self):
        return self.weight

    def setWeight(self, newWeigt):
        self.weight = newWeigt

    def getSize(self):
        return self.size