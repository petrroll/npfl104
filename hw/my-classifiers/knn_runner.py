from models.knn import KNN
from dta_loader import load_adult, load_synth_sep, load_synth_noise
from validation_runner import run
import time

a_train, a_test = load_synth_noise()
print("Artif noise:\t", run(a_train, a_test, 'target', KNN(k=3)))

a_train, a_test = load_synth_sep()
print("Artif sep:\t", run(a_train, a_test, 'target', KNN(k=3)))

a_train, a_test = load_adult(True, 0)
print("Adult:\t", run(a_train, a_test, 'target', KNN(k=5)))
