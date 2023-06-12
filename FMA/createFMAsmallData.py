import csv
import os
import warnings

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
directory = 'data/fma_metadata/'
os.makedirs(directory, exist_ok=True)

# create the file path for the CSV file
file_path = os.path.join(directory, 'fma_small_data.csv')
file = open(file_path, 'w', newline='')

with file:
    writer = csv.writer(file)
    writer.writerow(header)

# list of genres
genres = 'electronic experimental folk hiphop instrumental international pop rock'.split()

# iterate over each genre
for g in genres:
    folder_path = os.path.join(f'fma_small/{g}')
    filenames = [filename for filename in os.listdir(folder_path) if not filename.startswith('.')]

    # iterate over each file in the genre folder
    for filename in filenames:
        songname = f'./fma_small/{g}/{filename}'

        try:
            # Load the audio file
            with warnings.catch_warnings():
                warnings.filterwarnings('ignore')
                y, sr = librosa.load(songname, mono=True, duration=30)

            # If the duration of the song is equal to 30 sec or less than 30 sec, print
            if len(y) == sr * 30:
                print(f'file: {songname} - Song written to .CSV file')

            mfcc = librosa.feature.mfcc(y=y, sr=sr)
            to_append = f'{filename}'

            # extract mean and standard deviation of each MFCC coefficient
            for e in mfcc:
                to_append += f' {np.mean(e)}'
                to_append += f' {np.std(e)}'

            to_append += f' {g}'

            # append the data to the CSV file
            with open(file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(to_append.split())

        # Exceptions handel
        except Exception as e:
            print(f'Skipped file: {songname} - Error')
