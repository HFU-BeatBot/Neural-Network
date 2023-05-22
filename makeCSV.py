import csv
import os

import librosa
import numpy as np
from pydub import AudioSegment

from addNoise import addNoise


def generateArrayOfMeanAndSTD(song, filename, genre):
    y, sr = librosa.load(song, mono=True, duration=3)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    # to_append = f'{filename} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'
    to_append = f'{filename}'
    for e in mfcc:
        to_append += f' {np.mean(e)}'
        to_append += f' {np.std(e)}'
    to_append += f' {genre}'
    return to_append

def makeCSV(partLength = 5):
    #Preparing for the CSV file:
    #Preparing the header row as an array. First the filename than the mfcc values (mean and std) from 1 to 20
    header = 'filename'
    for i in range(1, 21):
        header += f' mfcc{i}_mean'
        header += f' mfcc{i}_std'
    header += ' label'
    header = header.split()

    #create an empty CSV file and fill the first row with the header array
    file = open('data.csv', 'w', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerow(header)

    #going through all wav files
    genres = 'blues classical country disco hiphop jazz metal pop reggae rock'.split()
    for g in genres:
        filenamewhohidden = (filename for filename in os.listdir(f'./genres/{g}') if not filename.startswith('.'))
        for filename in filenamewhohidden:
            #preparing variables
            songname = f'./genres/{g}/{filename}'
            FullAudio = AudioSegment.from_wav(songname)
            lengthOfAudio = FullAudio.duration_seconds

            #Only if the current song is longer than the length it should have it will splitted
            if (lengthOfAudio > partLength + 1):
                splitter = int(lengthOfAudio / partLength)
                i = 0
                j = int(0)
                #The splitter is the number of how many parts it can create of the whole song
                while (i < splitter):
                    #this line is doing the whole trick, it takes out the audio part which is needed
                    #after that it just export it and it takes the data out of the new wav
                    newAudioPart = FullAudio[j: j + partLength * 1000]
                    newAudioPart.export('tmp.wav', format='wav')
                    to_append = generateArrayOfMeanAndSTD(songname + str(i), 'tmp.wav', g)
                    #filling the data of the wav part into the csv
                    file = open('data.csv', 'a', newline='')
                    with file:
                        writer = csv.writer(file)
                        writer.writerow(to_append.split())
                    i += 1
                    j = j + partLength * 1000
                    #creating gausian noised wav file out of the wav part
                    signal, sr = librosa.load('tmp.wav')
                    addNoise(signal, sr, 'tmp.wav')
                    to_append = generateArrayOfMeanAndSTD(songname + str(i), 'tmp.wav', g)
                    # filling the data of the wav part into the csv
                    file = open('data.csv', 'a', newline='')
                    with file:
                        writer = csv.writer(file)
                        writer.writerow(to_append.split())
            #Otherwise the song is shorter than length we want and it creates the value normally
            else:
                to_append = generateArrayOfMeanAndSTD(songname, filename, g)
                file = open('data.csv', 'a', newline='')
                with file:
                    writer = csv.writer(file)
                    writer.writerow(to_append.split())
                # creating gausian noised wav file out of the wav part
                signal, sr = librosa.load('tmp.wav')
                addNoise(signal, sr, 'tmp.wav')
                to_append = generateArrayOfMeanAndSTD(songname + str(i), filename, g)
                # filling the data of the wav part into the csv
                file = open('data.csv', 'a', newline='')
                with file:
                    writer = csv.writer(file)
                    writer.writerow(to_append.split())