import os

from sacred import Experiment
from sacred.observers import MongoObserver
from sklearn import svm, datasets, model_selection
from dotenv import load_dotenv


db_name = "pydata_berlin"
mongo_uri = None

ex = Experiment('svm')

ex.observers.append(
    MongoObserver.create(
        url=mongo_uri,
        db_name=db_name,
    )
)

     
@ex.config
def cfg():
    C = 1.0
    gamma = 0.7
    kernel = "rbf"
    seed = 42


@ex.capture
def get_model(C, gamma, kernel):
    return svm.SVC(C=C, kernel=kernel, gamma=gamma)

           
@ex.automain # Use automain to enable command line integration.
def run():
    X, y = datasets.load_breast_cancer(return_X_y=True)
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
    clf = get_model()
    clf.fit(X_train, y_train)
    return clf.score(X_test, y_test)
