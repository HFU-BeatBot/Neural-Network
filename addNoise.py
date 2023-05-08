import os

import librosa
import soundfile as sf


from audiomentations import Compose, AddGaussianNoise, PitchShift, HighPassFilter, AddBackgroundNoise, PolarityInversion
print("Start")
augment = Compose([
    AddGaussianNoise(min_amplitude=0.01, max_amplitude=0.09, p=1),
    #PitchShift(min_semitones=-8, max_semitones=8, p=1),
    #HighPassFilter(min_cutoff_freq=2000, max_cutoff_freq=4000, p=1)

])
print("...")
if __name__ == "__main__":
    genres = 'blues classical country disco hiphop jazz metal pop reggae rock'.split()
    for g in genres:
        filenamewhohidden = (filename for filename in os.listdir(f'genres/{g}') if not filename.startswith('.'))
        for filename in filenamewhohidden:
            signal, sr = librosa.load(f'./genres/{g}/{filename}')
            songname = f'./genres/{g}/{filename}'
            NameOfFile = os.path.basename(songname)

            augmented_signal = augment(signal, sr)

            sf.write(f'./audiomentations/{g}/' + os.path.splitext(NameOfFile)[0] + '.'  + os.path.splitext(NameOfFile)[1] + 'Gaussian' + '.wav', augmented_signal, sr)



