import numpy as np
import pandas as pd

def replace_with_categorical_int(data, indexes):
    for i in indexes:
        data[i] = data[i].astype('category').cat.codes

def onehot_categorical_data(data):
    transformed_columns = []
    for i in data.columns:
        col = data[i]
        if col.dtype == 'object':
            res = pd.get_dummies(col.astype('category'), prefix=str(i))
        else:
            res = col
        transformed_columns.append(res)

    return pd.concat(transformed_columns, axis=1)

def load_data(path, to_categorical_int, skiprows):
    data = pd.read_csv(path, header=None, skiprows=skiprows)
    replace_with_categorical_int(data, to_categorical_int) # 14 is the target variable -> classId
    data_enc = onehot_categorical_data(data)

    return data_enc.values