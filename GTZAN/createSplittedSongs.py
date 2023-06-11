import os
import csv
import librosa
import numpy as np

from sklearn.preprocessing import StandardScaler

# Initialize the CSV file
header = 'filename'
for i in range(1, 21):
    header += f' mfcc{i}_mean'
    header += f' mfcc{i}_std'
header += ' label'
header = header.split()

# Path of the "genres" folder
genres_folder = 'genres'

# List of genres
genres = 'blues classical country disco hiphop jazz metal pop reggae rock'.split()

# Path to the output folder for the audio segments and the CSV file
output_folder = 'GTZAN_Splitted_Songs'
output_csv_file = os.path.join(output_folder, 'SplittedSong.csv')

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Create the CSV file
with open(output_csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)

# Define the desired length of each audio segment in seconds
snippet_duration = 5

# Loop over the genres
for genre in genres:
    genre_folder = os.path.join(genres_folder, genre)
    if os.path.isdir(genre_folder):

        # Load the song files in the genre folder
        songs_folder = os.path.join(genre_folder)
        songs = [song for song in os.listdir(songs_folder)]

        # Iterate over the songs and create the snippets
        for song in songs:
            song_path = os.path.join(genre_folder, song)

            # Convert MP3 to WAV
            wav_filename = os.path.splitext(song)[0] + '.wav'
            wav_path = os.path.join(songs_folder, wav_filename)
            os.system(f'ffmpeg -i "{song_path}" "{wav_path}"')

            # Load the WAV file
            data, sample_rate = librosa.load(song_path, sr=None)

            total_samples = len(data)
            snippet_samples = int(snippet_duration * sample_rate)

            # Extract the snippets
            for i in range(int(total_samples / snippet_samples)):
                start_index = i * snippet_samples
                end_index = start_index + snippet_samples
                snippet = data[start_index:end_index]

                # Extract MFCC features from the snippet
                mfcc = librosa.feature.mfcc(y=snippet, sr=sample_rate)
                mfcc_mean = np.mean(mfcc, axis=1)
                mfcc_std = np.std(mfcc, axis=1)
                mfcc_features = np.concatenate((mfcc_mean, mfcc_std))

                # Scale the features
                scaler = StandardScaler()
                scaled_features = scaler.fit_transform([mfcc_features])

                for e in mfcc:
                    wav_filename += f' {np.mean(e)}'
                    wav_filename += f' {np.std(e)}'

                wav_filename += f' {genre}'

                # Append the song information to the CSV file
                with open(output_csv_file, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(wav_filename.split())

print("Snippets were created and saved in the CSV file.")
