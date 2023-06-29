import csv
import os

import librosa
import numpy as np
from pydub import AudioSegment

from addNoise import addNoise


def generateArrayOfMeanAndSTD(song, filename, genre):
    y, sr = librosa.load(song, mono=True)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    # to_append = f'{filename} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'
    to_append = f'{filename}'
    for e in mfcc:
        to_append += f' {np.mean(e)}'
        to_append += f' {np.std(e)}'
    to_append += f' {genre}'
    return to_append


def makeCSV(partLength=5, genresOfLibrary='blues classical country disco hiphop jazz metal pop reggae rock',
            path='genres', noisy=False, isItMP3 = False, nameOfDataCSV = 'data.csv'):
    # Preparing for the CSV file:
    # Preparing the header row as an array. First the filename than the mfcc values (mean and std) from 1 to 20
    header = 'filename'
    for i in range(1, 21):
        header += f' mfcc{i}_mean'
        header += f' mfcc{i}_std'
    header += ' label'
    header = header.split()
    print("makeCSV Start")
    # create an empty CSV file and fill the first row with the header array
    file = open(nameOfDataCSV, 'w', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerow(header)

    # going through all wav files
    genres = genresOfLibrary.split()
    for g in genres:
        filenamewhohidden = (filename for filename in os.listdir(f'./{path}/{g}') if not filename.startswith('.'))
        for filename in filenamewhohidden:
            # preparing variables
            songname = f'./{path}/{g}/{filename}'
            if isItMP3:
                FullAudio = AudioSegment.from_mp3(songname)
            else:
                FullAudio = AudioSegment.from_wav(songname)
            lengthOfAudio = FullAudio.duration_seconds
            print("go")
            # Only if the current song is longer than the length it should have it will splitted
            if lengthOfAudio > partLength + 1:
                splitter = int(lengthOfAudio / partLength)
                i = 0
                j = int(0)
                # The splitter is the number of how many parts it can create of the whole song
                while i < splitter:
                    # this line is doing the whole trick, it takes out the audio part which is needed
                    # after that it just export it and it takes the data out of the new wav
                    newAudioPart = FullAudio[j: j + partLength * 1000]
                    newAudioPart.export('tmp.wav', format='wav')
                    to_append = generateArrayOfMeanAndSTD('tmp.wav', filename + str(i), g)
                    # filling the data of the wav part into the csv
                    file = open(nameOfDataCSV, 'a', newline='')
                    with file:
                        writer = csv.writer(file)
                        writer.writerow(to_append.split())
                    i += 1
                    j = j + partLength * 1000
                    # creating gausian noised wav file out of the wav part
                    if noisy == True:
                        signal, sr = librosa.load('tmp.wav')
                        addNoise(signal, sr, 'tmp.wav')
                        to_append = generateArrayOfMeanAndSTD('tmp.wav', filename + '_gaussian.' + str(i), g)
                        # filling the data of the wav part into the csv
                        file = open(nameOfDataCSV, 'a', newline='')
                        with file:
                            writer = csv.writer(file)
                            writer.writerow(to_append.split())
            # Otherwise the song is shorter than length we want and it creates the value normally
            else:
                print("else fall")
                newAudioPart = FullAudio
                newAudioPart.export('tmp.wav', format='wav')
                print("export geklappt")
                to_append = generateArrayOfMeanAndSTD('tmp.wav', filename, g)
                file = open(, 'a', newline='')
                with file:
                    writer = csv.writer(file)
                    writer.writerow(to_append.split())
                # creating gausian noised wav file out of the wav part
                signal, sr = librosa.load('tmp.wav')
                addNoise(signal, sr, 'tmp.wav')
                to_append = generateArrayOfMeanAndSTD('tmp.wav', filename + '_gaussian', g)
                # filling the data of the wav part into the csv
                file = open('nameOfDataCSV', 'a', newline='')
                with file:
                    writer = csv.writer(file)
                    writer.writerow(to_append.split())

    os.remove('tmp.wav')
print("Done")
