#song = 'Bee Gees - Stayin Alive (Official Video).mp3'
#song = 'Edvard Grieg-morgenstimmung.mp3'
# song = 'Johnny Cash - Hurt.mp3'
# song = 'Ray Charles - Hit The Road Jack (Official Lyrics Video).mp3'
# song = 'ACDC - Thunderstruck (Official Video).mp3'
# song = '50 Cent - In Da Club (Official Music Video).mp3'
# song = 'Beat It - Michael Jackson (Lyrics).mp3'
# song = 'Bob Marley & The Wailers - Buffalo Soldier (Official Music Video).mp3'
import librosa
import pandas as pd
import numpy as np
import tensorflow as tf

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


sampleSollLength = int(3)
FullAudio = AudioSegment.from_mp3(song)
NameOfFile = os.path.basename(song)
print(os.path.splitext(NameOfFile)[0])
lengthOfAudio = FullAudio.duration_seconds
print(lengthOfAudio)
if (lengthOfAudio > sampleSollLength + 1):
    splitter = int(lengthOfAudio / sampleSollLength)
    print('splitter: ' + str(splitter))
    predictionsOfSong = []
    i = int(0)
    j = int(0)
    while (i < splitter):
        newAudioPart = FullAudio[j: j + sampleSollLength * 1000]
        newAudioPart.export('./cache/' + 'SongPart' + str(i) + '.wav', format='wav')

        songPart = './cache/SongPart' + str(i) + '.wav'

        y, sr = librosa.load(songPart, mono=True, duration=30)
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

        data = data.drop(['filename'], axis=1)
        data.head()

        scaler = StandardScaler()
        X = scaler.fit_transform(np.array(data.iloc[:, :-1], dtype=float))

        numpySongArray = np.array([songToArray])
        numpySongArray = scaler.transform(numpySongArray)
        # np.reshape(numpySongArray, (26, 256)).T
        print('NumpySongArray:')
        print(numpySongArray)
        # model.fit(numpySongArray)
        prediction1 = model.predict(numpySongArray)
        print(prediction1)
        predictionsOfSong.append(np.argmax(prediction1))
        i = i + 1
        j = j + sampleSollLength * 1000
averagePrediction = 0
for i in range(len(predictionsOfSong)):
    averagePrediction = averagePrediction + predictionsOfSong[i]
print('average prediction: ' + str(averagePrediction / splitter))
print('end')

