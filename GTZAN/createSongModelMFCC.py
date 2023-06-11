import librosa
import numpy as np
from pydub import AudioSegment
from createModelMFCC import scaler, model

song = '50 Cent - In Da Club.wav'

# load the audio file using pydub
FullAudio = AudioSegment.from_file(song, format='wav')
lengthOfAudio = FullAudio.duration_seconds

# load the audio file using librosa
y, sr = librosa.load(song, mono=True, duration=lengthOfAudio)

# extract MFCC features using librosa
mfcc = librosa.feature.mfcc(y=y, sr=sr)
songToArray= []
for e in mfcc:
    songToArray.append(np.mean(e))
    songToArray.append(np.std(e))

# convert the song features to numpy array
numpySongArray = np.array([songToArray])

# scale the song features using the trained scaler
numpySongArray = scaler.transform(numpySongArray)
print('NumpySongArray:')
print(numpySongArray)

# make a prediction using the trained model
prediction = model.predict(numpySongArray)
print(np.argmax(prediction[0]))