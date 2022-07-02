"""
    Entrena el modelo con las caracteristicas creadas en el metodo make_features
"""
import os
import joblib
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

import pandas as pd


def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl

    """
    data_to_train = pd.read_csv(
        "./data_lake/business/features/precios_diarios.csv")

    data_to_train = data_to_train.drop(columns=["fecha"])
    target = data_to_train["precio"].array
    regressors = data_to_train.drop(columns=["precio"])
    x_train, x_rem, y_true_train, y_rem = train_test_split(
        regressors, target, test_size=0.3, random_state=603)

    x_valid, x_test, y_valid, y_true_test = train_test_split(x_rem,
                                                             y_rem,
                                                             test_size=0.5, random_state=603)

    x_test["y"] = y_true_test
    x_test.to_csv('src/models/dataToForecast.csv')

    model = MLPRegressor(max_iter= 100,
        activation='identity',
        solver= 'adam',
        learning_rate_init= 0.001)
    model = MLPRegressor()

    grid_search = GridSearchCV(estimator=model,
                               param_grid=[
        {
            "hidden_layer_sizes": [(1,), (2,), (3,), (4,), (5,)],
            "random_state": [1000, 1001, 1002, 1003, 1004, 1005]
        }
    ], cv=5)
    data_trained = grid_search.fit(x_train, y_true_train)
    path_parent_dir = os.path.join(os.getcwd(), "src/models")
    joblib.dump(data_trained, path_parent_dir + '/precios-diarios.pkl')


if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()
