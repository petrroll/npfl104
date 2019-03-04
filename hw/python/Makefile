SRC = *.py

# Explicit .PHONY because $(SRC) files exist -> MAKE wouldn't run the rule (that invokes python) with them as goal
.PHONY test_all: $(SRC)

.PHONY $(SRC): 
	python3.6 $@

