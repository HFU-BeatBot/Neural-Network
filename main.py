from classifySongOnModel import classifySongOnModel
from makeCSV import makeCSV
from makeModel import makeModel

makeCSV(partLength: int = 5,
            genresOfLibrary: str = 'blues classical country disco hiphop jazz metal pop reggae rock',
            path: str = 'genres',
            noisy: bool = False,
            isItMP3: bool = False,
            nameOfDataCSV: str = 'data.csv')


makeModel(csvFilePath: str = 'data.csv')


t = classifySongOnModel(song: Any,
                        model: Any,
                        scaler: Any)

# print(t)

# gtzan + noisy test accuracy: 0.9181286692619324
# gtzan         test accuracy: 0.826377272605896
# fma + noisy   test accuracy: 0.8433318138122559
# fma           test accuracy: 0.6334486603736877
# jLibrosa Gtzan     :
# jLibrosa FMA       : 0.6498094797134399
