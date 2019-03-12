from models.knn import KNN
from models.perc import Perc
from models.naive_bayes import NaiveBayes

from dta_loader import load_adult, load_synth_sep, load_synth_noise
from validation_runner import run

a_train, a_test = load_synth_noise()
print(run(a_train, a_train, 'target', NaiveBayes(), one_hot=False))

a_train, a_test = load_synth_sep()
print(run(a_train, a_test, 'target', NaiveBayes(), one_hot=False))

a_train, a_test = load_adult(False, 50)
print(run(a_train, a_test, 'target', NaiveBayes(), one_hot=False))