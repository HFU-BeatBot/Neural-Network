import csv
import os

import librosa
import numpy as np

# create the header for the CSV file
header = 'filename'
for i in range(1, 21):
    header += f' mfcc{i}_mean'
    header += f' mfcc{i}_std'
header += ' label'
header = header.split()

# create the directory for the CSV file
directory = 'data/'
os.makedirs(directory, exist_ok=True)

# create the file path for the CSV file
file_path = os.path.join(directory, 'gtzan_data.csv')
file = open(file_path, 'w', newline='')

with file:
    writer = csv.writer(file)
    writer.writerow(header)

# list of genres
genres = 'blues classical country disco hiphop jazz metal pop reggae rock'.split()

# iterate over each genre
for g in genres:
    folder_path = os.path.join(f'genres_wav/{g}')
    filenames = [filename for filename in os.listdir(folder_path)
                 if not filename.startswith('.')]

    # iterate over each file in the genre folder
    for filename in filenames:
        songname = f'./genres_wav/{g}/{filename}'
        y, sr = librosa.load(songname, mono=True, duration=3)
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        to_append = f'{filename}'

        # extract mean and standard deviation of each MFCC coefficient
        for e in mfcc:
            to_append += f' {np.mean(e)}'
            to_append += f' {np.std(e)}'

        to_append += f' {g}'

        # append the data to the CSV file
        file = open(file_path, 'a', newline='')
        with file:
            writer = csv.writer(file)
            writer.writerow(to_append.split())