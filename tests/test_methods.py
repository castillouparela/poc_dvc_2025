import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

import pytest
from sklearn.datasets import make_classification
from sklearn.base import BaseEstimator

# Configuración de fixtures usados en métodos de prueba (fase Arrange)
@pytest.fixture
def model():
    return RandomForestClassifier()

@pytest.fixture
def data():
    X, y = make_classification(n_samples=100, n_features=20, random_state=999)
    X_train, y_train = train_test_split (
                                            X,
                                            y,
                                            test_size   = 0.05,
                                            random_state = 999
                                        )
    return X_train, y_train

@pytest.fixture
def df_fixture():
    return pd.DataFrame({
        'Feature01': [0.20, 0.51, 0.30, 0.40, 0.50],
        'Feature02': [1500000, 2000000, 2500000, 3000000, 3500000],
        'Feature03': [0.10, 0.21, 0.02, 0.00, 0.23],
        'Feature04': [0.15, 0.26, 0.07, 0.09, 0.29],
        'Feature05': [10, 20, 30, 40, 50],
        'Feature06': [1, 0, 0, 4, 20]
    })
    
# Método de pruebas unitarias para la función simple_train_model
def test_simple_train_model(model: BaseEstimator, data: tuple):
    '''
    Method to test function for the simple_train_model method
    with methodological approach AAA (Arrange, Act, Assert)
    
    Parameters:
        model: Model to train from fixture
        data: Data to train the model from fixture
    '''
    # Arrange
    X_train, X_test, X_val, y_train, y_test, y_val = data
    
    # Act
    f1 = model.fit(X_train, y_train).score(X_test, y_test)
    model_trained = model.fit(pd.DataFrame(X_train), pd.Series(y_train))
    
    # Assert
    assert isinstance(model, BaseEstimator) # Validación del modelo recibido por parámetro
    assert isinstance(f1, float) # Validación del tipado de dato decimal (fracción de F1 Score)
    assert 0 <= f1 <= 1 # Validación del rango del valor retornado
    assert isinstance(model_trained, BaseEstimator) # Validación del modelo retornado