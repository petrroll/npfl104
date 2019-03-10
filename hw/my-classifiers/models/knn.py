import numpy as np
import pandas as pd
from models.model import *

class KNN(Model):
    '''
    Naive knn model with linear scaning of training data.
    '''
    def __init__(self, k, dim_weights = None, dist_w = False):
        self.k = k
        self.dim_weights = dim_weights
        self.dist_w = False

    def Build(self, inputs, targets):
        self.inputs = inputs
        self.targets = targets

    def Predict(self, input):
        diffs = np.abs(self.inputs - input) # Create difference to each training data instance
        if self.dim_weights is not None:    # Weight differences in indiv dimensions
            diffs *= self.dim_weights
        dist = np.sum(diffs * diffs, axis=1) # Compute distances (sum of ^2 dimension differences)
        
        knn_i = np.argpartition(dist, self.k - 1)[:self.k]    # Get indices of k neighbours
        
        knn = self.targets[knn_i]   # Knn target variables
        
        if self.dist_w:
            knn_dw = 1/dist[knn_i]      # Distance weight for each knn target variable
            return np.argmax(np.bincount(knn, knn_dw))
        else:
            return np.argmax(np.bincount(knn))


