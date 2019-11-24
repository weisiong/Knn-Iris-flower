import os
import csv
import random

cwd = os.getcwd()
print(cwd)
fullfilename = cwd + '/proj02/iris.data'

def loadDataset(filename, split):   
    trainSet = []
    trainLabel = []
    testSet = []
    testLabel = []

    with open(filename,'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainSet.append(dataset[x][:3])
                trainLabel.append(dataset[x][4:])
            else:
                testSet.append(dataset[x][:3])
                testLabel.append(dataset[x][4:])

    return (trainSet,trainLabel),(testSet,testLabel)

(trainSet,trainLabel),(testSet,testLabel) = loadDataset(fullfilename,0.66)

print(trainLabel[:3])



