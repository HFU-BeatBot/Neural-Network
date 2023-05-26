import os
import shutil
import pandas as pd

# Paths to the file
tracks_file = "C:/Users/Dominik/Desktop/FMA/fma_metadata/tracks.csv"

# Drop everything in tracks_file but track_id & genre_top
tracks_data = pd.read_csv(tracks_file, header=[0, 1, 2], low_memory=False)
tracks_data = tracks_data.drop(tracks_data.iloc[:, 1:40], axis=1)  # Drop column 1-40
tracks_data = tracks_data.drop(tracks_data.iloc[:, 2:14], axis=1)  # Drop column 2-14

# Change column names + merge header
tracks_data.columns = ['_'.join(col) for col in tracks_data.columns.values]  # Merge Headers
tracks_columns_list = ['track_id', 'label']
tracks_data.columns = tracks_columns_list  # Rename Column Header
print("Tracks dataframe: ", "\n")
print(tracks_data, "\n")

# Add leading zeros
tracks_data['track_id'] = tracks_data['track_id'].astype(str).str.zfill(6)

# Check if data folders already exist
dataIsExist = os.path.exists("C:/Users/Dominik/Desktop/FMA/data")
bluesIsExist = os.path.exists("C:/Users/Dominik/Desktop/FMA/data/blues")
classicalIsExist = os.path.exists("C:/Users/Dominik/Desktop/FMA/data/classical")
countryIsExist = os.path.exists("C:/Users/Dominik/Desktop/FMA/data/country")
discoIsExist = os.path.exists("C:/Users/Dominik/Desktop/FMA/data/disco")
hipHopIsExist = os.path.exists("C:/Users/Dominik/Desktop/FMA/data/hiphop")
jazzIsExist = os.path.exists("C:/Users/Dominik/Desktop/FMA/data/jazz")
metalIsExist = os.path.exists("C:/Users/Dominik/Desktop/FMA/data/metal")
popIsExist = os.path.exists("C:/Users/Dominik/Desktop/FMA/data/pop")
reggaeIsExist = os.path.exists("C:/Users/Dominik/Desktop/FMA/data/reggae")
rockIsExist = os.path.exists("C:/Users/Dominik/Desktop/FMA/data/rock")
if not dataIsExist:
    # Create data folder
    os.makedirs("C:/Users/Dominik/Desktop/FMA/data")
    print("Data folder created.")
if not bluesIsExist:
    # Create blues folder
    os.makedirs("C:/Users/Dominik/Desktop/FMA/data/blues")
    print("Blues folder created.")
if not classicalIsExist:
    # Create classical folder
    os.makedirs("C:/Users/Dominik/Desktop/FMA/data/classical")
    print("Classical folder created.")
if not countryIsExist:
    # Create country folder
    os.makedirs("C:/Users/Dominik/Desktop/FMA/data/country")
    print("Country folder created.")
if not discoIsExist:
    # Create disco folder
    os.makedirs("C:/Users/Dominik/Desktop/FMA/data/disco")
    print("Disco folder created.")
if not hipHopIsExist:
    # Create hiphop folder
    os.makedirs("C:/Users/Dominik/Desktop/FMA/data/hiphop")
    print("HipHop folder created.")
if not jazzIsExist:
    # Create jazz folder
    os.makedirs("C:/Users/Dominik/Desktop/FMA/data/jazz")
    print("Jazz folder created.")
if not metalIsExist:
    # Create metal folder
    os.makedirs("C:/Users/Dominik/Desktop/FMA/data/metal")
    print("Metal folder created.")
if not popIsExist:
    # Create pop folder
    os.makedirs("C:/Users/Dominik/Desktop/FMA/data/pop")
    print("Pop folder created.")
if not reggaeIsExist:
    # Create reggae folder
    os.makedirs("C:/Users/Dominik/Desktop/FMA/data/reggae")
    print("Reggae folder created.")
if not rockIsExist:
    # Create rock folder
    os.makedirs("C:/Users/Dominik/Desktop/FMA/data/rock")
    print("Rock folder created.")

# Filter for genres
rock_tracks_data = tracks_data[tracks_data['label'].isin(['Rock'])]
blues_tracks_data = tracks_data[tracks_data['label'].isin(['Blues'])]
classical_tracks_data = tracks_data[tracks_data['label'].isin(['Classical'])]
country_tracks_data = tracks_data[tracks_data['label'].isin(['Country'])]
disco_tracks_data = tracks_data[tracks_data['label'].isin(['Disco'])]
hiphop_tracks_data = tracks_data[tracks_data['label'].isin(['Hip-Hop'])]
jazz_tracks_data = tracks_data[tracks_data['label'].isin(['Jazz'])]
metal_tracks_data = tracks_data[tracks_data['label'].isin(['Metal'])]
pop_tracks_data = tracks_data[tracks_data['label'].isin(['Pop'])]
reggae_tracks_data = tracks_data[tracks_data['label'].isin(['Reggae - Dub'])]

# Move Rock Songs
for index, row in rock_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/Desktop/FMA/fma_medium/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/Desktop/FMA/data/rock/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Blues Songs
for index, row in blues_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/Desktop/FMA/fma_medium/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/Desktop/FMA/data/blues/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Classical Songs
for index, row in classical_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/Desktop/FMA/fma_medium/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/Desktop/FMA/data/classical/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Country Songs
for index, row in country_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/Desktop/FMA/fma_medium/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/Desktop/FMA/data/country/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Disco Songs
for index, row in disco_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/Desktop/FMA/fma_medium/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/Desktop/FMA/data/disco/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Hip-Hop Songs
for index, row in hiphop_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/Desktop/FMA/fma_medium/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/Desktop/FMA/data/hiphop/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Jazz Songs
for index, row in jazz_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/Desktop/FMA/fma_medium/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/Desktop/FMA/data/jazz/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Metal Songs
for index, row in metal_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/Desktop/FMA/fma_medium/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/Desktop/FMA/data/metal/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Pop Songs
for index, row in pop_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/Desktop/FMA/fma_medium/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/Desktop/FMA/data/pop/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Reggae Songs
for index, row in reggae_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/Desktop/FMA/fma_medium/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/Desktop/FMA/data/reggae/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')