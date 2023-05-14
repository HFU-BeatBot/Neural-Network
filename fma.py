import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import to_categorical

# Pfade zu den Dateien
''' features_file = "C:/Users/Nahed/Desktop/New-NN/fma/data/fma_metadata/features.csv"
tracks_file = "C:/Users/Nahed/Desktop/New-NN/fma/data/fma_metadata/tracks.csv"
genres_file = "C:/Users/Nahed/Desktop/New-NN/fma/data/fma_metadata/genres.csv" '''
features_file = "C:/Users/Domi/Desktop/FMA/fma_metadata/features.csv"
tracks_file = "C:/Users/Domi/Desktop/FMA/fma_metadata/tracks.csv"
genres_file = "C:/Users/Domi/Desktop/FMA/fma_metadata/genres.csv"



# Einlesen die .csv-Dateien
features_df = pd.read_csv(features_file, index_col=0, header=[0, 1, 2])
tracks_df = pd.read_csv(tracks_file, index_col=0, header=[0, 1])
genres_df = pd.read_csv(genres_file, index_col=0)


# Filtern der MFCC-Daten (Mean und Standardabweichung)
mfcc_data = features_df.loc[:, pd.IndexSlice["mfcc", ["mean", "std"]]]

# Umstrukturierung des MultiIndex
mfcc_data.columns = [f"{feature}_{stat}_{number}" for feature, stat, number in mfcc_data.columns]

# Ausgabe der MFCC-Daten
print("tracks_df", tracks_df)
print("genres_df", genres_df)
print("mfcc_data", mfcc_data)

# Filtere die Genres basierend auf der Spalte "parent"
#  genres = ['Blues', 'Classical', 'Country', 'Disco', 'Hiphop', 'Jazz', 'Metal', 'Pop', 'Reggae', 'Rock']
genres = ['Experimental', 'Electronic', 'Rock', 'Instrumental', 'Pop', 'Folk', 'Hip-Hop', 'International', 'Jazz'
          'Classical', 'Country', 'Spoken', 'Blues', 'Soul-RnB', 'Old-Time / Historic']
filtered_genres_df = genres_df[genres_df['title'].isin(genres)]
filtered_genres_df = filtered_genres_df.sort_values(by=['#tracks'], ascending=True)
filtered_genres_df.to_csv('filtered_genres.csv', sep=',')  # csv mit Anzahl an Tracks pro Genre

# Top Level Genres
''' print('{} top-level genres'.format(len(genres_file['top_level'].unique())))
genres_file.loc[genres['top_level'].unique()].sort_values('#tracks', ascending=False) '''


# Gebe die gefilterten Genres aus
print("filtered_genres_df", filtered_genres_df)

# Extrahieren der relevanten Spalten aus der tracks.csv-Datei
tracks_metadata = tracks_df[("track", "genre_top")]

# Filtern der Zeilen basierend auf den gewünschten Genres
filtered_tracks = tracks_df[tracks_metadata.isin(filtered_genres_df)]

# Ausgabe der gefilterten Tracks
print("filtered_tracks", filtered_tracks)

# Extrahieren der Features für die gefilterten Tracks
filtered_features = mfcc_data.loc[filtered_genres_df.index]
print("filtered_features", filtered_features)

# Extrahieren der Zielvariablen (Genre Labels)
labels = filtered_tracks[("track", "genre_top")].values
print("labels", labels)

# Aufteilen der Daten in Trainings- und Testsets
X_train, X_test, y_train, y_test = train_test_split(filtered_features, labels, test_size=0.1)

# Skalierung der Daten
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Label-Encoding der Zielvariablen
encoder = LabelEncoder()
y_train_encoded = encoder.fit_transform(y_train)
y_test_encoded = encoder.transform(y_test)

# One-Hot-Encoding der Zielvariablen
y_train_encoded = to_categorical(y_train_encoded)
y_test_encoded = to_categorical(y_test_encoded)

# Erstellen des neuronalen Netzwerkmodells
model = Sequential()
model.add(Dense(256, activation='relu', input_shape=(X_train_scaled.shape[1],)))
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(filtered_genres_df), activation='softmax'))

# Kompilieren des Modells
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Training des Modells
model.fit(X_train_scaled, y_train_encoded, validation_data=(X_test_scaled, y_test_encoded), epochs=10, batch_size=128)