import os
import librosa
import soundfile as sf

# create the directory for the WAV files
wav_directory = 'genres_wav/'
os.makedirs(wav_directory, exist_ok=True)

# list of genres
genres = 'blues classical country disco hiphop jazz metal pop reggae rock'.split()

# iterate over each genre
for g in genres:
    genre_directory = os.path.join(wav_directory, g)
    os.makedirs(genre_directory, exist_ok=True)

    folder_path = os.path.join(f'genres/{g}')
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            songname = os.path.join(root, filename)

            try:
                # Convert AU to WAV
                wav_filename = filename.replace('.au', '.wav')
                wav_path = os.path.join(genre_directory, wav_filename)
                audio, sr = librosa.load(songname, mono=True, duration=30)
                sf.write(wav_path, audio, sr)

                print(f'file: {wav_filename} - Song converted to WAV')

            except Exception as e:
                print(f'Skipped file: {songname} - Error')
