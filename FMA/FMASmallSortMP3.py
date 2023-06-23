import os
import shutil
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

# Check if data folder already exist
dataIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data")

# Check if fma_small genre folders already exist
electronicIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data/electronic")
experimentalIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data/experimental")
folkIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data/folk")
hipHopIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data/hiphop")
instrumentalIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data/instrumental")
internationalIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data/international")
popIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data/pop")
rockIsExist = os.path.exists("C:/Users/Dominik/PycharmProjects/Neural-Network/data/rock")

if not dataIsExist:
    # Create data folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data")
    print("Data folder created.")
if not folkIsExist:
    # Create folk folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data/folk")
    print("Folk folder created.")
if not experimentalIsExist:
    # Create Experimental folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data/experimental")
    print("Experimental folder created.")
if not internationalIsExist:
    # Create International folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data/international")
    print("International folder created.")
if not electronicIsExist:
    # Create Electronic folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data/electronic")
    print("Electronic folder created.")
if not instrumentalIsExist:
    # Create Instrumental folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data/instrumental")
    print("Instrumental folder created.")
if not hipHopIsExist:
    # Create hiphop folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data/hiphop")
    print("HipHop folder created.")
if not popIsExist:
    # Create pop folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data/pop")
    print("Pop folder created.")
if not rockIsExist:
    # Create rock folder
    os.makedirs("C:/Users/Dominik/PycharmProjects/Neural-Network/data/rock")
    print("Rock folder created.")

# Filter for fma small genres
electronic_tracks_data = tracks_data[tracks_data['label'].isin(['Electronic'])]
experimental_tracks_data = tracks_data[tracks_data['label'].isin(['Experimental'])]
folk_tracks_data = tracks_data[tracks_data['label'].isin(['Folk'])]
hiphop_tracks_data = tracks_data[tracks_data['label'].isin(['Hip-Hop'])]
instrumental_tracks_data = tracks_data[tracks_data['label'].isin(['Instrumental'])]
international_tracks_data = tracks_data[tracks_data['label'].isin(['International'])]
pop_tracks_data = tracks_data[tracks_data['label'].isin(['Pop'])]
rock_tracks_data = tracks_data[tracks_data['label'].isin(['Rock'])]

# Move Songs from child to root directories
parent_folder = "C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_small"
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
    shutil.rmtree(folder_path)

# Move Electronic Songs
for index, row in electronic_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_small/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/electronic/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Experimental Songs
for index, row in experimental_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_small/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/experimental/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Folk Songs
for index, row in folk_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_small/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/folk/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Hip-Hop Songs
for index, row in hiphop_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_small/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/hiphop/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Instrumental Songs
for index, row in instrumental_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_small/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/instrumental/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move International Songs
for index, row in international_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_small/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/international/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Pop Songs
for index, row in pop_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_small/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/pop/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')

# Move Rock Songs
for index, row in rock_tracks_data.iterrows():
    track_id = row['track_id']
    print(track_id)
    old_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/fma_small/{track_id}.mp3'
    new_file = f'C:/Users/Dominik/PycharmProjects/Neural-Network/data/rock/{track_id}.mp3'
    try:
        shutil.move(old_file, new_file)
        print('File Exists')
    except (Exception,):
        print('File does not Exist')
