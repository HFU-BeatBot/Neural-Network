import librosa
import pandas as pd
import numpy as np
import tensorflow as tf
# '%matplotlib inline
import os
import csv

from keras.legacy_tf_layers.normalization import BatchNormalization
from keras.wrappers.scikit_learn import KerasClassifier
from matplotlib import pyplot as plt
from sklearn.feature_selection import VarianceThreshold
from sklearn.metrics import accuracy_score
# Preprocessing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler, Normalizer
# Keras
import keras
from keras import models
from keras import layers
from keras import callbacks


data = pd.read_csv('data.csv')
data.head()

# Dropping unneccesary columns
data = data.drop(['filename'], axis=1)
data.head()

genre_list = data.iloc[:, -1]
encoder = LabelEncoder()
y = encoder.fit_transform(genre_list)
print(y)

# normalizing
scaler = StandardScaler()
X = scaler.fit_transform(np.array(data.iloc[:, :-1], dtype=float))
# spliting of dataset into train and test dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)


def base_model(optimizer = 'adam', dropout_rate = 0.3, kernel_initializer = 'normal', activation = 'relu', units = 128):
    tf.keras.utils.set_random_seed(
        1
    )
    # creating a model
    model = models.Sequential()

    model.add(layers.Dense(units=256, activation= activation, input_shape=(X_train.shape[1],), kernel_initializer=kernel_initializer))
    layers.Dropout(rate=dropout_rate),  # apply 30% dropout to the next layer

    model.add(layers.Dense(units= 1028, activation=activation, kernel_initializer=kernel_initializer))
    layers.Dropout(rate=dropout_rate),

    model.add(layers.Dense(units= 512, activation=activation, kernel_initializer=kernel_initializer))
    layers.Dropout(rate=dropout_rate),

    model.add(layers.Dense(units=512, activation=activation, kernel_initializer=kernel_initializer))
    layers.Dropout(rate=dropout_rate),

    model.add(layers.Dense(units= 256, activation=activation, kernel_initializer=kernel_initializer))
    layers.Dropout(rate=dropout_rate),

    model.add(layers.Dense(units= units, activation=activation, kernel_initializer=kernel_initializer))
    layers.Dropout(rate=dropout_rate),

    model.add(layers.Dense(units=10, activation='softmax'))

    model.compile(optimizer= optimizer,
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    early_stopping = callbacks.EarlyStopping(
        min_delta=0.002,  # minimium amount of change to count as an improvement
        patience=1,  # how many epochs to wait before stopping
        restore_best_weights=True,
    )

    history = model.fit(X_train,
                        y_train,
                        validation_data=(X_test, y_test),
                        epochs=200,
                        callbacks=[early_stopping],
                        batch_size=500)
    return model

# Defining parameters for performing GridSearch
optimizer = ['sgd', 'rmsprop', 'adam']
dropout_rate = [0.1, 0.2, 0.3, 0.4, 0.5]
input_layer_nodes = [50, 107, 150, 200]
kernel_initializer = ['uniform', 'normal']
activation = ['relu', 'elu']

param_grid = dict(kernel_initializer = kernel_initializer, dropout_rate = dropout_rate, activation = activation, optimizer = optimizer, units = input_layer_nodes)

model = KerasClassifier(build_fn = base_model, epochs = 3, batch_size = 128, verbose = 2)

grid = GridSearchCV(estimator = model, param_grid=param_grid, n_jobs = -1, cv = 5)
grid.fit(X_train, y_train)

# View hyperparameters of best neural network
print("\nBest Training Parameters: ", grid.best_params_)
print("Best Training Accuracy: ", grid.best_score_)