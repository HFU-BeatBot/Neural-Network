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

song = 'Bob Marley & The Wailers - Buffalo Soldier (Official Music Video).mp3'

FullAudio = AudioSegment.from_mp3(song)             #falls WAV Datei dann .from_wav()
lengthOfAudio = FullAudio.duration_seconds
y, sr = librosa.load(song, mono=True, duration=lengthOfAudio)
chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
rmse = librosa.feature.rms(y=y)
spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
zcr = librosa.feature.zero_crossing_rate(y)
mfcc = librosa.feature.mfcc(y=y, sr=sr)
songToArray = [np.mean(chroma_stft), np.mean(rmse), np.mean(spec_cent), np.mean(spec_bw), np.mean(rolloff), np.mean(zcr)]
for e in mfcc:
    songToArray.append(np.mean(e))

numpySongArray = np.array([songToArray])
numpySongArray = scaler.transform(numpySongArray)

print('NumpySongArray:')
print(numpySongArray)

prediction = model.predict(numpySongArray)
print(np.argmax(prediction[0]))

