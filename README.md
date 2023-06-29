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

## FMA Dataset (Free Music Archive)
- All metadata and features for all tracks are distributed in fma_metadata.zip (342 MiB).
- Download this Data-Package from this link directly [FMA Webpage](https://os.unil.cloud.switch.ch/fma/fma_metadata.zip)

The needed files from the fma_metadata folder:
- tracks.csv: per track metadata such as ID, title, artist, genres, tags and play counts, for all 106,574 tracks.
- genres.csv: all 163 genres with name and parent (used to infer the genre hierarchy and top-level genres).
- features.csv: common features extracted with librosa. 

### FMA small Dataset
The model here is trained with the FMA small dataset:  
- A collection of 8 balanced genres with 1000 audio files each, all having a length of 30 seconds in mp3 format (7.2 GiB)
- 8 genres: electronic, experimental, folk, hiphop, instrumental, international, pop and rock
- Download the FMA small dataset from this website: [FMA small](https://os.unil.cloud.switch.ch/fma/fma_small.zip) 

## Code
After downloading and unzipping the dataset, which is located in the folder called genres. Now you can transfer that into the required IDE (PyCharm). 

___
# Instruction
## Step by Step

For your understanding it needs several steps to create this neuronal network.

1. Get a library of sample song for each genre. 
2. Clone repository
3. Create mfcc values out of the sample-songs and fill them into a CSV-File.
4. To optimize the model, the values are getting splitted into 5 seconds parts. 
5. To optimize the model, the values are getting white noise (gaussian). 
6. Create a model (neuronal network) out of the CSV-File. Save the model and scaler.

To specify a song with the model you need to do:
7. Create the mfcc values of the song and load it into a numpy array. 
8. Use the scaler of the model on that numpy array. 
9. Use the model on that numpy array.

> You will return a number from 0 - 9, if your using the GTZAN-Dataset.

> You will return a number from 0 - 7, if your using the FMA small-Dataset.

### Genres
The genres can be specified by the model.

Here the GTZAN-Dataset genres:

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

Here the FMA small-Dataset genres:

0. electronic 
1. experimental 
2. folk 
3. hiphop 
4. instrumental 
5. international 
6. pop 
7. rock

___
## Usage
Follow those steps to use the Neural-Network:

1. Clone the repository. As for the IDE, we recommend you to use Jetbeans Pycharm.
```
git clone https://github.com/HFU-BeatBot/Neural-Network.git
```

2. Here we are using once the GTZAN-Dataset genres folder and the FMA small-Dataset genres folder. (see Dataset, where you find the links)
you can also use your desired Dataset-genres.


3. We don't need the complete audio file, we just need the mfcc values of those files. 
To do that we need to create the CSV-File with the MFCC Values of the sample songs by using this below. 
This will create by default 5 seconds part of your sample songs and additional create mfcc values with white noise (gaussian) on it and save as 'data.csv' in this directory. 
If you wish another length you can adjust the seconds of parts in the brackets.
```
from makeCSV import makeCSV

makeCSV()
```

4. With the CSV-file we can create now the model with the makeModel() method. 
Type the pathname of the CSV-File into the brackets, the standard path is 'data.csv' for our both Datasets.  
```
from makeCSV import makeCSV

makeModel("pathnameOfCSV")
```

5. The model and scaler is saved in same directory as the makeModel.py.


6. To specify a song we use the classifySongOnModel(song, model, scaler) function. 
In which you type the songpath of your wished song, the path of the model.h5 and the patch of the scaler.bin. 
This will return a number which represent one of the genres.
```
from classifySongOnModel import classifySongOnModel

classifySongOnModel("pathnameOfSong", "pathnameOfModel", "pathnameOfScaler")
```

## addnoise.py
This file defines a function addNoise() that takes a signal, sample rate, and optional parameters for the noise type and file format. 
It adds Gaussian noise to the input signal using the AddGaussianNoise function from the augment library. 
The augmented signal is then saved as a WAV file.

## makeCSV.py
This file imports necessary libraries and defines two functions: generateArrayOfMeanAndSTD() and makeCSV().

-	generateArrayOfMeanAndSTD() 
takes a song file, its filename, and genre as input. It loads the song using librosa, extracts MFCC features, calculates the mean and standard deviation of each feature, and returns a formatted string containing the filename, MFCC mean and standard deviation values, and genre.


-	makeCSV() 
This is the main function that generates a CSV file. It prepares the header row with column names for the filename, MFCC mean and standard deviation values, and label. It iterates through the Songs files in the specified genres folder, checks the length of each song, splits it into parts if it is longer than the specified duration, generates the MFCC features and labels for each part, and appends the data to the CSV file. It also adds Gaussian noise to the parts and appends the augmented data to the CSV file. The resulting CSV file contains the extracted features and labels for further analysis.

Here you can set our desired snippet value (partLength), genres (genresOfLibrary) and the genres folder (path)

- The first value "partLength" declares of the length of the parts which it creates out of the sample song.
- The second value "genresOfLibrary" are the folder names of the library.
- The third value is the path of the library of sample songs

Here we are using the GTZAN Dataset
```
from makeCSV import makeCSV

makeCSV(partLength = 5, genresOfLibrary ='blues classical country disco hiphop jazz metal pop reggae rock', path = 'genres');
```
Here we are using the FMA small Dataset
```
from makeCSV import makeCSV

makeCSV(partLength = 5, genresOfLibrary ='electronic experimental folk hiphop instrumental international pop rock', path = 'genres');
```
## makeModel.py
The model defines the architecture of a neural network model for genre classification.
It has been trained using the data stored in the CSV-File, in our case 'data.csv' file, which contains the noisy and split values generated using the makeCSV.py code.
 
The model does the following:
-	It performs training of the model, evaluation of its performance, prediction on test data, and saving the trained model. 
-	It generates visualizations to illustrate the training process and model performance. 
-	The neural network model consists of multiple dense layers with ReLU activation functions. 
-	Dropout layers are included to prevent overfitting. 
-	The output layer uses softmax activation for multi-class classification.

→ The resulting files are:

- the trained model is saved as 'model.h5',
- scaler as 'scaler.bin' and
- the visualizations is saved as 'loss_val_loss_with_earlystopping.png'.

Here you can use you own created CSV-File with your provided Dataset.

In our case we are using here our created CSV-File 'data.csv' (once for GTZAN-Dataset and once for FMA-Dataset)
```
from makeModel import makeModel

makeModel(csvFilePath = 'data.csv')
```

## classifySongOnModel.py
This file is used to classify a genre of song. It creates the MFCC std and mean values out of the given song and put them into a numpy array.
This numpy array of data is then taken by the model and it predicts the genre. It returns an Integer which represent as a genre of the library.
- The first value is the path of the songfile.
- The second value is the path of the model.h5
- The third value is the path of the scaler.bin

In our case you can see below, we have used this song "Cascada_-_Everytime_We_Touch_Official_Video.mp3", which return the number 
```
from classifySongOnModel import classifySongOnModel

classifySongOnModel("Cascada_-_Everytime_We_Touch_Official_Video.mp3", "model.h", "scaler.bin");
```

### FMASmallSortMP3.py
If you want to work with the FMA dataset, here is a helpful code that classifies your songs dataset and puts them in the appropriate genres folders
This file, much like FMALargeGTZANGenres.py, is used to assign the songs from FMA_small [FMA SMALL](https://os.unil.cloud.switch.ch/fma/fma_small.zip) (8GB) data to genre folders, this time the 8 genres specified in fma_small (electronic, experimental, folk, hiphop, instrumental, international, pop and rock).
To use this file place the tracks.csv [track.csv](https://os.unil.cloud.switch.ch/fma/fma_metadata.zip) (342 MB) at (/FMA/data/fma_metadata/tracks.csv) and the mp3 files at (/FMA/data/fma_small/)

→ The resulting directory is 'fma_small'

___
## main()
The makeCSV function is called to create a CSV file with genre information. 
The function takes various parameters, such as partLength, genresOfLibrary, path, noisy, isItMP3 and nameOfDataCSV to configure and save the CSV file accordingly.

The makeModel function is called to create a model. 
A CSV file (data.csv) is passed as the csvFilePath parameter to train the model on the data.

Finally, the classifySongOnModel function is called to classify a song based on the created model. 
The function is passed the path to the song (song), the path to the model (model) and the path to the scaler (scaler) to analyze the song and determine the genre.

Our full example using the GTZAN Dataset is shown in the main.py
```
makeCSV(partLength=5,
        genresOfLibrary='blues classical country disco hiphop jazz metal pop reggae rock',
        path='genres',
        noisy=False,
        isItMP3=False,
        nameOfDataCSV='data.csv')

makeModel(csvFilePath='data.csv')

t = classifySongOnModel("Cascada_-_Everytime_We_Touch_Official_Video.mp3",
                        "model.h5",
                        "scaler.bin")
```

## Accuracy
Here are the accuracy results:
> GTZAN model with noise: 91.81% 
>>GTZAN model without noise: 82.64%
    
>FMA small model with noise: 84.33%
>>FMA small model without noise: 63.34%
    
>jLibrosa GTZAN model: 81.00%
>>jLibrosa FMA model: 64.98%

