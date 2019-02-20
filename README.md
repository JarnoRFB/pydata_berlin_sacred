[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JarnoRFB/pydata_berlin_sacred/master)

# Machine Learning Experiments with Sacred @PyData Berlin
A short introduction to [sacred](https://github.com/IDSIA/sacred) for logging machine learning experiments.

## Installation
If you want to run the notebook offline, you will need conda and docker:

    $ conda create -f environment.yml
    $ cd sacred_setup
    $ docker-compose up -d
    $ cd ..
    $ jupyter notebook