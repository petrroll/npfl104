import numpy as np
from models.model import Model

class Perc(Model):
    '''
    Perceptron model, assumes only two target classes with values 0/1.
    '''
    def __init__(self, lr = 0.03, lr_decay = 0.99, epochs = 2):
        self.lr = lr
        self.lr_decay = lr_decay
        self.epochs = epochs

    def Build(self, inputs, targets):       

        # prepare weights + inputs array, prepend column of 1 for bias
        dim = inputs.shape[1]
        w = np.random.normal(loc = 0.0, scale = 1/2, size = dim+1)
        b = np.insert(inputs, 0, values=1, axis=1) 

        lr = self.lr

        # calculate weights iteratively and save them, decay lr
        for _ in range(self.epochs):
            w = self.__update_weigts(b, targets, w, lr)
            lr *= self.lr_decay
        
        self.w = w


    def __update_weigts(self, b, targets, w, lr):

        # update weights for each input data
        for i in range(0, len(targets)):
            result = (np.dot(b[i], w) > 0)
            if result != targets[i]:
                w = w - lr * (w - b[i]) * (targets[i] - result) # w -= lr * (w-b[i]) * errorPolarity


        return w


    def Predict(self, input):
        b = np.insert(input, 0, values=1, axis=0) 

        result = (np.dot(b, self.w) > 0)
        return result

