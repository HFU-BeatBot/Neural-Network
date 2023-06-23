from pydub import AudioSegment
import os



sampleSollLength = 5;

songname = 'Cascada_-_Everytime_We_Touch_Official_Video.mp3'
FullAudio = AudioSegment.from_mp3(songname)
NameOfFile = os.path.basename(songname)
print(os.path.splitext(NameOfFile)[0])
lengthOfAudio = FullAudio.duration_seconds
print(lengthOfAudio)
splitter = int(lengthOfAudio / sampleSollLength)
i = int(0)
j = int(0)
newAudioPart = FullAudio[j: j + sampleSollLength * 1000]
newAudioPart.export(
    os.path.splitext(NameOfFile)[0] + 'bo.wav',
    format='wav')



print('end')