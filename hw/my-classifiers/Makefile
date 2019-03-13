# Based on: https://blog.horejsek.com/makefile-with-python/
VENV_NAME?=env
PYTHON=$(VENV_NAME)/bin/python
PYTHON_GLOBAL=python3

ALGS=perc nb knn

# Alg runners
all: $(ALGS)

$(ALGS): download $(VENV_NAME)
	$(PYTHON) $(@)_runner.py

# Data download
artificial_objects:
	wget https://ufal.mff.cuni.cz/~zabokrtsky/courses/npfl104/data/classification/artificial_objects.tgz
	tar -xvz --one-top-level -f artificial_objects.tgz
	rm -r artificial_objects.tgz

adult:
	wget -r -nH --cut-dirs=2 --no-parent --reject="index.html*" http://archive.ics.uci.edu/ml/machine-learning-databases/adult/

download: adult artificial_objects

clean_download:
	rm -r artificial_objects
	rm -r adult


# ENV
$(VENV_NAME): requirements.txt
	@test -d $(VENV_NAME) || $(PYTHON_GLOBAL) -m venv $(VENV_NAME)
	$(PYTHON) -m pip install -r requirements.txt

clean_$(VENV_NAME): 
	rm -r $(VENV_NAME)

# Common:
clean_pycache:
	rm -r __pycache__
	rm -r models/__pycache__

clean: clean_$(VENV_NAME) clean_download clean_pycache


