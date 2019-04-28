# Based on: https://blog.horejsek.com/makefile-with-python/
VENV_NAME?=env
PYTHON=$(VENV_NAME)/bin/python
PYTHON_GLOBAL=python3

ALGS=regression

# Alg runners
all: $(ALGS)

$(ALGS): download $(VENV_NAME)
	$(PYTHON) $(@)_runner.py

# Data download
pragueestateprices:
	mkdir $@
	wget -P $@ https://ufal.mff.cuni.cz/~zabokrtsky/courses/npfl104/data/regression/pragueestateprices_train.tsv
	wget -P $@ https://ufal.mff.cuni.cz/~zabokrtsky/courses/npfl104/data/regression/pragueestateprices_test.tsv 


artificial:
	mkdir $@
	wget -P $@ https://ufal.mff.cuni.cz/~zabokrtsky/courses/npfl104/data/regression/artificial_2x_train.tsv
	wget -P $@ https://ufal.mff.cuni.cz/~zabokrtsky/courses/npfl104/data/regression/artificial_2x_test.tsv

download: pragueestateprices artificial

clean_download:
	rm -r artificial
	rm -r pragueestateprices

# ENV
$(VENV_NAME): requirements.txt
	@test -d $(VENV_NAME) || $(PYTHON_GLOBAL) -m venv $(VENV_NAME)
	$(PYTHON) -m pip install -r requirements.txt

clean_$(VENV_NAME): 
	rm -rf $(VENV_NAME)

# Common:
clean_pycache:
	rm -rf __pycache__
	rm -rf models/__pycache__

clean: clean_$(VENV_NAME) clean_download clean_pycache


