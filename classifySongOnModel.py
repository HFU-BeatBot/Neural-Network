import librosa
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
# '%matplotlib inline
import os
import csv

from pydub import AudioSegment
# Preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
# Keras
import keras
from keras import models
from keras import layers
from joblib import load

def classifySongOnModel(song, model, scaler):
    # Example of how the song string could look like:
    # song = 'Bob Marley & The Wailers - Buffalo Soldier (Official Music Video).mp3'

    # Load the song extract the mfcc values
    y, sr = librosa.load(song, mono=True)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)

    # filling the mfcc values into an array
    songToArray = []
    for e in mfcc:
        songToArray.append(np.mean(e))
        songToArray.append(np.std(e))

    # tranform the array to numpy array
    numpySongArray = np.array([songToArray], dtype=float)

    # scale the numpy array with the models scaler
    standardScaler = load(scaler)
    numpySongArray = standardScaler.transform(numpySongArray)

    # printing the values of the numpy array. Is not neccesary, it is just for control purpose.
    print('NumpySongArray:')
    print(numpySongArray)

    # the model predicts the genre of that song and print it into the console and return it
    model = tf.keras.models.load_model
    prediction = model.predict(numpySongArray)
    print(np.argmax(prediction[0]))
    return np.argmax(prediction[0])



