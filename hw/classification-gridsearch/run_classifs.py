import numpy as np
import pandas as pd

import os
import seaborn as sns

from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

# Loads dataset & processes it:
# - fills NA data
# - processes categorical data so that categories from both train&test are known
def load_dataset(dataset, drop_columns=None):
    df_train = pd.read_csv("./2019-npfl104-shared/data/"+dataset+"/train.txt.gz", header=None)
    df_test = pd.read_csv("./2019-npfl104-shared/data/"+dataset+"/test.txt.gz", header=None)

    train_size = len(df_train)
    df_tog = df_train.append(df_test)

    # Convert to categorical
    for col in df_tog.columns[np.where(df_tog.dtypes == 'object')]:
        df_tog[col] = pd.Categorical(df_tog[col])

        
    # Explicitely drop specified columns
    if drop_columns:
        df_tog = df_tog.drop(drop_columns, axis=1)


    df_train, df_test = df_tog[:train_size], df_tog[train_size:]
    
    df_train = df_train.fillna(df_train.mode().iloc[0])
    df_test = df_test.fillna(df_test.mode().iloc[0])
    
    return df_train, df_test

# Used to split dataframe to features & target (last column)
def get_X(df):
    return pd.get_dummies(df[df.columns[:-1]], dummy_na=True)
def get_Y(df):
    dfc = df[df.columns[-1]]
    return dfc.cat.codes if dfc.dtype.name == "category" else dfc


dftr, dfte = load_dataset("pamap-easy")

classifiers = [
    (SVC(kernel="linear", C=1, gamma='scale'), "SVC", "l"),
    (SVC(kernel="poly", C=1, gamma='scale'), "SVC", "p"),
    (SVC(kernel="rbf", C=1, gamma='scale'), "SVC", "p"),
]

for cls, name in zip(classifiers, ["linear", "poly", "rbf"]):
    model, cls_name, cls_args = cls
        
    score = cross_val_score(model, get_X(dftr), get_Y(dftr), cv=5)  
    print("crossValTrain(" + name  + "): "+ str(score))

parameters = {
    'kernel':['rbf'], 
    'C':[0.1, 1, 10, 100, 1000, 10000], 
    'gamma': [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]
}

model = SVC(gamma='scale')
gs = GridSearchCV(model, parameters, cv=3, n_jobs=-2, return_train_score=True)
res = gs.fit(get_X(dftr), get_Y(dftr))
print("Best params: " +  str(res.best_params_))

heat_score = res.cv_results_['mean_test_score'].reshape(len(parameters['gamma']),len(parameters['C']))
fig = sns.heatmap(heat_score, annot=True, fmt=".4f", center = 0.8, xticklabels=parameters['gamma'], yticklabels=parameters['C'])
fig.set_xlabel("Gamma")
fig.set_ylabel("C")
fig.figure.savefig("heatmap.png")
print("Heatmap for GS saved in heatmap.png")

test_score = res.score(get_X(dfte), get_Y(dfte))
print("Score on test set: " + str(test_score))
