import librosa
import pandas as pd
import numpy as np
import tensorflow as tf
# import matplotlib.pyplot as plt
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



# generating a dataset
#header = 'filename chroma_stft rmse spectral_centroid spectral_bandwidth rolloff zero_crossing_rate'
header = 'filename'
for i in range(1, 21):
    header += f' mfcc{i}'
header += ' label'
header = header.split()

file = open('data.csv', 'w', newline='')
with file:
    writer = csv.writer(file)
    writer.writerow(header)
genres = 'blues classical country disco hiphop jazz metal pop reggae rock'.split()
for g in genres:
    filenamewhohidden = (filename for filename in os.listdir(f'./genres/{g}') if not filename.startswith('.'))
    for filename in filenamewhohidden:
        songname = f'./genres/{g}/{filename}'
        y, sr = librosa.load(songname, mono=True, duration=3)
        #chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        #rmse = librosa.feature.rms(y=y)
        #spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        #spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        #rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        #zcr = librosa.feature.zero_crossing_rate(y)
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        #to_append = f'{filename} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'
        to_append = f'{filename}'
        for e in mfcc:
            to_append += f' {np.mean(e)}'
        to_append += f' {g}'
        file = open('data.csv', 'a', newline='')
        with file:
            writer = csv.writer(file)
            writer.writerow(to_append.split())

# reading dataset from csv
