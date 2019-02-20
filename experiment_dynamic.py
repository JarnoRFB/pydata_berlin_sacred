import os
from importlib import import_module  # For dynamic imports.

from sacred import Experiment
from sacred.observers import MongoObserver
from sklearn import svm, datasets, model_selection
from dotenv import load_dotenv

env_path = "sacred_setup/.env"
load_dotenv(dotenv_path=env_path)
db_name = os.environ["MONGO_DATABASE"]
mongo_uri = (f'mongodb://{os.environ["MONGO_INITDB_ROOT_USERNAME"]}:'
             f'{os.environ["MONGO_INITDB_ROOT_PASSWORD"]}@localhost:27017/?authMechanism=SCRAM-SHA-1')

ex = Experiment('svm')

ex.observers.append(
    MongoObserver.create(
        url=mongo_uri,
        db_name=db_name,
    )
)

             
def load(path):
    """Load a class, given its fully qualified path."""
    p, m = path.rsplit('.', 1)
    module = import_module(p)
    class_or_method = getattr(module, m)
    return class_or_method
     

@ex.capture(prefix="model")  # Prefix to only get the relevant subset of the config.
def get_model(path, hyperparameters):
    Model = load(path)  # Import model class dynamically.
    return Model(**hyperparameters)  # Instantiate with hyperparameters.

           
@ex.automain # Use automain to enable command line integration.
def run():
    X, y = datasets.load_breast_cancer(return_X_y=True)
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
    clf = get_model()
    clf.fit(X_train, y_train)
    return clf.score(X_test, y_test)
