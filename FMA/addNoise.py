import os

import librosa
import soundfile as sf


from audiomentations import Compose, AddGaussianNoise, PitchShift, HighPassFilter, AddBackgroundNoise, PolarityInversion

def addNoise(signal, sr, wavName = "Gaussian", fileType ="wav"):

    print("Start")
    augment = Compose([
        AddGaussianNoise(min_amplitude=0.01, max_amplitude=0.01, p=1),
        #PitchShift(min_semitones=-8, max_semitones=8, p=1),
        #HighPassFilter(min_cutoff_freq=2000, max_cutoff_freq=4000, p=1)
    ])
    #return augment(signal, sr)
    augmented_signal = augment(signal, sr)
    sf.write(wavName, augmented_signal, sr)

