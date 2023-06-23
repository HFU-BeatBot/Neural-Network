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
- Download the GTZAN Dataset from this site: [GTZAN](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification)

### FMA (Free Music Archive) Dataset
- A collection of 10 genres with more than 100 audio files each, all having a length of 30 seconds
- 10 genres: blues, classical, country, disco, hiphop, jazz, metal, pop, reggae and rock
- All metadata and features for all tracks are distributed in fma_metadata.zip (342 MiB).
- Download this Data-Package from this link directly: [FMA Webpage](https://os.unil.cloud.switch.ch/fma/fma_metadata.zip) or visit this site: [FMA Github](https://github.com/mdeff/fma)

- tracks.csv: per track metadata such as ID, title, artist, genres, tags and play counts, for all 106,574 tracks.
- genres.csv: all 163 genres with name and parent (used to infer the genre hierarchy and top-level genres).
- features.csv: common features extracted with librosa. 

##### FMA small:
- fma_small: 8,000 tracks of 30s, 8 balanced genres (GTZAN-like) (7.2 GiB)
- Download the dataset from this website: [FMA Small](https://os.unil.cloud.switch.ch/fma/fma_small.zip)
- The 8 involves genres are: electronic, experimental, folk, hiphop, instrumental, international, pop and rock.

## Code
The Python codes are available in both the FMA and GTZAN folders with slight modifications.

### convertSongsToWav.py
#### FMA small
We have the FMA small dataset organized into genre folders called "fma_small".
Then we created a "fma_small_wav" directory to store WAV files, and then for each genre in the given list, the code iterates over the corresponding genre folder. 
It converts each MP3 file to WAV format, saves it in the genre-specific directory.

#### GTZAN
In this code we created a "genres_wav" directory to store WAV files, and then for each genre in the given list, the code iterates over the corresponding genre folder. 
It converts each AU file to WAV format, saves it in the genre-specific directory.

### createDataMFCC.py:
#### FMA small
This code works with the FMA small dataset, exactly with the converted one "fma_small_wav" directory.
In the code, we access these genre folders and process individual songs. 
The processed data is then saved in a CSV file named "fma_small_data.csv" in the directory "data".

Please note that the FMA small dataset may contain some defective songs. 
To handle this, the code includes a try-catch block to ignore and skip any problematic songs during processing.

#### GTZAN
This code generates the GTZAN dataset in the form of a CSV file (gtzan_data.csv) with MFCC (Mel-frequency Cepstral Coefficients) features extracted from audio files, which saved in the "genres_wav" directory.
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

### filterFMAData.py
The goal of this code is to filter the Data from the FMA dataset. 

- In the variable filtered_tracks_data, the tracks were filtered to keep only those belonging to the selected genres. 
The selected genres are: 'Blues', 'Classical', 'Country', 'Disco', 'Hip-Hop', 'Jazz', 'Metal', 'Pop', 'Reggae - Dub', and 'Rock'. 
This filtering was based on the 'label' column in the "tracks_data" DataFrame.
- In the variable genres_data, the genres were filtered to keep only those genres that belong to the selected genres. 
This filtering was based on the 'title' column in the "genres_data" DataFrame.
- In the variable merged_genres, the data from the merged_data and genres_data DataFrames was further filtered to keep only the data for the selected genres. 
The 'label' column was used for this filtering.

### createSplittedSongs.py
- Loads audio files from the specified genres folder and creates snippets of 5-second duration.
- Extracts MFCC features from each snippet and scales the features using a StandardScaler. 
- Makes predictions using the trained model and saves the snippet paths and predicted genres in a CSV file. 

For the FMA data
- The resulting CSV file is saved as fma_SplittedSong.csv in the "FMA_Splitted_Songs" folder.

For the GTZAN data
- The resulting CSV file is saved as gtzan_SplittedSong.csv in the "GTZAN_Splitted_Songs" folder.

### addSongsnoise.py
This code generates noisy versions of songs. 
It adds random noise to the original audio and normalizes the resulting audio. 
The code then saves the noisy songs in a separate folder organized by genre and extracts MFCC (Mel-frequency cepstral coefficients) features from the noisy audio. 
The extracted MFCC features are saved in a CSV file along with the corresponding song information.

For the FMA data
- The resulting CSV file is saved as fma_noisy_songs.csv in the "data" folder.
- The resulting noisy versions songs is saved in the "FMA_Noisy_Songs" folder.

For the GTZAN data
- The resulting CSV file is saved as gtzan_noisy_songs.csv in the "data" folder.
- The resulting noisy versions songs is saved in the "GTZAN_Noisy_Songs" folder.

### FMALargeSortGTZANGenres.py
This file is used to automatically assign the songs from the FMA_large (https://os.unil.cloud.switch.ch/fma/fma_large.zip 93GB) data to the GTZAN genre folders.
It automatically creates the GTZAN  (blues, classical, country, disco, hiphop, jazz, metal, pop, reggae and rock) 
folders at given location and moves the songs that fit the GTZAN genres into the folders.

To use this file place the tracks.csv (https://os.unil.cloud.switch.ch/fma/fma_metadata.zip 342 MB) at (/FMA/data/fma_metadata/tracks.csv) 
and the mp3 files at (/FMA/data/fma_small/).

### FMASmallSortMP3.py
This file, much like FMALargeGTZANGenres.py, is used to assign the songs from FMA_small (https://os.unil.cloud.switch.ch/fma/fma_small.zip 8GB) data
to genre folders, this time the 8 genres specified in fma_small (electronic, experimental, folk, hiphop, instrumental, international, pop and rock).

To use this file place the tracks.csv (https://os.unil.cloud.switch.ch/fma/fma_metadata.zip 342 MB) at (/FMA/data/fma_metadata/tracks.csv) 
and the mp3 files at (/FMA/data/fma_small/).

### getMfccStdAndMeanOfASong.py
This file is used to get the std and mean MFCC values of a single Song.
To use it you have to replace the file path (file_path = 'STUCK ON YOU (reggae)-first5sec.wav') with the file path to the Song you
want the MFCC values of.

### Usage
1. Ensure that you have the required dependencies installed.
2. Download the dataset and place the necessary files in the "data" directory,for both GTZAN and FMA.
3. Run the code to train the model and evaluate its accuracy on the test dataset.
4. The trained model will be saved as ".h5" Format for future use.

### TOM:
___
# Instruction
## Step by Step

For your understanding it needs several steps to create this neuronal network.
Below you will find an instruction which shows you to use fiber.

1.  Get a library of sample song for each genre.
2.  Clone repository
2.  Create mfcc values out of the sample-songs and fill them into a CSV-File.
3. To optimize the model, the values are getting splitted into 5 seconds parts. 
4. To optimize the model, the values are getting white noise (gaussian). 
5. Create a model (neuronal network) out of the CSV-File. Save the model and scaler.
-   To specify a song with the model you need to do:
6. Create the mfcc values of the song and load it into a numpy array.
7. Use the scaler of the model on that numpy array.
8. Use the model on that numpy array.
-   You will now return a nummer from 0 - 9. Each number stands for genre.

### Genres

Those genres can be specified by the model:
0. blues
1. classical
2. country
3. disco
4. hiphop
5. jazz
6. metal
7. pop
8. reggae
9. rock
___
## 1. Sample-Song Library

This was our first sample-song library:

[GTZAN](https://www.kaggle.com/datasets/carlthome/gtzan-genre-collection)

There are 100 songs of 30 seconds length, for each genre. That is a great base 
to start with but, we only could achieve an accuracy of 87%. This was for us 
not enough, so we looked for more sample-songs.

This is our second-song library:

[FMA](https://github.com/mdeff/fma)

There are more than 100 000 sample songs. Which are not by default in a folder
of their genre. So it needs to specified in which genre the songs are. The only
link between them are csv-files which combined has to be combined.

___
## Usage
Follow those steps to use fiber:
1. Clone the repository. As for the IDE, we recommend you to use Jetbeans Pycharm.
```
git clone https://github.com/HFU-BeatBot/Neural-Network.git
```
2. Create a folder with the name 'genres' and in this folder creates 10 folder 
with the genrenames. Take care that you use the exact same names as it stands above (without the numbering). 
Fill in them folders the sample songs of GTZAN or from your own source.
But if you use the FMA files you need to do...
3. We don't need the complete audio file, we just need the mfcc values of those files. To do that we need to create the CSV-File with the MFCC Values of the sample songs by using this below. This will create by default 5 seconds part of your sample songs and additional create mfcc values with white noise (gaussian) on it and save as 'data.csv' in this directory. If you wish another length you can adjust the seconds of parts in the brackets. 
```
from makeCSV import makeCSV

makeCSV()
```
4. With the CSV-file we can create now the model with the makeModel() method. Type the pathname of the CSV-File into the brackets, the standard path is "/data.csv".  
```
from makeCSV import makeCSV

makeModel("pathnameOfCSV")
```
5. The model and scaler is saved in same directory as the makeModel.py.
6. To specify a song we use the classifySongOnModel(song, model, scaler) function. In which you type the songpath of your wished song, the path of the model.h and the patch of the scaler.bin. This will then return a number which represent one of the genres.
```
from classifySongOnModel import classifySongOnModel

classifySongOnModel("pathnameOfSong", "pathnameOfModel", "pathnameOfScaler")
```

## makeCSV.py
This makes a data.csv file out of a library of songs which are sorted in genres folder. It splits the songs into
parts. From that part it takes the std and mean MFCC values and put into 
a csv-file (data.csv). However, it further creates a noisy version of that part 
calculate the std and mean MFCC values and put them into the csv-file as well.
The first value "partLength" declares of the length of the parts which it creates out of the sample song.
The second value "genresOfLibrary" are the folder names of the library.
The third value is the path of the library of sample songs
```
from makeCSV import makeCSV

makeCSV(partLength = 5, genresOfLibrary ='blues classical country disco hiphop jazz metal pop reggae rock', path = 'genres');
```
## makeModel.py
This is creating the model out of the csv-file. Which will be saved as "model.h5" and the scaler will
be saved as "scaler.bin" in the same directory as of the makeModel.py file. The parameter of that
model achieves the best accuracy of the GTZAN Library.
The only value that it takes is the path of the csv-file.
```
from makeModel import makeModel

makeModel(csvFilePath = 'data.csv')
```
## classifySongOnModel.py
This file is used to classify a genre of song. It creates the MFCC std and mean values out of 
the given song and put them into a numpy array. This numpy array of data is then taken by the model and
it predicts the genre. It returns an Integer which represent as a genre of the library.
The first value is the path of the songfile.
The second value is the path of the model.h5
The third value is the path of the scaler.bin
```
from classifySongOnModel import classifySongOnModel

classifySongOnModel("Cascada_-_Everytime_We_Touch_Official_Video.mp3", "model.h", "scaler.bin");
```

## Create CSV 
To change the length of the audio files, just fill the duration in seconds into the brackets.
```
from makeCSV import makeCSV

makeCSV(3);
```
___
## main()
A full example is shown in the main.py
```
from classifySongOnModel import classifySongOnModel
from makeCSV import makeCSV
from makeModel import makeModel


makeCSV();
makeModel();
t= classifySongOnModel("Cascada_-_Everytime_We_Touch_Official_Video.mp3", "model.h", "scaler.bin");

print(t)
```

# Archive
In the archive are files which were needed but ain't finding any use now because they become obsolete through other files.
Those files are still usefull for special tasks.

### createModelFunction.py
This was the first attempt to make use gridSearcher on the neuronal network model.
By defining the parameters of the gridSearcher function it tries every possible model with
those parameter. In the end it shows in the console the parameter with the highest
accuracy.

### createNoiseDataMFCC.py
This function had the purpose of creating a data.csv file out songs in genres folder.
It creates just the std and mean MFCC values and saves them in the data.csv. 
Additionally it creates a noisy song out of it and saves that MFCC values into
the data.csv as well.

### createSongModel.py
In order that the model can predict a genre, it needs a song. This file creates
all the MFCC values out of a given song and saves it into an appropriate numpy array.
The model then predicts the genre by that array.

### createSongModelMFCC.py
This creates only the MFCC std and MFCC mean values of a given song. Those values
are saved to a numpy array, which then takes the model to predict the genre.

### createSplittedSongModel.py
This file splits the song in 5 seconds parts and saves them one at a time temporarly in the
folder "cache". The next 5 seconds part overwrite the predecessor. It then creates all MFCC values and write them into an array of numpyArrays. 
In the end, it predicts the genre of all 5 second parts and write the result into
the console

### equalizeGenreSongs.py
In order to make a good model the library of songs has to be balanced. This file
takes a filled csv-file and creates a new csv-file with a certain maximum number of entries of all genres.

### fiber.py
The original model on which are the most files are based on. This file creates the data.csv and the model together.
It ain't has great accuracy that is the reason why we modified it.
The original code: [Classification of Music into different Genres using Keras](https://medium.com/@sdoshi579/classification-of-music-into-different-genres-using-keras-82ab5339efe0)

### sampleTo3SecPartsMaker.py
This file creates 3 seconds parts out of the library songs and saves them in to
the same directory as the original.

### splitSongto5Sec.py

<<< Dominik >>>

# TO BE CONTINUED