import numpy as np
import pandas as pd

def load_adult():
    # dta description
    types = {
        'age': 'int64',
        'workclass': 'object', # Never-worked not in data
        'fnlwgt': 'int64',
        'education': 'object',
        'education-num': 'int64',
        'marital-status': 'object',
        'occupation': 'object',
        'relationship': 'object',
        'race': 'object',
        'sex': 'object',
        'capital-gain': 'int64',
        'capital-loss': 'int64',
        'hours-per-week': 'int64',
        'native-country': 'object',
        'target': 'object'
    }

    names = list(types.keys())

    # load data
    train = pd.read_csv('./adult/adult.data', names=names, na_values="?", dtype=types, index_col=False, skipinitialspace=True)
    test = pd.read_csv('./adult/adult.test', names=names, na_values="?", dtype=types, index_col=False, skipinitialspace=True, skiprows=1)

    # merge data so that we have info about all potential classes & can process everything at once
    train_size = len(train)
    tog = train.append(test)

    # clean data
    tog['target'] = tog['target'].str.rstrip('.')

    # change object (string) columns to category type
    for col in tog.columns[np.where(tog.dtypes == 'object')]:
        tog[col] = pd.Categorical(tog[col])


    return (tog[:train_size], tog[train_size:])

def load_synth(name_base):
    # dta description
    types = {
        "size": "object",
        "color": "object",
        "type": "object",
        "target": "object",
    }

    names = list(types.keys())

    # load data
    train = pd.read_csv(f'./artificial_objects/{name_base}_train.csv', names=names,     dtype=types, index_col=False, skipinitialspace=True)
    test = pd.read_csv(f'./artificial_objects/{name_base}_test.csv', names=names,   dtype=types, index_col=False, skipinitialspace=True)

    # merge data so that we have info about all potential   classes & can process everything at once
    train_size = len(train)
    tog = train.append(test)

    # change object (string) columns to category type
    for col in tog.columns[np.where(tog.dtypes ==   'object')]:
        tog[col] = tog[col].astype('category')

    return (tog[:train_size], tog[train_size:])

def load_synth_sep():
    return load_synth('artificial_separable')

def load_synth_noise():
    return load_synth('artificial_with_noise')