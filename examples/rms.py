import librosa
import librosa.display
import numpy as np
import array

y, sr = librosa.load(librosa.ex('trumpet'))

librosa.feature.rms(y=y)


S, phase = librosa.magphase(librosa.stft(y))

rms = librosa.feature.rms(S=S)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(nrows=2, sharex=True)

times = librosa.times_like(rms)

ax[0].semilogy(times, rms[0], label='RMS Energy')

ax[0].set(xticks=[])

ax[0].legend()

ax[0].label_outer()

librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max),
                         y_axis='log', x_axis='time', ax=ax[1])

ax[1].set(title='log Power spectrogram')


S = librosa.magphase(librosa.stft(y, window=np.ones, center=False))[0]

print(librosa.feature.rms(S=S))

plt.show()