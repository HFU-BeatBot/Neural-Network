import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import to_categorical

# Paths to the files
features_file = "data/fma_metadata/features.csv"
tracks_file = "data/fma_metadata/tracks.csv"
genres_file = "data/fma_metadata/genres.csv"

# Read the .csv files
features_df = pd.read_csv(features_file, index_col=0, header=[0, 1, 2])
tracks_df = pd.read_csv(tracks_file, index_col=0, header=[0, 1])
genres_df = pd.read_csv(genres_file, index_col=0)

# Filter the MFCC data (mean and standard deviation)
mfcc_data = features_df.loc[:, pd.IndexSlice["mfcc", ["mean", "std"]]]

# Restructure the MultiIndex
mfcc_data.columns = [f"{feature}_{stat}_{number}" for feature, stat, number in mfcc_data.columns]

# Output the MFCC data
print("tracks_df", tracks_df)
print("genres_df", genres_df)
print("mfcc_data", mfcc_data)

# Extract the relevant columns from the tracks.csv file
#tracks_metadata = tracks_df[("track", "genre_top")]

# Filter the rows based on the desired genres
#filtered_tracks = tracks_df[tracks_metadata.isin(filtered_genres)]

# Output the filtered tracks
#print("filtered_tracks", filtered_tracks)

# Extract the features for the filtered tracks
#filtered_features = mfcc_data.loc[genres_df.index]
#print("filtered_features", filtered_features)


# Extract the target variables (Genre Labels)
labels = tracks_df[("track", "genre_top")].values
print("labels", labels)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(mfcc_data, labels, test_size=0.2, random_state=42)

# Scale the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Label encode the target variables
encoder = LabelEncoder()
y_train_encoded = encoder.fit_transform(y_train)
y_test_encoded = encoder.transform(y_test)
y_train_encoded = to_categorical(y_train_encoded)
y_test_encoded = to_categorical(y_test_encoded)

# Number of different categories
num_categories = y_train_encoded.shape[1]
print("num_categories", num_categories)

# Create the neural network model
model = Sequential()
model.add(Dense(256, activation='relu', input_shape=(X_train_scaled.shape[1],)))
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_categories, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train_scaled, y_train_encoded, validation_data=(X_test_scaled, y_test_encoded), epochs=10, batch_size=128)

# Calculate accuracy on the training dataset
_, train_accuracy = model.evaluate(X_train_scaled, y_train_encoded, verbose=0)
print("Train Accuracy", train_accuracy)

# Calculate accuracy on the test dataset
_, test_accuracy = model.evaluate(X_test_scaled, y_test_encoded, verbose=0)
print("Test Accuracy", test_accuracy)

# Save the model
model.save("fma_model.h5")