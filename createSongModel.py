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

#song = 'Bee Gees - Stayin Alive (Official Video).mp3'
#song = 'Edvard Grieg-morgenstimmung.mp3'
#song = 'Johnny Cash - Hurt.mp3'
#song = 'Ray Charles - Hit The Road Jack (Official Lyrics Video).mp3'
#song = 'ACDC - Thunderstruck (Official Video).mp3'
#song = '50 Cent - In Da Club (Official Music Video).mp3'
#song = 'Beat It - Michael Jackson (Lyrics).mp3'
#song = 'Bob Marley & The Wailers - Buffalo Soldier (Official Music Video).mp3'
FullAudio = AudioSegment.from_mp3(song)
lengthOfAudio = FullAudio.duration_seconds
y, sr = librosa.load(song, mono=True, duration=lengthOfAudio)
chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
rmse = librosa.feature.rms(y=y)
spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
zcr = librosa.feature.zero_crossing_rate(y)
mfcc = librosa.feature.mfcc(y=y, sr=sr)
#to_append = f'{filename} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'
#songToArray = [None] * 27
songToArray = [np.mean(chroma_stft), np.mean(rmse), np.mean(spec_cent), np.mean(spec_bw), np.mean(rolloff), np.mean(zcr)]
for e in mfcc:
    songToArray.append(np.mean(e))

scaler = StandardScaler()
X = scaler.fit_transform(np.array(data.iloc[:, :-1], dtype=float))

numpySongArray = np.array([songToArray])
numpySongArray = scaler.transform(numpySongArray)
#np.reshape(numpySongArray, (26, 256)).T
print('NumpySongArray:')
print(numpySongArray)
#model.fit(numpySongArray)
prediction = model.predict(numpySongArray)
print(np.argmax(prediction[0]))

