
import librosa.display
import librosa
import matplotlib.pyplot as plt
import numpy as np

# Load sound file
y, sr = librosa.load("../output/test.wav")

res = librosa.onset.onset_detect(y=y, sr=sr, units='time')
print(res)