import os
import shutil
from os.path import join
import pandas as pd

# Paths to the file
tracks_file = 'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_metadata/tracks.csv'

# Drop everything in tracks_file but track_id & genre_top
tracks_data = pd.read_csv(tracks_file, header=[0, 1, 2], low_memory=False)
tracks_data = tracks_data.drop(tracks_data.iloc[:, 1:40], axis=1)  # Drop column 1-40
tracks_data = tracks_data.drop(tracks_data.iloc[:, 2:14], axis=1)  # Drop column 2-14

# Change column names + merge header
tracks_data.columns = ['_'.join(col) for col in tracks_data.columns.values]  # Merge Headers
tracks_columns_list = ['track_id', 'label']
tracks_data.columns = tracks_columns_list  # Rename Column Header
tracks_data['track_id'] = tracks_data['track_id'].astype(str).str.zfill(6)  # Add leading zeros to track_id
print("Tracks dataframe: ", "\n")
print(tracks_data, "\n")

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

# Filter for genres
rock_tracks_data = tracks_data[tracks_data['label'].isin(['Rock'])]
blues_tracks_data = tracks_data[tracks_data['label'].isin(['Blues'])]
classical_tracks_data = tracks_data[tracks_data['label'].isin(['Classical'])]
country_tracks_data = tracks_data[tracks_data['label'].isin(['Country'])]
hiphop_tracks_data = tracks_data[tracks_data['label'].isin(['Hip-Hop'])]
jazz_tracks_data = tracks_data[tracks_data['label'].isin(['Jazz'])]
pop_tracks_data = tracks_data[tracks_data['label'].isin(['Pop'])]

# Move Songs from child to root directories
'''parent_folder = "C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large"

child_folders = [folder for folder in os.listdir(parent_folder)     # Get a list of all child folders
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
    shutil.rmtree(folder_path)'''

# Tracks data for Metal, Disco and Reggae
tracks_data2 = pd.read_csv(tracks_file, header=[0, 1, 2], low_memory=False)
tracks_data2 = tracks_data2.drop(tracks_data2.iloc[:, 1:40], axis=1)  # Drop column 1-40
tracks_data2 = tracks_data2.drop(tracks_data2.iloc[:, 3:14], axis=1)  # Drop column 3-14
tracks_data2.columns = ['_'.join(col) for col in tracks_data2.columns.values]  # Merge Headers
tracks_columns_list = ['track_id', 'label', 'genres']
tracks_data2.columns = tracks_columns_list  # Rename Column Header
tracks_data2['track_id'] = tracks_data2['track_id'].astype(str).str.zfill(6)  # Add leading zeros to track_id
print("Tracks data 2: ")
print(tracks_data2)

# Filter for extra genres
metal_tracks_data = tracks_data2[tracks_data2['genres'].isin(['[31]', '[101]', '[167]'])]
reggae_tracks_data = tracks_data2[tracks_data2['genres'].isin(['[79]', '[602]'])]
disco_tracks_data = tracks_data2[tracks_data2['genres'].isin(['[11]'])]

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

# Move Hip-Hop Songs
for index, row in hiphop_tracks_data.iterrows():
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

# Move Metal Songs
for index, row in metal_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_large/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/metal/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists Metal to Metal Folder')
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
