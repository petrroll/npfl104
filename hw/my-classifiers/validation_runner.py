import pandas as pd

def run(train, test, target_col, model_constructor, **model_args):
    # prepare data in np.array formats
    train_i = pd.get_dummies(train.drop(target_col, axis=1)).values
    train_t = train[target_col].cat.codes

    test_i = pd.get_dummies(test.drop(target_col, axis=1)).values
    test_t = test[target_col].cat.codes

    # create & build model
    model = model_constructor(**model_args)
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