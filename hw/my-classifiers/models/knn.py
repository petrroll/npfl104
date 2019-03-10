import numpy as np
from models.model import Model

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

        self.dist_comp_buffer = np.zeros(self.inputs.shape)
        self.dist_buffer = np.zeros(self.inputs.shape[0])

    def Predict(self, input):
        data = self.inputs
        dist_comp_buffer = self.dist_comp_buffer
        dist_buffer = self.dist_buffer

        # Compute differences in individual dimensions
        np.subtract(data, input, out=dist_comp_buffer) 

        # Weight differences in indiv dimensions
        if self.dim_weights is not None:
            np.multiply(dist_comp_buffer, self.dim_weights, out=dist_comp_buffer)   

        # Square dimension differences (eucledian distance)
        np.square(dist_comp_buffer, out=dist_comp_buffer)
        
        # Compute distances (sum of ^2 dimension differences)
        np.sum(dist_comp_buffer, axis=1, out=dist_buffer) 

        # Get indices of k nearest neighbours & their targets  
        knn_i = np.argpartition(dist_buffer, self.k - 1)[:self.k]         
        knn = self.targets[knn_i]
        
        if self.dist_w:
            knn_dw = 1/dist_buffer[knn_i]      # Distance weight for each knn target variable
            return np.argmax(np.bincount(knn, knn_dw))
        else:
            return np.argmax(np.bincount(knn))


