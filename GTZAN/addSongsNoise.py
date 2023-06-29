import os
import csv
import numpy as np
import soundfile as sf
import librosa

# Initialize the CSV file
header = 'filename'
for i in range(1, 21):
    header += f' mfcc{i}_mean'
    header += f' mfcc{i}_std'
header += ' label'
header = header.split()

# Set the path to the FMA small dataset
fma_path = 'genres_wav'

# Create the output folder if it doesn't exist
output_folder = 'GTZAN_Noisy_Songs'
os.makedirs(output_folder, exist_ok=True)

# Initialize the CSV file
csv_file = os.path.join('data/gtzan_noisy_songs.csv')

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)

# Set the noise level
noise_level = 0.05

# Iterate over the FMA small songs
for root, dirs, files in os.walk(fma_path):
    for filename in files:
        if filename.endswith('.wav'):
            song_path = os.path.join(root, filename)
            label = os.path.basename(root)

            # Read the song file
            data, sample_rate = sf.read(song_path)

            # Add noise to the song data
            noise = np.random.normal(0, noise_level, len(data))
            noisy_data = data + noise

            # Normalize the audio data
            max_value = np.max(np.abs(noisy_data))
            normalized_data = noisy_data / max_value

            # Create the genre folder if it doesn't exist
            genre_folder = os.path.join(output_folder, label)
            os.makedirs(genre_folder, exist_ok=True)

            # Save the noisy audio file in the genre folder
            output_filename = f'{filename[:-4]}_noisy.wav'
            output_path = os.path.join(genre_folder, output_filename)
            sf.write(output_path, normalized_data, sample_rate)

            # Extract MFCC features from the noisy audio
            mfcc = librosa.feature.mfcc(y=noisy_data, sr=sample_rate)
            mfcc_mean = np.mean(mfcc, axis=1)
            mfcc_std = np.std(mfcc, axis=1)
            mfcc_features = np.concatenate((mfcc_mean, mfcc_std))

            # Append the song information with MFCC values to the CSV file
            row = [output_filename, label]
            for feature in mfcc_features:
                row.append(feature)
            with open(csv_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(row)

print("Noisy songs were generated and saved in the output folder.")
