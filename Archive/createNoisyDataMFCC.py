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
from addNoise import addNoise



def writeCSV(songname, filename):
    y, sr = librosa.load(songname, mono=True, duration=3)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    # to_append = f'{filename} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'
    to_append = f'{filename}'
    for e in mfcc:
        to_append += f' {np.mean(e)}'
        to_append += f' {np.std(e)}'
    to_append += f' {g}'
    file = open('data.csv', 'a', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerow(to_append.split())


# generating a dataset
#header = 'filename chroma_stft rmse spectral_centroid spectral_bandwidth rolloff zero_crossing_rate'
header = 'filename'
for i in range(1, 21):
    header += f' mfcc{i}_mean'
    header += f' mfcc{i}_std'
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
        writeCSV(songname, filename)

        signal, sr = librosa.load(songname)
        addNoise(signal, sr)
        songnameGaussion = "Gaussian.wav"
        filenameGaussion = "Gaussian_" + filename
        writeCSV(songnameGaussion, filenameGaussion)
        os.remove(songnameGaussion)

# reading dataset from csv

