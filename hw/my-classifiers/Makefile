all: perc knn nb

artificial_objects:
	wget https://ufal.mff.cuni.cz/~zabokrtsky/courses/npfl104/data/classification/artificial_objects.tgz
	tar -xvz --one-top-level -f artificial_objects.tgz
	rm -r artificial_objects.tgz

adult:
	wget -r -nH --cut-dirs=2 --no-parent --reject="index.html*" http://archive.ics.uci.edu/ml/machine-learning-databases/adult/

download: adult artificial_objects

nb: download
	python3 naive_bayes_runner.py

knn: download
	python3 knn_runner.py

perc: download
	python3 perc_runner.py

