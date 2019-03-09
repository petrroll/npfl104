from models.knn import KNN
from dta_loader import load_adult, load_synth_sep, load_synth_noise
from validation_runner import run

a_train, a_test = load_synth_noise()
print(run(a_train, a_test, 'target', KNN, k=3))

a_train, a_test = load_synth_sep()
print(run(a_train, a_test, 'target', KNN, k=3))