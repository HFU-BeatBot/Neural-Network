from classifySongOnModel import classifySongOnModel
from makeCSV import makeCSV
from makeModel import makeModel

# Step 1: Generate the CSV file with audio features
makeCSV(partLength=5,
        genresOfLibrary='blues classical country disco hiphop jazz metal pop reggae rock',
        path='genres',
        noisy=False,
        isItMP3=False,
        nameOfDataCSV='data.csv')

# Step 2: Train the model using the generated CSV file
makeModel(csvFilePath='data.csv')

# Step 3: Classify a song using the trained model
t = classifySongOnModel("Cascada_-_Everytime_We_Touch_Official_Video.mp3",
                        "model.h5",
                        "scaler.bin")
