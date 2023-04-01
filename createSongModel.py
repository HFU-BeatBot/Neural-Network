import librosa
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
# '%matplotlib inline
import os
import csv
# Preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
# Keras
import keras
from keras import models
from keras import layers

song = 'Bee Gees - Stayin Alive (Official Video).mp3'
y, sr = librosa.load(song, mono=True, duration=30)
chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
rmse = librosa.feature.rms(y=y)
spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
zcr = librosa.feature.zero_crossing_rate(y)
mfcc = librosa.feature.mfcc(y=y, sr=sr)
# to_append = f'{filename} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'
# songToArray = [None] * 27
songToArray = [np.mean(chroma_stft), np.mean(rmse), np.mean(spec_cent), np.mean(spec_bw), np.mean(rolloff),
               np.mean(zcr)]
for e in mfcc:
    songToArray.append(np.mean(e))

scaler = StandardScaler()
X = scaler.fit_transform(np.array(data.iloc[:, :-1], dtype=float))

numpySongArray = np.array([songToArray])
# np.reshape(numpySongArray, (26, 256)).T
print('NumpySongArray:')
print(numpySongArray)
# model.fit(numpySongArray)
prediction = model.predict(numpySongArray)
np.argmax(prediction)