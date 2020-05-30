from time import sleep
from pydub import AudioSegment
import os
import sounddevice as sd
import random

path = os.path.join("C:/Users/vitor/Music/")
musics = os.listdir(path)
random.shuffle(musics)

for music in musics:
    audio = AudioSegment.from_mp3(path + music)
    seconds = audio.duration_seconds
    fs = audio.frame_rate*2
    audio = audio.get_array_of_samples()
    sd.play(audio, fs)