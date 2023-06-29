from classifySongOnModel import classifySongOnModel
from makeCSV import makeCSV
from makeModel import makeModel


makeCSV(5, 'blues classical country disco hiphop jazz metal pop reggae rock', 'genres', False, False, 'data.csv')

makeModel('data.csv')

t = classifySongOnModel('The Beatles - Hey Jude.mp3', 'model.h5', 'scaler.bin')

print(t)

# test_acc:  0.9036144614219666
