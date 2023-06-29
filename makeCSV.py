import csv
import os
import librosa
import numpy as np
from pydub import AudioSegment
from addNoise import addNoise

def generateArrayOfMeanAndSTD(song, filename, genre):
    # Load the audio signal and calculate the MFCCs
    y, sr = librosa.load(song, mono=True)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    to_append = f'{filename}'
    for e in mfcc:
        # Append the MFCC mean and standard deviation to the array
        to_append += f' {np.mean(e)}'
        to_append += f' {np.std(e)}'
    to_append += f' {genre}'  # Append the genre to the array
    return to_append

def makeCSV(partLength=5, genresOfLibrary='blues classical country disco hiphop jazz metal pop reggae rock',
            path='genres', noisy=False, isItMP3=False, nameOfDataCSV='data.csv'):
    # Preparing for the CSV file:
    # Prepare the header row as an array. First, the filename, followed by the MFCC values (mean and std) from 1 to 20
    header = 'filename'
    for i in range(1, 21):
        header += f' mfcc{i}_mean'
        header += f' mfcc{i}_std'
    header += ' label'
    header = header.split()
    print("makeCSV Start")
    # Create an empty CSV file and fill the first row with the header array
    file = open(nameOfDataCSV, 'w', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerow(header)

    # Iterate through all wav files
    genres = genresOfLibrary.split()
    for g in genres:
        filenamewhohidden = (filename for filename in os.listdir(f'./{path}/{g}') if not filename.startswith('.'))
        for filename in filenamewhohidden:
            # Prepare variables
            songname = f'./{path}/{g}/{filename}'
            if isItMP3:
                FullAudio = AudioSegment.from_mp3(songname)
            else:
                FullAudio = AudioSegment.from_wav(songname)
            lengthOfAudio = FullAudio.duration_seconds
            print("go")
            # Only split the current song if it is longer than the desired length
            if lengthOfAudio > partLength + 1:
                splitter = int(lengthOfAudio / partLength)
                i = 0
                j = int(0)
                # The splitter is the number of parts that can be created from the whole song
                while i < splitter:
                    # Extract the audio part needed and export it as a new WAV file
                    newAudioPart = FullAudio[j: j + partLength * 1000]
                    newAudioPart.export('tmp.wav', format='wav')
                    to_append = generateArrayOfMeanAndSTD('tmp.wav', filename + str(i), g)
                    # Fill the data of the WAV part into the CSV
                    file = open(nameOfDataCSV, 'a', newline='')
                    with file:
                        writer = csv.writer(file)
                        writer.writerow(to_append.split())
                    i += 1
                    j = j + partLength * 1000
                    # Create a Gaussian-noised WAV file out of the WAV part
                    if noisy == True:
                        signal, sr = librosa.load('tmp.wav')
                        addNoise(signal, sr, 'tmp.wav')
                        to_append = generateArrayOfMeanAndSTD('tmp.wav', filename + '_gaussian.' + str(i), g)
                        # Fill the data of the WAV part into the CSV
                        file = open(nameOfDataCSV, 'a', newline='')
                        with file:
                            writer = csv.writer(file)
                            writer.writerow(to_append.split())
            # Otherwise, the song is shorter than the desired length and it is processed normally
            else:
                print("else fall")
                newAudioPart = FullAudio
                newAudioPart.export('tmp.wav', format='wav')
                print("export geklappt")
                to_append = generateArrayOfMeanAndSTD('tmp.wav', filename, g)
                file = open(nameOfDataCSV, 'a', newline='')
                with file:
                    writer = csv.writer(file)
                    writer.writerow(to_append.split())
                # Create a Gaussian-noised WAV file out of the WAV part
                signal, sr = librosa.load('tmp.wav')
                addNoise(signal, sr, 'tmp.wav')
                to_append = generateArrayOfMeanAndSTD('tmp.wav', filename + '_gaussian', g)
                # Fill the data of the WAV part into the CSV
                file = open(nameOfDataCSV, 'a', newline='')
                with file:
                    writer = csv.writer(file)
                    writer.writerow(to_append.split())

    os.remove('tmp.wav')
print("Done")
