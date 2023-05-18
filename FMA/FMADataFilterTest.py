import pandas as pd

# Paths to the files
features_file = "C:/Users/Dominik/Desktop/FMA/fma_metadata/features.csv"
tracks_file = "C:/Users/Dominik/Desktop/FMA/fma_metadata/tracks.csv"
genres_file = "C:/Users/Dominik/Desktop/FMA/fma_metadata/genres.csv"

# Drop everything in tracks_file but track_id & genre_top
tracks_data = pd.read_csv(tracks_file, low_memory=False)
tracks_data = tracks_data.drop(tracks_data.iloc[:, 1:40], axis=1)  # Drop column 1-40
tracks_data = tracks_data.drop(tracks_data.iloc[:, 2:14], axis=1)  # Drop column 2-14

# Get column names
column_headers_tracks = list(tracks_data.columns.values)
# print("The Column Header for tracks :", column_headers_tracks)

# Change column names + drop first 2 rows
tracks_data = tracks_data.rename(columns={'Unnamed: 0': 'track_id', 'track.7': 'genre_top'})
tracks_data = tracks_data.tail(-2)  # Drop first 2 rows

# Filter out rows without explicit genre
genres = ['Electronic', 'Rock', 'Instrumental', 'Pop', 'Folk', 'Hip-Hop', 'International', 'Jazz'
          'Classical', 'Country', 'Spoken', 'Blues', 'Soul-RnB']
filtered_tracks_data = tracks_data[tracks_data['genre_top'].isin(genres)]
print(filtered_tracks_data)

#  Es gibt viele tracks mit mehreren Genre in tracks.csv
#  Waere jetzt die Frage ob wir die rausfiltern oder was wir mit denen machen

# Overview of top_level genres in genres.csv
genres_extended = ['Electronic', 'Rock', 'Instrumental', 'Pop', 'Folk', 'Hip-Hop', 'International',
                   'Jazz', 'Classical', 'Country', 'Spoken', 'Blues', 'Soul-RnB', 'Metal',
                   'Death-Metal', 'Black-Metal', 'Country', 'Disco', 'Reggae - Dub']
genres_data = pd.read_csv(genres_file, low_memory=False)
genres_data = genres_data[genres_data['title'].isin(genres_extended)]
genres_data = genres_data.sort_values(by=['#tracks'], ascending=True)  # sort by number of tracks
print(genres_data)

#  Metal ist in der top_level category Rock
#  Disco nur 300 Songs
#  Reggae - Dub 880 Songs

# Filter out track_id & mfcc std & mean in features.csv
features_data = pd.read_csv(features_file, sep=';', header=[0, 1, 2, 3], low_memory=False)
features_data = features_data.drop(features_data.iloc[:, 1:293], axis=1)  # Drop column 1-293 (293-313 mfcc mean)
features_data = features_data.drop(features_data.iloc[:, 21:81], axis=1)  # Drop column 21-81
features_data = features_data.drop(features_data.iloc[:, 41:168], axis=1)  # Only track_id, mfcc_mean & mfcc_std left
#  column_headers_features = list(features_data.columns.values)
#  print("The Column Header for tracks :", column_headers_features)
print(features_data)
