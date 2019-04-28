import pandas as pd
import numpy as np
from models.linregress import LinRegression

def get_artif():
    train = pd.read_csv('./artificial/artificial_2x_test.tsv', names=['x', 'target'], index_col=None, header=None, sep='\t')
    test = pd.read_csv('./artificial/artificial_2x_train.tsv', names=['x', 'target'], index_col=None, header=None, sep='\t')

    return (train, test)


def get_prague():
    names = ['area', 'construction', 'ownership',   'status', 'floor', 'equip', 'cellar',     'balcony', 'target', 'nth']
    train = pd.read_csv('./pragueestateprices/pragueestateprices_train.tsv', index_col=None,     names=names, header=None, sep='\t')
    test = pd.read_csv('./pragueestateprices/pragueestateprices_test.tsv', index_col=None,  names=names, header=None, sep='\t')


    train_size = len(train)
    tog = train.append(test)

    for col in tog.columns[np.where(tog.dtypes ==   'object')]:
        tog[col] = pd.Categorical(tog[col])

    tog = tog.drop('nth', axis=1)

    train, test = (tog[:train_size], tog[train_size:])

    return (train, test)

def get_X(df):
    return pd.get_dummies(df[df.columns[:-1]])

def get_Y(df):
    return df[df.columns[-1]]

def evaluate_model(model, test):
    x_test = get_X(test).values
    y_test = get_Y(test).values

    err = 0
    for i in range(0, len(test)):
        err += (model.Predict(x_test[i]) - y_test[i]) ** 2

    err /= len(test)
    return err

def report(name, mse, r2):
    print(name + "\t" + "MSE: " + str(mse) + "\t sqrt(MSE): " + str(mse ** (1/2)) + "\t R2: " + str(r2))


def run_model(dta, name):
    train, test = dta

    model = LinRegression(epochs = 1000, lr = 0.0001)
    model.Build(get_X(train).values, get_Y(train).values)

    mse = evaluate_model(model, test)
    tse = (((get_Y(test) - get_Y(test).mean()) ** 2).sum() / len(test)) 
    r2 = 1-(mse/tse)
    
    report(name, mse, r2)

if __name__ == "__main__":
    run_model(get_prague(), "prague")
    run_model(get_artif(), "artif")


