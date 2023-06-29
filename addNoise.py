import soundfile as sf

from audiomentations import Compose, AddGaussianNoise

def addNoise(signal, sr, wavName="Gaussian", fileType="wav"):

    print("addNoise")
    # Define an augmentation pipeline with AddGaussianNoise
    augment = Compose([
        AddGaussianNoise(min_amplitude=0.01, max_amplitude=0.01, p=1),
    ])
    # Apply the augmentation pipeline to the input signal with the given sample rate
    augmented_signal = augment(signal, sr)

    # Save the augmented signal as a WAV file with the specified name and sample rate
    sf.write(wavName, augmented_signal, sr)
