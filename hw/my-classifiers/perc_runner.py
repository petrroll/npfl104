from models.knn import KNN
from models.perc import Perc

from dta_loader import load_adult, load_synth_sep, load_synth_noise
from validation_runner import run

a_train, a_test = load_synth_noise()
print("Artif noise:\t", run(a_train, a_train, 'target', Perc(0.5, 0.95, 80)))

a_train, a_test = load_synth_sep()
print("Artif sep:\t", run(a_train, a_test, 'target', Perc(0.5, 0.9, 10)))

a_train, a_test = load_adult()
print("Adult:\t", run(a_train, a_test, 'target', Perc(0.025, 0.85, 20)))