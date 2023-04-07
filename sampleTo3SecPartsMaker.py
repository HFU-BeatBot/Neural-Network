from pydub import AudioSegment
import os

sampleSollLength = int(3)
genres = 'blues classical country disco hiphop jazz metal pop reggae rock'.split()
for g in genres:
    filenamewhohidden = (filename for filename in os.listdir(f'genres/{g}') if not filename.startswith('.'))
    for filename in filenamewhohidden:
        songname = f'./genres/{g}/{filename}'
        FullAudio = AudioSegment.from_wav(songname)
        NameOfFile = os.path.basename(songname)
        print(os.path.splitext(NameOfFile)[0])
        lengthOfAudio = FullAudio.duration_seconds
        print(lengthOfAudio)
        if (lengthOfAudio > sampleSollLength + 1):
            splitter = int(lengthOfAudio / sampleSollLength)
            i = int(0)
            j = int(0)
            while (i < splitter):
                newAudioPart = FullAudio[j: j + sampleSollLength * 1000]
                newAudioPart.export(
                    f'./genres/{g}/' + os.path.splitext(NameOfFile)[0] + '.' + str(i) + os.path.splitext(NameOfFile)[1],
                    format='wav')
                i = i + 1
                j = j + sampleSollLength * 1000

print('end')