# Neural-Network
The neural-network which decides what genre the given song belongs to.

## Setup

```
pip install -r requirements.txt
```
### Nahed:
___
# Introduction
This project focuses on music genre classification using neural networks.

It involves two models: 
1.	GTZAN model: This one is trained on the GTZAN dataset.
2.	FMA model: This one is trained on the FMA dataset.

The workflow for both models is similar, and the goal is the same - to classify music genres.
___
# GTZAN
## Dataset
- A collection of 10 balanced genres with 100 audio files each, all having a length of 30 seconds in au format (1GiB)
- 10 genres: blues, classical, country, disco, hiphop, jazz, metal, pop, reggae and rock
- Download the GTZAN Dataset from this site: [GTZAN](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification)

## Code
After downloading and unzipping the dataset, which is located in the folder called genres. Now you can transfer that into the required IDE (PyCharm). 

### 1. convertSongsToWav.py
This code creates a 'genres_wav' directory to store WAV files. For each genre in the given list, the code iterates over the corresponding genre folder. 
It converts each AU file to WAV format, saves it in the genre-specific directory.

→ The resulting directory is saved as 'genres_wav'

### 2.	createDataMFCC.py
This code generates the GTZAN dataset in the form of a CSV file ' gtzan_data.csv ' with MFCC (Mel-frequency Cepstral Coefficients) features extracted from audio files, which saved in the 'genres_wav' directory.

→ The resulting file is saved as 'gtzan_data.csv' in the directory 'data'

In steps 3 and 4, we apply two important procedures to the GTZAN data:
- adding individual noise and 
- creating 5-second snippets
These codes contribute to the overall structure and understanding. 

However, in steps 5 and 6, we combine steps 3 and 4 into a single code. This code allows us to process the data more efficiently and save the results in a single CSV file. This approach enhances our workflow and simplifies further work with the data. 

### 3.	createSplittedSongs.py
This code loads audio files from the specified genres folder and creates 5-second snippets. It extracts MFCC features from each snippet using the librosa library and scales the features using a StandardScaler. The extracted features, along with the corresponding genre information, are then saved in a CSV file.

→ The resulting file is saved as 'gtzan_SplittedSong.csv' in the directory 'GTZAN_Splitted_Songs'

### 4.	addSongsnoise.py
This code generates noisy versions of songs. 
It adds random noise to the original audio and normalizes the resulting audio. 
The code then saves the noisy songs in a separate folder organized by genre and extracts MFCC (Mel-frequency cepstral coefficients) features from the noisy audio. 
The extracted MFCC features are saved in a CSV file along with the corresponding song information.

→ The resulting file is saved as 'gtzan_noisy_songs.csv' in the directory 'data' 

→ The resulting noisy versions songs is saved in the directory 'GTZAN_Noisy_Songs'

### 5. addNoise.py
This file defines a function addNoise() that takes a signal, sample rate, and optional parameters for the noise type and file format. It adds Gaussian noise to the input signal using the AddGaussianNoise function from the augment library. The augmented signal is then saved as a WAV file.

### 6. makeCSV.py
This file imports necessary libraries and defines two functions: generateArrayOfMeanAndSTD() and makeCSV().

-	generateArrayOfMeanAndSTD() 
takes a song file, its filename, and genre as input. It loads the song using librosa, extracts MFCC features, calculates the mean and standard deviation of each feature, and returns a formatted string containing the filename, MFCC mean and standard deviation values, and genre.
-	makeCSV() 
This is the main function that generates a CSV file. It prepares the header row with column names for the filename, MFCC mean and standard deviation values, and label. It iterates through the WAV files in the specified genres folder, checks the length of each song, splits it into parts if it is longer than the specified duration, generates the MFCC features and labels for each part, and appends the data to the CSV file. It also adds Gaussian noise to the parts and appends the augmented data to the CSV file. The resulting CSV file contains the extracted features and labels for further analysis.

→ The resulting file is saved as 'data.csv' in the directory 'data'
To use the code, simply call makeCSV() function, and the CSV file will be generated with the extracted features and labels.
 
### 7. createModelMFCC.py
The model defines the architecture of a neural network model for genre classification.
It has been trained using the data stored in the 'data.csv' file, which contains the noisy and split values generated using the makeCSV.py code. 
The model achieved a training accuracy of 99% and a test accuracy of 93%. 
 
