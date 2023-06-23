import os
import shutil
import pandas as pd
from pydub import AudioSegment

# Path to tracks.csv
tracks_file = 'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_metadata/tracks.csv'

# Check if data folders already exist
dataIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data")
bluesIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data/blues")
classicalIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data/classical")
countryIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data/country")
discoIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data/disco")
hipHopIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data/hiphop")
jazzIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data/jazz")
metalIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data/metal")
popIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data/pop")
reggaeIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data/reggae")
rockIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data/rock")

# Create data & genre folders
if not dataIsExist:
    # Create data folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data")
    print("Data folder created.")
if not bluesIsExist:
    # Create blues folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data/blues")
    print("Blues folder created.")
if not classicalIsExist:
    # Create classical folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data/classical")
    print("Classical folder created.")
if not countryIsExist:
    # Create country folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data/country")
    print("Country folder created.")
if not discoIsExist:
    # Create disco folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data/disco")
    print("Disco folder created.")
if not hipHopIsExist:
    # Create hiphop folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data/hiphop")
    print("HipHop folder created.")
if not jazzIsExist:
    # Create jazz folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data/jazz")
    print("Jazz folder created.")
if not metalIsExist:
    # Create metal folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data/metal")
    print("Metal folder created.")
if not popIsExist:
    # Create pop folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data/pop")
    print("Pop folder created.")
if not reggaeIsExist:
    # Create reggae folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data/reggae")
    print("Reggae folder created.")
if not rockIsExist:
    # Create rock folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data/rock")
    print("Rock folder created.")

# Move Songs from child to root directories
parent_folder = "C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large"

# Get a list of all child folders
child_folders = [folder for folder in os.listdir(parent_folder)
                 if os.path.isdir(os.path.join(parent_folder, folder))]

# Move files from child folders to parent folder
for folder in child_folders:
    folder_path = os.path.join(parent_folder, folder)
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        shutil.move(file_path, parent_folder)

# Delete the child folders
for folder in child_folders:
    folder_path = os.path.join(parent_folder, folder)
    shutil.rmtree(folder_path)

# Tracks data for Metal, Disco and Reggae
tracks_data = pd.read_csv(tracks_file, header=[0, 1, 2], low_memory=False)
tracks_data = tracks_data.drop(tracks_data.iloc[:, 1:40], axis=1)  # Drop column 1-40
tracks_data = tracks_data.drop(tracks_data.iloc[:, 3:14], axis=1)  # Drop column 3-14
tracks_data.columns = ['_'.join(col) for col in tracks_data.columns.values]  # Merge Headers
tracks_columns_list = ['track_id', 'label', 'genres']
tracks_data.columns = tracks_columns_list  # Rename Column Header
tracks_data['track_id'] = tracks_data['track_id'].astype(str).str.zfill(6)  # Add leading zeros to track_id
print("Tracks data: ")
print(tracks_data)

# Filter for FMA Genres for GTZAN Genres (See FMA genres.csv @ https://github.com/mdeff/fma &
# GTZAN genres @ https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification)

# Blues
blues_tracks_data = tracks_data[tracks_data['genres'].isin(['[3]'])]
# Additional Disco Tracks
additional_blues_tracks_data = tracks_data[tracks_data['genres'].str.startswith('[3,')
                                           & tracks_data['genres'].str.endswith(']')]
# Classical
classical_tracks_data = tracks_data[tracks_data['genres'].isin(['[5]'])]
# Additional Classical Tracks
additional_classical_tracks_data = tracks_data[tracks_data['genres'].str.startswith('[5,')
                                               & tracks_data['genres'].str.endswith(']')]
# Country, Country & Western
country_tracks_data = tracks_data[tracks_data['genres'].isin(['[9]', '[651]'])]
# Additional Country Tracks
additional_country_tracks_data = tracks_data[tracks_data['genres'].str.startswith('[9,')
                                             & tracks_data['genres'].str.endswith(']')]
# Disco
disco_tracks_data = tracks_data[tracks_data['genres'].isin(['[11]'])]
# Additional Disco Tracks
additional_disco_tracks_data = tracks_data[tracks_data['genres'].str.startswith('[11,')
                                           & tracks_data['genres'].str.endswith(']')]
# Hip-Hop, Alternative Hip-Hop, Abstract Hip-Hop, Hip-Hop Beats
hipHop_tracks_data = tracks_data[tracks_data['genres'].isin(['[21]', '[100]', '[580]', '[811]'])]
# Jazz, Jazz: Vocal, Free-Jazz, Jazz: Out, Modern Jazz
jazz_tracks_data = tracks_data[tracks_data['genres'].isin(['[4]', '[37]', '[74]', '[97]', '[906]'])]
# Additional Jazz Tracks
additional_jazz_tracks_data = tracks_data[tracks_data['genres'].str.contains(r'\[4,|\[37,|\[74,|\[97,|\[906,',
                                                                             regex=True)]
