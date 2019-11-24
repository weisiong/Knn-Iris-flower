import os
import csv
import random
import math

cwd = os.getcwd()
print(cwd)
fullfilename = cwd + '/proj02/iris.data'

def loadDataset(filename, split):   
    trainSet = []
    testSet = []
    with open(filename,'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainSet.append(dataset[x])
            else:
                testSet.append(dataset[x])
    return trainSet,testSet

trainSet,testSet = loadDataset(fullfilename,0.66)


def euclideanDistance(instance1,instance2,length):
    distance=0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]),2)
    return math.sqrt(distance)

# the most similar neighbors
def getNearestNeighbors(train, test_row, num_neighbors):
    leng = len(test_row) - 1
    distances = list()
    for train_row in train:
        dist = euclideanDistance(test_row, train_row, leng)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors

# Make a classification prediction with neighbors
def predict_classification(neighbors):
	output_values = [row[-1] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction

sample = [4.7, 3.2, 5.6, 1.2]
neighbors = getNearestNeighbors(trainSet,sample,3)
prediction = predict_classification(neighbors)

print(prediction)

