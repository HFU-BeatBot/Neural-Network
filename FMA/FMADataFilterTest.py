import pandas as pd

# Paths to the files
old_features_file = "C:/Users/Dominik/PycharmProjects/Neural-Network/data.csv"
features_file = "C:/Users/Dominik/Desktop/FMA/fma_metadata/features.csv"
tracks_file = "C:/Users/Dominik/Desktop/FMA/fma_metadata/tracks.csv"
genres_file = "C:/Users/Dominik/Desktop/FMA/fma_metadata/genres.csv"
folder_path = "C:/Users/Dominik/Desktop/FMA/fma_medium"

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

# Filter out rows without explicit genre
genres = ['Blues', 'Classical', 'Country', 'Disco', 'Hip-Hop'
          'Jazz', 'Metal', 'Pop', 'Reggae - Dub', 'Rock']
filtered_tracks_data = tracks_data[tracks_data['label'].isin(genres)]
print("Filtered Tracks dataframe: ", "\n")
print(filtered_tracks_data, "\n")

# top_level genres + metal variations in genres.csv
genres_extended = ['Electronic', 'Rock', 'Instrumental', 'Pop', 'Folk', 'Hip-Hop', 'International',
                   'Jazz', 'Classical', 'Country', 'Spoken', 'Blues', 'Soul-RnB', 'Metal',
                   'Death-Metal', 'Black-Metal', 'Country', 'Disco', 'Reggae - Dub']
genres_data = pd.read_csv(genres_file, low_memory=False)
genres_data = genres_data[genres_data['title'].isin(genres_extended)]
genres_data = genres_data.sort_values(by=['#tracks'])  # sort by number of tracks
print("Genres dataframe: ", "\n")
print(genres_data, "\n")

# Filter out track_id & mfcc std & mean in features.csv
features_data = pd.read_csv(features_file, sep=';', header=[0, 1, 2, 3, 4], low_memory=False)
features_data = features_data.drop(features_data.iloc[:, 1:293], axis=1)  # Drop column 1-293 (293-313 mfcc mean)
features_data = features_data.drop(features_data.iloc[:, 21:81], axis=1)  # Drop column 21-81
features_data = features_data.drop(features_data.iloc[:, 41:168], axis=1)  # Only track_id, mfcc_mean & mfcc_std left

# Reformat header to single index
features_data.columns = ['_'.join(col) for col in features_data.columns.values]  # Merge Headers
columns = ['track_id', 'mfcc1_mean', 'mfcc2_mean', 'mfcc3_mean', 'mfcc4_mean', 'mfcc5_mean', 'mfcc6_mean',
           'mfcc7_mean', 'mfcc8_mean', 'mfcc9_mean', 'mfcc10_mean', 'mfcc11_mean', 'mfcc12_mean', 'mfcc13_mean',
           'mfcc14_mean', 'mfcc15_mean', 'mfcc16_mean', 'mfcc17_mean', 'mfcc18_mean', 'mfcc19_mean', 'mfcc20_mean',
           'mfcc1_std', 'mfcc2_std', 'mfcc3_std', 'mfcc4_std', 'mfcc5_std', 'mfcc6_std', 'mfcc7_std', 'mfcc8_std',
           'mfcc9_std', 'mfcc10_std', 'mfcc11_std', 'mfcc12_std', 'mfcc13_std', 'mfcc14_std', 'mfcc15_std',
           'mfcc16_std', 'mfcc17_std', 'mfcc18_std', 'mfcc19_std', 'mfcc20_std']
features_data.columns = columns  # Rename Column Header
print("Filtered Features dataframe: ", "\n")
print(features_data, "\n")

# Merge tracks_data and features_data
merged_data = pd.concat([features_data, tracks_data], axis=1, join='inner')  # Merge Data Frames
merged_data = merged_data.drop(merged_data.columns[41], axis=1)  # Drop duplicate track_id
rearranged_columns = ['mfcc1_mean', 'mfcc1_std', 'mfcc2_mean', 'mfcc2_std', 'mfcc3_mean', 'mfcc3_std',
                      'mfcc4_mean', 'mfcc4_std', 'mfcc5_std', 'mfcc5_mean', 'mfcc6_mean', 'mfcc6_std', 'mfcc7_mean',
                      'mfcc7_std', 'mfcc8_mean', 'mfcc8_std', 'mfcc9_mean', 'mfcc9_std', 'mfcc10_mean', 'mfcc10_std',
                      'mfcc11_mean', 'mfcc11_std', 'mfcc12_mean', 'mfcc12_std', 'mfcc13_mean', 'mfcc13_std',
                      'mfcc14_mean', 'mfcc14_std', 'mfcc15_mean', 'mfcc15_std', 'mfcc16_mean', 'mfcc16_std',
                      'mfcc17_mean', 'mfcc17_std', 'mfcc18_mean', 'mfcc18_std', 'mfcc19_mean', 'mfcc19_std',
                      'mfcc20_mean', 'mfcc20_std', 'label']
merged_data = merged_data[rearranged_columns]  # Rearrange Columns
print("Merged dataframe: ", "\n")
print(merged_data)

# Filtering by 10 "old" genres
genres_old = ['Blues', 'Classical', 'Country', 'Disco', 'Hip-Hop', 'Jazz', 'Metal', 'Death-Metal', 'Black-Metal', 'Pop',
              'Reggae - Dub', 'Rock']
merged_old_genres_data = merged_data[merged_data['label'].isin(genres_old)]
merged_old_genres_data = merged_old_genres_data.sort_values('label')  # Sort by column label
merged_old_genres_data = merged_old_genres_data.replace({  # Replace old genre formatting with new one
    'label': {
        'Blues': 'blues',
        'Classical': 'classical',
        'Country': 'country',
        'Disco': 'disco',
        'Hip-Hop': 'hiphop',
        'Jazz': 'jazz',
        'Metal': 'metal',
        'Pop': 'pop',
        'Reggae - Dub': 'reggae',
        'Rock': 'rock'
    }
})
print("\n", "Old genres merged dataframe", "\n")
print(merged_old_genres_data)

# Reading and formatting old Data
old_features_data = pd.read_csv(old_features_file, low_memory=False)
old_features_data = old_features_data.drop(['filename'], axis=1)  # Dropping column filename
print("\n", "Old features dataframe", "\n")
print(old_features_data)

# Merge old_features_data & merged old genres data
final_ten_genres_data = pd.concat([old_features_data, merged_old_genres_data], axis=0)  # Merge Data Frames
print("\n", "Final 10 genres dataframe", "\n")
print(final_ten_genres_data)

# Writing merged dataframe to .csv
final_ten_genres_data.to_csv('ten_genres_old_plus_fma_data.csv')  # Write to csv without line numbering

# Filtering by 16 "new" genres
genres_new = ['Experimental', 'Electronic', 'Rock', 'Instrumental', 'Pop', 'Folk', 'Hip-Hop', 'International', 'Jazz',
              'Classical', 'Country', 'Spoken', 'Blues', 'Soul-RnB', 'Old-Time/Historic', 'Easy Listening']
merged_new_genres_data = merged_data[merged_data['label'].isin(genres_new)]
merged_new_genres_data = merged_new_genres_data.sort_values('label')  # Sort by column label
print("\n", "New genres merged dataframe", "\n")
print(merged_new_genres_data)
