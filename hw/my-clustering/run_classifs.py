import numpy as np
import pandas as pd

import os

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

def bench_k_means(estimator, name, data):
    t0 = time()
    estimator.fit(data)
    print('%-9s\t%.2fs\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'
          % (name, (time() - t0), estimator.inertia_,
             metrics.homogeneity_score(labels, estimator.labels_),
             metrics.completeness_score(labels, estimator.labels_),
             metrics.v_measure_score(labels, estimator.labels_),
             metrics.adjusted_rand_score(labels, estimator.labels_),
             metrics.adjusted_mutual_info_score(labels,  estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_,
                                      metric='euclidean',
                                      sample_size=sample_size)))

if __name__ == "__main__":
    from sklearn import metrics
    from time import time

    from sklearn.cluster import KMeans
    from models.kmeans import KMeansMy

    dftr, dfte = load_dataset("pamap-easy")

    labels = get_Y(dftr).values
    data = get_X(dftr).values    
    sample_size = len(dftr)

    def run_experiment(k):
        print("K=" + str(k))
        print('init\t\ttime\tinertia\thomo\tcompl\tv-meas\tARI\tAMI\tsilhouette')
        bench_k_means(KMeansMy(k, 5), "myKMEANS", data = get_X(dftr).values)
        bench_k_means(KMeans(init='k-means++', n_clusters=k, n_init=2), name="k-means++", data=data)
        bench_k_means(KMeans(init='random', n_clusters=k, n_init=2), name="random", data=data)

    run_experiment(10)
    run_experiment(25)
    run_experiment(35)




