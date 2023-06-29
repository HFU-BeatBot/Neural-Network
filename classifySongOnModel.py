import librosa
import numpy as np
import tensorflow as tf
from joblib import load

print("classifySongOnModel ready")

def classifySongOnModel(song, model, scaler):
    print("Start classifySongOnModel()")

    # Load the song and extract the MFCC values
    y, sr = librosa.load(song, mono=True)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)

    # Fill the MFCC values into an array
    songToArray = []
    for e in mfcc:
        songToArray.append(np.mean(e))
        songToArray.append(np.std(e))

    # Transform the array into a numpy array
    numpySongArray = np.array([songToArray], dtype=float)

    # Scale the numpy array using the model's scaler
    standardScaler = load(scaler)
    numpySongArray = standardScaler.transform(numpySongArray)

    # Print the values of the numpy array (for control purposes)
    print('NumpySongArray:')
    print(numpySongArray)

    # Load the model and predict the genre of the song
    model = tf.keras.models.load_model(model)
    prediction = model.predict(numpySongArray)
    print(np.argmax(prediction[0]))
    print("End classifySongOnModel()")

    return np.argmax(prediction[0])
