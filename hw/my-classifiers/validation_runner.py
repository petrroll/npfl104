import pandas as pd
import numpy as np

# TODO: Move one_hot encoding decision to data loading

# cuts pd dataframe into two numpy arrays, one with features the other with targets
def prepare_data(data, target_col='target', one_hot = True):
    if one_hot:
        features = pd.get_dummies(data.drop(target_col, axis=1)).values
    else:
        dta = data.drop(target_col, axis=1)
        for col in dta.columns[np.where(dta.dtypes == 'category')]:
            dta[col]  = dta[col].cat.codes
        features = dta.values

    targets = data[target_col].cat.codes
    return (features, targets)


def run(train, test, target_col, model, one_hot = True, print_acc_each=None):
    # prepare data in np.array formats
    train_i, train_t = prepare_data(train, target_col, one_hot) 
    test_i, test_t = prepare_data(test, target_col, one_hot) 

    # build model
    model.Build(train_i, train_t)

    # test model
    succ = 0
    tests_len = len(test_i)
    for i in range(tests_len):
        if model.Predict(test_i[i]) == test_t[i]:
            succ += 1
        if (print_acc_each is not None and i % print_acc_each == print_acc_each-1):
            print(i/tests_len, succ/(i+1))
    return succ / tests_len