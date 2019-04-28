import numpy as np
import pandas as pd

class Model():
    def Build(self, inputs, targets):
        raise NotImplementedError()
    
    def Predict(self, input):
        raise NotImplementedError()
