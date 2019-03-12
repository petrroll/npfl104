from models.knn import KNN
from models.perc import Perc
from models.naive_bayes import NaiveBayes

from dta_loader import load_adult, load_synth_sep, load_synth_noise
from validation_runner import run


# Consider pure categorical instead of onehot for bayes 

a_train, a_test = load_synth_noise()
print(run(a_train, a_train, 'target', NaiveBayes()))

a_train, a_test = load_synth_sep()
print(run(a_train, a_test, 'target', NaiveBayes()))

a_train, a_test = load_adult(False, 50)
print(run(a_train, a_test, 'target', NaiveBayes()))