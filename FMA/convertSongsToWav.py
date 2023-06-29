import os
import librosa
import soundfile as sf

# create the directory for the WAV files
wav_directory = 'fma_small_wav/'
os.makedirs(wav_directory, exist_ok=True)

# list of genres
genres = 'electronic experimental folk hiphop instrumental international pop rock'.split()

# iterate over each genre
for g in genres:
    genre_directory = os.path.join(wav_directory, g)
    os.makedirs(genre_directory, exist_ok=True)

    folder_path = os.path.join(f'fma_small/{g}')
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            songname = os.path.join(root, filename)

            try:
                # Convert MP3 to WAV
                wav_filename = filename.replace('.mp3', '.wav')
                wav_path = os.path.join(genre_directory, wav_filename)
                audio, sr = librosa.load(songname, mono=True, duration=30)
                sf.write(wav_path, audio, sr)

                print(f'file: {wav_filename} - Song converted to WAV')

            except Exception as e:
                print(f'Skipped file: {songname} - Error')
