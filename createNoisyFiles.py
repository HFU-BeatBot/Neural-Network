
import csv
import os

import librosa
import numpy as np
from pydub import AudioSegment

from addNoise import addNoise


#going through all wav files
genres = 'electronic experimental folk hiphop instrumental international pop rock'.split()
for g in genres:
    filenamewhohidden = (filename for filename in os.listdir(f'./data_fma_small/{g}') if not filename.startswith('.'))
    for filename in filenamewhohidden:
        #preparing variables
        songname = f'./data_fma_small/{g}/{filename}'
        signal, sr = librosa.load(songname)
        NameOfFile = os.path.basename(songname)
        addNoise(signal, sr, f'./data_fma_small/{g}/' + "noisy" + NameOfFile)
print("end")