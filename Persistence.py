import csv
import numpy as np

def getTrxPaises():
    labels = []
    data = []
    reader = csv.reader(open("Database/Paises.csv", "rb"), delimiter=';')

    for index, row in enumerate(reader):
        v = [float(row[i]) for i in range(1, len(row))]
        data.append(v)
        labels.append([row[0]])

    return np.array(data), labels

def getTrxPaisesFull():
    labels = []
    data = []
    reader = csv.reader(open("Database/PaisesFull.csv", "rb"), delimiter=';')

    for index, row in enumerate(reader):
        v = [float(row[i]) for i in range(1, len(row))]
        data.append(v)
        labels.append([row[0]])

    return np.array(data), labels
