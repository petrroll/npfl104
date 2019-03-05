import numpy as np
import pandas as pd

import dta_utils as dta

def load_adult():
    return (dta.load_data("./adult/adult.data", [14], skiprows=1), dta.load_data("./adult/adult.test", [14], skiprows=1))

