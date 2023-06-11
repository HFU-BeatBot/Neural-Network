# Neural-Network
The neural-network which decides what genre the given song belongs to.

## Setup

```
pip install -r requirements.txt
```

## Introduction
This project focuses on music genre classification using neural networks.

It involves two models: one trained on the GTZAN dataset and another trained on the FMA dataset.
The workflow for both models is similar, and the goal is the same - to classify music genres.

## Datasets
### GTZAN Dataset
- A collection of 10 genres with 100 audio files each, all having a length of 30 seconds
- 10 genres: blues, classical, country, disco, hiphop, jazz, metal, pop, reggae and rock
- Download the GTZAN Dataset from this site: https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification

### FMA (Free Music Archive) Dataset
- A collection of 10 genres with more than 100 audio files each, all having a length of 30 seconds
- 10 genres: blues, classical, country, disco, hiphop, jazz, metal, pop, reggae and rock
- All metadata and features for all tracks are distributed in fma_metadata.zip (342 MiB).
- Download this Data-Package from this link directly: https://os.unil.cloud.switch.ch/fma/fma_metadata.zip or visit this site: https://github.com/mdeff/fma

- tracks.csv: per track metadata such as ID, title, artist, genres, tags and play counts, for all 106,574 tracks.
- genres.csv: all 163 genres with name and parent (used to infer the genre hierarchy and top-level genres).
- features.csv: common features extracted with librosa. 

## Code
The Python codes are available in both the FMA and GTZAN folders with slight modifications.

### createDataMFCC.py:
This code generates a dataset in the form of a CSV file (data.csv) with MFCC (Mel-frequency Cepstral Coefficients) features extracted from audio files.
The CSV file is created in the "data" folder.

### createModelMFCC.py
- Defines the architecture of a neural network model for genre classification.
- Performs training of the model, evaluation of its performance, prediction on test data, and saving the trained model. 
- Generates visualizations to illustrate the training process and model performance. 
- The neural network model consists of multiple dense layers with ReLU activation functions. 
- Dropout layers are included to prevent overfitting. 
- The output layer uses softmax activation for multi-class classification. 
- The trained model is saved as model.h5, and visualizations are saved as .png and .bin files.

### createSongModelMFCC.py
In this code, we are loading an audio file named '50 Cent - In Da Club.wav'. 
The Goal here is to print the genre label from the Song. 

### createSplittedSongs.py
- Loads audio files from the specified genres folder and creates snippets of 5-second duration.
- Extracts MFCC features from each snippet and scales the features using a StandardScaler. 
- Makes predictions using the trained model and saves the snippet paths and predicted genres in a CSV file. 

For the FMA data
- The resulting CSV file is saved as SplittedSong.csv in the "FMA_Splitted_Songs" folder.

For the GTZAN data
- The resulting CSV file is saved as SplittedSong.csv in the "GTZAN_Splitted_Songs" folder.

### filterFMAData.py
The goal of this code is to filter the Data from the FMA dataset. 

- In the variable filtered_tracks_data, the tracks were filtered to keep only those belonging to the selected genres. 
The selected genres are: 'Blues', 'Classical', 'Country', 'Disco', 'Hip-Hop', 'Jazz', 'Metal', 'Pop', 'Reggae - Dub', and 'Rock'. 
This filtering was based on the 'label' column in the "tracks_data" DataFrame.
- In the variable genres_data, the genres were filtered to keep only those genres that belong to the selected genres. 
This filtering was based on the 'title' column in the "genres_data" DataFrame.
- In the variable merged_genres, the data from the merged_data and genres_data DataFrames was further filtered to keep only the data for the selected genres. 
The 'label' column was used for this filtering.

### Usage
1. Ensure that you have the required dependencies installed.
2. Download the dataset and place the necessary files in the "data" directory,for both GTZAN and FMA.
3. Run the code to train the model and evaluate its accuracy on the test dataset.
4. The trained model will be saved as ".h5" Format for future use.


# TO BE COTINUED