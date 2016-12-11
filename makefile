init:
	mkdir data
	conda create --name tf python=3.5 pandas jupyter matplotlib scikit-learn Flask

tf_install:
	conda install -c conda-forge tensorflow