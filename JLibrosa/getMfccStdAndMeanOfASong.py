import librosa
import numpy as np

file_path = 'STUCK ON YOU (reggae)-first5sec.wav'
audio, sr = librosa.load(file_path)

mfccs = librosa.feature.mfcc(y=audio, sr=sr)

mfccs_mean = np.mean(mfccs, axis=1)
mfccs_std = np.std(mfccs, axis=1)

print("MFCCs Mean:", mfccs_mean)
print("MFCCs Standard Deviation:", mfccs_std)

