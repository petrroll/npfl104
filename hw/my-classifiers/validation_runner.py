import pandas as pd

# cuts pd dataframe into two numpy arrays, one with features the other with targets
def prepare_data(data, target_col='target'):
    features = pd.get_dummies(data.drop(target_col, axis=1)).values
    targets = data[target_col].cat.codes

    return (features, targets)


def run(train, test, target_col, model):
    # prepare data in np.array formats
    train_i, train_t = prepare_data(train, target_col) 
    test_i, test_t = prepare_data(test, target_col) 

    # build model
    model.Build(train_i, train_t)

    # test model
    succ = 0
    tests_len = len(test_i)
    for i in range(tests_len):
        if model.Predict(test_i[i]) == test_t[i]:
            succ += 1
        if (i % 1000 == 999):
            print(succ/(i+1))
    return succ / tests_len