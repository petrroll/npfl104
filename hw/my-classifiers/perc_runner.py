from models.knn import KNN
from models.perc import Perc

from dta_loader import load_adult, load_synth_sep, load_synth_noise
from validation_runner import run

a_train, a_test = load_synth_noise()
print(run(a_train, a_test, 'target', Perc(0.05, 0.995, 1000)))

a_train, a_test = load_synth_sep()
print(run(a_train, a_test, 'target', Perc(0.05, 0.995, 1000)))

a_train, a_test = load_adult()
print(run(a_train, a_test, 'target', Perc(0.05, 0.85, 20)))