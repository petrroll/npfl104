import pandas as pd
import numpy as np

from sklearn.linear_model import ARDRegression
from sklearn.linear_model import HuberRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR

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

def create_models():
    return [
        (ARDRegression(n_iter = 10000), "ARD"),
        (HuberRegressor(), "Huber"),
        (LinearRegression(normalize=False), "LR"),
        (KNeighborsRegressor(n_neighbors=5), "KNN"),
        (DecisionTreeRegressor(max_depth=10, min_samples_split=5,min_samples_leaf=3), "Tree"),
        #SVR()
    ]

def R2ToMSE(r2, df_test):
    score = (1-r2)
    score *= ((get_Y(df_test) - get_Y(df_test).mean()) ** 2).sum()
    
    return score/len(df_test)

def report(name, mse, r2):
    print(name + "\t" + "MSE: " + str(mse) + "\t sqrt(MSE): " + str(mse ** (1/2)) + "\t R2: " + str(r2))


def eval_dataset(data):
    df_train, df_test = data
    
    for (m, name) in create_models():
        m = m.fit(get_X(df_train), get_Y(df_train))
        r2 = m.score(get_X(df_test), get_Y(df_test))
    
        report(name,R2ToMSE(r2, df_test), r2)

if __name__ == "__main__":
    print("Prague:")
    eval_dataset(get_prague())
    print("Artif:")
    eval_dataset(get_artif())
