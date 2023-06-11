from classifySongOnModel import classifySongOnModel
from makeCSV import makeCSV
from makeModel import makeModel


makeCSV();
makeModel();
t= classifySongOnModel("Cascada_-_Everytime_We_Touch_Official_Video.mp3", "model.h", "scaler.bin");

print(t)