# Metal, Death-Metal, Black-Metal
metal_tracks_data = tracks_data[tracks_data['genres'].isin(['[31]', '[101]', '[167]'])]
# Additional Metal Tracks
additional_metal_tracks_data = tracks_data[tracks_data['genres'].str.contains(r'\[31,|\[101,|\[167,', regex=True)]
# Pop, Experimental Pop, Synth-Pop
pop_tracks_data = tracks_data[tracks_data['genres'].isin(['[10]', '[76]', '[111]', '[362]'])]
# Reggae - Dub, Reggae - Dancehall
reggae_tracks_data = tracks_data[tracks_data['genres'].isin(['[79]', '[602]'])]
# Additional Reggae Tracks
additional_reggae_tracks_data = tracks_data[tracks_data['genres'].str.contains(r'\[79,|\[602,', regex=True)]
# Rock, Post-Rock, Krautrock, Loud-Rock, Noise-Rock, Psych-Rock, Indie-Rock, Space-Rock, Rock-Opera
rock_tracks_data = tracks_data[tracks_data['genres'].isin(['[12]', '[26]', '[36]', '[45]', '[53]', '[58]', '[66]',
                                                           '[113]', '[440]'])]

# Move Blues Songs
for index, row in blues_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/blues/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Additional Blues Songs
for index, row in additional_blues_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/blues/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Classical Songs
for index, row in classical_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/classical/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Additional Classical Songs
for index, row in additional_classical_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/classical/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Country Songs
for index, row in country_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/country/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Additional Country Songs
for index, row in additional_country_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/country/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Disco Songs
for index, row in disco_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/disco/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Additional Disco Songs
for index, row in additional_disco_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/disco/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Hip-Hop Songs
for index, row in hipHop_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/hiphop/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Jazz Songs
for index, row in jazz_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/jazz/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Additional Jazz Songs
for index, row in additional_jazz_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/jazz/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Metal Songs
for index, row in metal_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/metal/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Additional Metal Songs
for index, row in additional_metal_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/metal/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Pop Songs
for index, row in pop_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/pop/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Reggae Songs
for index, row in reggae_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/reggae/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Additional Reggae Songs
for index, row in additional_reggae_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/reggae/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Rock Songs
for index, row in rock_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/rock/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# .mp3 to .wav conversion (pip install ffmpeg-downloader) & (ffdl install --add-path) required

# Specify folder path containing the .mp3 files
folder_path_blues = "C:/Users/Dominik/PycharmProjects/Neural-Network/data/blues/"
folder_path_classical = "C:/Users/Dominik/PycharmProjects/Neural-Network/data/classical/"
folder_path_country = "C:/Users/Dominik/PycharmProjects/Neural-Network/data/country/"
folder_path_disco = "C:/Users/Dominik/PycharmProjects/Neural-Network/data/disco/"
folder_path_hiphop = "C:/Users/Dominik/PycharmProjects/Neural-Network/data/hiphop/"
folder_path_jazz = "C:/Users/Dominik/PycharmProjects/Neural-Network/data/jazz/"
folder_path_metal = "C:/Users/Dominik/PycharmProjects/Neural-Network/data/metal/"
folder_path_pop = "C:/Users/Dominik/PycharmProjects/Neural-Network/data/pop/"
folder_path_reggae = "C:/Users/Dominik/PycharmProjects/Neural-Network/data/reggae/"
folder_path_rock = "C:/Users/Dominik/PycharmProjects/Neural-Network/data/rock/"


def convert_mp3_to_wav(mp3_path, wav_path):
    audio = AudioSegment.from_mp3(mp3_path)
    audio.export(wav_path, format="wav")


def convert_folder_files(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".mp3"):
            mp3_path = os.path.join(folder, filename)
            wav_path = os.path.join(folder, os.path.splitext(filename)[0] + ".wav")
            convert_mp3_to_wav(mp3_path, wav_path)


# Convert .mp3 files in the folders to WAV
convert_folder_files(folder_path_blues)
convert_folder_files(folder_path_classical)
convert_folder_files(folder_path_country)
convert_folder_files(folder_path_disco)
convert_folder_files(folder_path_hiphop)
convert_folder_files(folder_path_jazz)
convert_folder_files(folder_path_metal)
convert_folder_files(folder_path_pop)
convert_folder_files(folder_path_reggae)
convert_folder_files(folder_path_rock)