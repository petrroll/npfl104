import numpy as np
import pandas as pd

import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression

# Loads dataset & processes it:
# - fills NA data
# - processes categorical data so that categories from both train&test are known
def load_dataset(dataset, drop_columns):
    df_train = pd.read_csv("./2019-npfl104-shared/data/"+dataset+"/train.txt.gz", header=None)
    df_test = pd.read_csv("./2019-npfl104-shared/data/"+dataset+"/test.txt.gz", header=None)

    train_size = len(df_train)
    df_tog = df_train.append(df_test)

    # Convert to categorical
    for col in df_tog.columns[np.where(df_tog.dtypes == 'object')]:
        df_tog[col] = pd.Categorical(df_tog[col])

    # Drop too unique columns e.g. ids
    for col in df_tog.columns:
        idlike_col = []
        if df_tog[col].nunique() > 0.6 * len(df_tog):
            idlike_col.append(col)
    df_tog = df_tog.drop(idlike_col, axis=1)
        
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

# Creates classifiers & their description 
def create_classifiers():
    return [
        (KNeighborsClassifier(3), "KNeighborsClassifier", "k=3"),
        #(SVC(kernel="linear", C=0.025), "SVC", "kernel=\"linear\", C=0.025"),
        #SVC(gamma=2, C=1),
        #GaussianProcessClassifier(1.0 * RBF(1.0)),
        (DecisionTreeClassifier(max_depth=5), "DecisionTreeClassifier", "max_depth=5"),
        (RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1), "RandomForestClassifier", "max_depth=5, n_estimators=10, max_features=1"),
        #(MLPClassifier(), "MLPClassifier", "default"),
        (AdaBoostClassifier(), "AdaBoostClassifier", "default"),
        (GaussianNB(), "GaussianNB", "default"),
        (LogisticRegression(multi_class='auto', solver='lbfgs'), "LogisticRegression", "multi_class='auto', solver='lbfgs'")
        #QuadraticDiscriminantAnalysis()
    ]

# Runs classifier and outputs result in appropriate format
def run_classifiers(df_train, df_test, dtset_args):
    for cls in create_classifiers():
        model, cls_name, cls_args = cls
        
        # Fit and score model with given data
        model = model.fit(get_X(df_train), get_Y(df_train))
        score = model.score(get_X(df_test), get_Y(df_test))
        
        # Produce report string (I'd much rather use f strings but need to support older python)
        dtset_name, dtset_comm = dtset_args
        print(dtset_name + "\t" + cls_name  + "\t" + "{:.2f}".format(score*100) + "\t" + "Petr H." + "\t" + ", ".join([dtset_comm, cls_args]) )

# Runs specified datasets (auguments them with universal comment)
def run_def_datasets(dtsets):
    datasets = [ (dtset, "ORIGFEATS, ONEHOT") for dtset in dtsets ]
    
    for dtst in datasets:
        dtset_name, _ = dtst
        drop_columns =  None if dtset_name != "czech-car-accidents" else [4]    # Drop datum+time column else onehot explosion 
        df_train, df_test = load_dataset(dtset_name, drop_columns)              #TODO: Config based dropping
        run_classifiers(df_train, df_test, dtst)

def main():
    dtsets = os.listdir("./2019-npfl104-shared/data/")
    run_def_datasets(dtsets)

main()