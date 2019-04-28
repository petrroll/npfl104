import numpy as np
from models.model import Model

class KMeansMy(Model):
    '''
    KMeans clustering model.
    '''
    def __init__(self, k, iters):
        self.k = k
        self.iters = iters

        self.inertia_ = 25

    def Build(self, inputs):
        centers = self.__init_centers(inputs)
        for _ in range(self.iters):
            centers = self.__iteration(inputs, centers)
        self.centers = centers


    def __init_centers(self, inputs):
        x = inputs
        k = self.k

        centers = np.zeros((k, ) + x[0].shape)
        for i in range(k):
            random_i = np.random.choice(len(x) - 1, 1)[0]
            centers[i] = x[random_i]
                
        return centers

    def __get_closest_center(self, centers, data, j):
        closest = -1
        closest_dist = 2 ** 31
        for i in range(len(centers)):
            dist = np.linalg.norm(data[j] - centers[i])
            if (dist < closest_dist): 
                closest_dist = dist
                closest = i
        return closest


    def __iteration(self, data, centers):
        k = self.k

        aggr = np.zeros((k, ) + data[0].shape)
        aggr_n = np.zeros(k)

        for i in range(len(data)):
            clst_cluster = self.__get_closest_center(centers, data, i)

            aggr[clst_cluster] += data[i]
            aggr_n[clst_cluster] += 1

        for i in range(len(aggr)):
            aggr[i] /= aggr_n[i]

        return aggr



    def fit(self, data):
        self.Build(data)
        self.labels_ = self.Predict(data)

    def Predict(self, input):
        centers = self.centers
        data = input

        result = np.zeros(len(data))
        for i in range(len(data)):
            result[i] = self.__get_closest_center(centers, data, i)
        
        return result


