# Compute local onset autocorrelation
import librosa
import librosa.display
import numpy as np

# y, sr = librosa.load(librosa.ex('nutcracker'), duration=30)
y, sr = librosa.load('output/test.wav', duration=10)

hop_length = 512

oenv = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop_length)

tempogram = librosa.feature.tempogram(onset_envelope=oenv, sr=sr,

                                      hop_length=hop_length)

# Compute global onset autocorrelation

ac_global = librosa.autocorrelate(oenv, max_size=tempogram.shape[0])

ac_global = librosa.util.normalize(ac_global)

# Estimate the global tempo for display purposes

tempo = librosa.beat.tempo(onset_envelope=oenv, sr=sr,

                           hop_length=hop_length)[0]

import matplotlib.pyplot as plt

fig, ax = plt.subplots(nrows=4, figsize=(10, 10))

times = librosa.times_like(oenv, sr=sr, hop_length=hop_length)

ax[0].plot(times, oenv, label='Onset strength')

ax[0].label_outer()

ax[0].legend(frameon=True)

librosa.display.specshow(tempogram, sr=sr, hop_length=hop_length,

                         x_axis='time', y_axis='tempo', cmap='magma',

                         ax=ax[1])

ax[1].axhline(tempo, color='w', linestyle='--', alpha=1,

            label='Estimated tempo={:g}'.format(tempo))

ax[1].legend(loc='upper right')

ax[1].set(title='Tempogram')

x = np.linspace(0, tempogram.shape[0] * float(hop_length) / sr,

                num=tempogram.shape[0])

ax[2].plot(x, np.mean(tempogram, axis=1), label='Mean local autocorrelation')

ax[2].plot(x, ac_global, '--', alpha=0.75, label='Global autocorrelation')

ax[2].set(xlabel='Lag (seconds)')

ax[2].legend(frameon=True)

freqs = librosa.tempo_frequencies(tempogram.shape[0], hop_length=hop_length, sr=sr)

ax[3].semilogx(freqs[1:], np.mean(tempogram[1:], axis=1),

             label='Mean local autocorrelation', base=2)

ax[3].semilogx(freqs[1:], ac_global[1:], '--', alpha=0.75,

             label='Global autocorrelation', base=2)

ax[3].axvline(tempo, color='black', linestyle='--', alpha=.8,

            label='Estimated tempo={:g}'.format(tempo))

ax[3].legend(frameon=True)

ax[3].set(xlabel='BPM')

ax[3].grid(True)
plt.show()