The model does the following:
-	It performs training of the model, evaluation of its performance, prediction on test data, and saving the trained model. 
-	It generates visualizations to illustrate the training process and model performance. 
-	The neural network model consists of multiple dense layers with ReLU activation functions. 
-	Dropout layers are included to prevent overfitting. 
-	The output layer uses softmax activation for multi-class classification. 

→ The resulting files are:

- the trained model is saved as 'gtzan_model.h5',
- scaler as 'gtzan_scaler.bin' and
- the visualizations is saved as 'gtzan_loss_val_loss_with_earlystopping.png'.

### 8. createSongModelMFCC.py
In this code, we are loading an audio file named '50 Cent - In Da Club.wav'. 
The Goal here is to print the genre label from the Song. 

→ The resulting output will be a number from 0 to 9, representing the detected genre from the list 'blues, classical, country, disco, hiphop, jazz, metal, pop, reggae, rock'  

___
# FMA (Free Music Archive)
## FMA Dataset
- All metadata and features for all tracks are distributed in fma_metadata.zip (342 MiB).
- Download this Data-Package from this link directly [FMA Webpage](https://os.unil.cloud.switch.ch/fma/fma_metadata.zip)

The needed files from the fma_metadata folder:
- tracks.csv: per track metadata such as ID, title, artist, genres, tags and play counts, for all 106,574 tracks.
- genres.csv: all 163 genres with name and parent (used to infer the genre hierarchy and top-level genres).
- features.csv: common features extracted with librosa. 

## FMA small Dataset
The model here is trained with the FMA small dataset:  
- A collection of 8 balanced genres with 1000 audio files each, all having a length of 30 seconds in mp3 format (7.2 GiB)
- 8 genres: electronic, experimental, folk, hiphop, instrumental, international, pop and rock
- Download the FMA small dataset from this website: [FMA small](https://os.unil.cloud.switch.ch/fma/fma_small.zip) 

## FMA large Dataset (Dominik)
- fma_large: 106,574 tracks of 30s, 161 unbalanced genres (93 GiB)
- Download the dataset from this website: [FMA Large](https://os.unil.cloud.switch.ch/fma/fma_large.zip)
- The 16 main genres are: electronic, experimental, folk, hiphop, instrumental, international, pop, rock, jazz, classical, country, spoken, blues, soul/rnb, old-time/histroic and easy listening

# Code
### 1. FMASmallSortMP3.py (Dominik)
This file, much like FMALargeGTZANGenres.py, is used to assign the songs from FMA_small (https://os.unil.cloud.switch.ch/fma/fma_small.zip 8GB) data to genre folders, this time the 8 genres specified in fma_small (electronic, experimental, folk, hiphop, instrumental, international, pop and rock).
To use this file place the tracks.csv (https://os.unil.cloud.switch.ch/fma/fma_metadata.zip 342 MB) at (/FMA/data/fma_metadata/tracks.csv) and the mp3 files at (/FMA/data/fma_small/)

→ The resulting directory is 'fma_small'

### 2. convertSongsToWav.py
Here we created a 'fma_small_wav' directory to store WAV files from the 'fma_small' directory, and then for each genre in the given list, the code iterates over the corresponding genre folder. 
It converts each MP3 file to WAV format, saves it in the genre-specific directory.

→ The resulting directory is 'fma_small_wav'


### 3. createDataMFCC.py:
This code works with the FMA small dataset, exactly with the converted one "fma_small_wav" directory.
In the code, we access these genre folders and process individual songs. 

→ The resulting file saved as 'fma_small_data.csv' in the directory 'data'.

Please note that the FMA small dataset may contain some defective songs. 
To handle this, the code includes a try-catch block to ignore and skip any problematic songs during processing.

In steps 4 and 5, we apply two important procedures to the FMA data:
- adding individual noise and 
- creating 5-second snippets
These codes contribute to the overall structure and understanding. 

However, in steps 6 and 7, we combine steps 4 and 5 into a single code. This code allows us to process the data more efficiently and save the results in a single CSV file. This approach enhances our workflow and simplifies further work with the data.

### 4. addSongsnoise.py
This code generates noisy versions of songs. 
It adds random noise to the original audio and normalizes the resulting audio. 
The code then saves the noisy songs in a separate folder organized by genre and extracts MFCC (Mel-frequency cepstral coefficients) features from the noisy audio. 
The extracted MFCC features are saved in a CSV file along with the corresponding song information.

→ The resulting CSV file is saved as 'fma_noisy_songs.csv' in the directory 'data' 

→ The resulting noisy versions songs is saved in the 'FMA_Noisy_Songs'

### 5. createSplittedSongs.py
This code generates noisy versions of songs. 
It adds random noise to the original audio and normalizes the resulting audio. 
The code then saves the noisy songs in a separate folder organized by genre and extracts MFCC (Mel-frequency cepstral coefficients) features from the noisy audio. 
The extracted MFCC features are saved in a CSV file along with the corresponding song information.

→ The resulting file is saved as 'fma_SplittedSong.csv' in the directory 'FMA_Splitted_Songs' 

### 6. addNoise.py
This file defines a function addNoise() that takes a signal, sample rate, and optional parameters for the noise type and file format. It adds Gaussian noise to the input signal using the AddGaussianNoise function from the augment library. The augmented signal is then saved as a WAV file.

### 7. makeCSV.py
This file imports necessary libraries and defines two functions: generateArrayOfMeanAndSTD() and makeCSV().

-	generateArrayOfMeanAndSTD() 
takes a song file, its filename, and genre as input. It loads the song using librosa, extracts MFCC features, calculates the mean and standard deviation of each feature, and returns a formatted string containing the filename, MFCC mean and standard deviation values, and genre.
-	makeCSV() 
This is the main function that generates a CSV file. It prepares the header row with column names for the filename, MFCC mean and standard deviation values, and label. It iterates through the WAV files in the specified genres folder, checks the length of each song, splits it into parts if it is longer than the specified duration, generates the MFCC features and labels for each part, and appends the data to the CSV file. It also adds Gaussian noise to the parts and appends the augmented data to the CSV file. The resulting CSV file contains the extracted features and labels for further analysis.

→ The resulting file is saved as 'data.csv' in the directory 'data'
To use the code, simply call makeCSV() function, and the CSV file will be generated with the extracted features and labels.

### 8. createModelMFCC.py
The model defines the architecture of a neural network model for genre classification.
It has been trained using the data stored in the 'data.csv' file, which contains the noisy and split values generated using the makeCSV.py code. 
The model achieved a training accuracy of 82% and a test accuracy of 72%. 
 
The model does the following:
-	It performs training of the model, evaluation of its performance, prediction on test data, and saving the trained model. 
-	It generates visualizations to illustrate the training process and model performance. 
-	The neural network model consists of multiple dense layers with ReLU activation functions. 
-	Dropout layers are included to prevent overfitting. 
-	The output layer uses softmax activation for multi-class classification. 

→ The resulting files are:
- the trained model is saved as 'gtzan_model.h5',
- the scaler as 'gtzan_scaler.bin' and
- the visualizations is saved as 'gtzan_loss_val_loss_with_earlystopping.png'.

### 9. createSongModelMFCC.py
In this code, we are loading an audio file named '50 Cent - In Da Club.wav'. 
The Goal here is to print the genre label from the Song. 

→ The resulting output will be a number from 0 to 7, representing the detected genre from the list 'electronic, experimental, folk, hiphop, instrumental, international, pop, rock'

### Usage
1. Ensure that you have the required dependencies installed.
2. Download the dataset and ensure that the required files are placed in the desired directory for both GTZAN and FMA.
3. Follow the provided steps to familiarize yourself with the workflow.
4. Run the code to train the model and evaluate its accuracy on the test dataset.
5. The trained model will be saved as ".h5" Format for future use.

### Dominik:
___

### FMALargeSortGTZANGenres.py
This file is used to automatically assign the songs from the FMA_large (https://os.unil.cloud.switch.ch/fma/fma_large.zip 93GB) data to the GTZAN genre folders.
It automatically creates the GTZAN  (blues, classical, country, disco, hiphop, jazz, metal, pop, reggae and rock) 
folders at given location and moves the songs that fit the GTZAN genres into the folders.

To use this file place the tracks.csv (https://os.unil.cloud.switch.ch/fma/fma_metadata.zip 342 MB) at (/FMA/data/fma_metadata/tracks.csv) 
and the mp3 files at (/FMA/data/fma_small/).

### getMfccStdAndMeanOfASong.py
This file is used to get the std and mean MFCC values of a single Song.
To use it you have to replace the file path (file_path = 'STUCK ON YOU (reggae)-first5sec.wav') with the file path to the Song you
want the MFCC values of.


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