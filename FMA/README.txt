
## Music Genre Classification Model
This repository contains a machine learning model for music genre classification using MFCC (Mel Frequency Cepstral Coefficients) features. 
The model is trained on the FMA (Free Music Archive) dataset.

### Model Description
The model is implemented using the Keras library and consists of a multi-layer neural network. It takes MFCC features extracted from music tracks as input and predicts the genre of the music.

### Usage
1. Ensure that you have the required dependencies installed (Pandas, Scikit-learn, Keras).
2. Download the FMA dataset and place the necessary files (features.csv, tracks.csv, genres.csv) in the "data/fma_metadata" directory.
3. Run the code to train the model and evaluate its accuracy on the test dataset.
4. The trained model will be saved as "fma_model.h5" for future use.

### Files
- fma.py: Contains the code for loading the dataset, preprocessing the data, training the model, and evaluating its performance.
- fma_model.h5: The saved trained model.

### Data
- All metadata and features for all tracks are distributed in fma_metadata.zip (342 MiB).
- Download this Data-Package from this link directly: https://os.unil.cloud.switch.ch/fma/fma_metadata.zip or visit this site: https://github.com/mdeff/fma

- tracks.csv: per track metadata such as ID, title, artist, genres, tags and play counts, for all 106,574 tracks.
- genres.csv: all 163 genres with name and parent (used to infer the genre hierarchy and top-level genres).
- features.csv: common features extracted with librosa. 
