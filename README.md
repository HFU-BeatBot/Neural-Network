# Neural-Network
The neural-network which decides what genre the given song belongs to.

## Setup

```
pip install -r requirements.txt
```
___
# Introduction
This project focuses on music genre classification using neural networks.

It involves two models: 
1.	JLibrosa GTZAN model: This one is trained on the GTZAN dataset.
2.	JLibrosa FMA model: This one is trained on the FMA dataset.

The workflow for both models is similar, and the goal is the same - to classify music genres.
___
# Datasets
## GTZAN Dataset
- A collection of 10 balanced genres with 100 audio files each, all having a length of 30 seconds in au format (1GiB)
- 10 genres: blues, classical, country, disco, hiphop, jazz, metal, pop, reggae and rock
- Download the GTZAN Dataset from this site: [GTZAN](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification)

## FMA Dataset
- All metadata and features for all tracks are distributed in fma_metadata.zip (342 MiB).
- Download this Data-Package from this link directly [FMA Webpage](https://os.unil.cloud.switch.ch/fma/fma_metadata.zip)

The needed files from the fma_metadata folder:
- tracks.csv: per track metadata such as ID, title, artist, genres, tags and play counts, for all 106,574 tracks.
- genres.csv: all 163 genres with name and parent (used to infer the genre hierarchy and top-level genres).
- features.csv: common features extracted with librosa. 

## Code
After downloading and unzipping the dataset, which is located in the folder called genres. Now you can transfer that into the required IDE (PyCharm). 

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
 
### createModel.py
The model defines the architecture of a neural network model for genre classification.
It has been trained using the data stored in the 'data.csv' file, which contains the noisy and split values generated using the makeCSV.py code.
 
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

### FMASmallSortMP3.py
This file, much like FMALargeGTZANGenres.py, is used to assign the songs from FMA_small (https://os.unil.cloud.switch.ch/fma/fma_small.zip 8GB) data to genre folders, this time the 8 genres specified in fma_small (electronic, experimental, folk, hiphop, instrumental, international, pop and rock).
To use this file place the tracks.csv (https://os.unil.cloud.switch.ch/fma/fma_metadata.zip 342 MB) at (/FMA/data/fma_metadata/tracks.csv) and the mp3 files at (/FMA/data/fma_small/)

→ The resulting directory is 'fma_small'

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

## Accuracy

The GTZAN model achieved a test accuracy of 93%. 
At the beginning we achieved only 65 accuracy, then with the noise of songs and better trained the model we achieved an 85 accuracy in FMA model.
