import numpy as np
from models.model import Model

class NaiveBayes(Model):
    '''
    Naïve bayes model, assumes only categorical features (continuous values need to be binned first).

    argmax_t: P(t|d) = P(t,d) / P(d) =P(d)isStaticAcrossT= P(t,d) = P(d|t)*P(t) =naive= TT_i{P(d_i|t)}*P(t)
    '''
    def __init__(self):
        pass
    
    def Build(self, inputs, targets):

        # compute P(t): first individual counts & they divide by number of datapoints
        # t_i -> P(t_i)
        prior = np.bincount(targets).astype('float64')
        prior /= np.sum(prior)

        # prepare some values
        classes_t = len(prior)
        columns = inputs.shape[1]

        # compute P(d_i|t) for each i
        # d_i_j -> [P(d_i=j|t_1), P(d_i=j|t_2), P(d_i=j|t_3), ..], one table for each i, size: |classes(d_i)|
        # P(d_i|t) is estimated using multinomial distribution from data: c(di=k, t=l) / c(t=l)
        
        # create conditional tables (|feature_i|, |target|) for each feature 
        cond = []
        classes_per_column = np.max(inputs, axis=0) + 1 # +1 because classes are 0-based
        cond = [np.zeros((classes, classes_t)) for classes in classes_per_column]

        # Compute counts for each cond: d_i_j -> c(d_i=j, t=1)
        for dta_i in range(len(targets)):
            t = targets[dta_i]
            for i in range(columns):
                j = inputs[dta_i, i]   
                cond[i][j, t] += 1

        # transform c(d_i=j, t=1) to P(d_i=j|t=1)
        for cond_t in cond:
            t_sum = np.sum(cond_t, axis=0) + 1 # smoothing
            for t in range(classes_t):
                cond_t[:,t] /= t_sum[t] 
                cond_t[:,t] += 1e-10        


        self.cond = cond
        self.prior = prior            

    def Predict(self, input):
        cond = self.cond
        prior = self.prior
        classes_t = cond[0].shape[1]

        res = np.ones(classes_t)
        for c in range(len(input)):
            res += np.log(cond[c][input[c]])

        res += np.log(prior)

        return np.argmax(res)
    