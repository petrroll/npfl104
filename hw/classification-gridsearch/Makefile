# Based on: https://blog.horejsek.com/makefile-with-python/
VENV_NAME?=env
PYTHON=$(VENV_NAME)/bin/python
PYTHON_GLOBAL=python3

run: 2019-npfl104-shared $(VENV_NAME)
	$(PYTHON) run_classifs.py 2> /dev/null

2019-npfl104-shared: $(VENV_NAME)
	@test -d 2019-npfl104-shared || git clone ssh://gitolite@redmine.ms.mff.cuni.cz/undergrads/student/2019-npfl104-shared.git
	@test -d 2019-npfl104-shared || $(MAKE) -C "./2019-npfl104-shared/data/czech-car-accidents"

# ENV
$(VENV_NAME): requirements.txt
	@test -d $(VENV_NAME) || $(PYTHON_GLOBAL) -m venv $(VENV_NAME)
	$(PYTHON) -m pip install -r requirements.txt

clean_$(VENV_NAME): 
	rm -rf $(VENV_NAME)

# Common:
clean_pycache:
	rm -rf __pycache__

clean_data:
	rm -rf 2019-npfl104-shared

clean: clean_$(VENV_NAME) clean_data clean_pycache 


