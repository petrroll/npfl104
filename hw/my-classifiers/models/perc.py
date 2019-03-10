import numpy as np
import pandas as pd
from models.model import *

class Perc(Model):
    '''
    Perceptron model, assumes only two target classes with values 0/1.
    '''
    def __init__(self, lr = 0.03):
        self.lr = lr

    def Build(self, inputs, targets):       
        dim = inputs.shape[1]

        # prepare weights + inputs array, prepend column of 1 for bias
        w = np.random.normal(loc = 0.0, scale = 1/dim, size = dim+1)
        b = np.insert(inputs, 0, values=1, axis=1) 

        # update weights for each input data
        for i in range(1, len(targets)):
            result = np.dot(b[i], w) > 0
            if result != targets[i]:
                w = w - self.lr * (w - b[i]) * (targets[i] - result) # w -= lr * (w-b[i]) * errorPolarity

        self.w = w

    def Predict(self, input):
        b = np.insert(input, 0, values=1, axis=0) 
        result = np.dot(b, self.w) > 0
        return result

