import math
class Cluster:
    mean = []
    hasChanged = False

    def __init__(self, mean):
        self.mean = mean
        self.clusterPoints = [[]]
    def addPoint(self, point):
        self.clusterPoints.append(point)
    def calcCentroid(self):
        sum = [0] * len(self.clusterPoints[0])
        for i in range(len(self.clusterPoints)):
            temp = self.clusterPoints[i]
            for j in range(len(temp)):
                sum[j] += temp[j]
        for k in range(len(sum)):
            sum[k] /= float(len(self.clusterPoints))

        self.mean = sum
        self.clusterPoints = [[]]
    def getMean(self):
        return self.mean