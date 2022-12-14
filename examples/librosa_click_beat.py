# Sonify detected beat events
import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np

y, sr = librosa.load(librosa.ex('choice'), duration=10)

tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

y_beats = librosa.clicks(frames=beats, sr=sr)

# Or generate a signal of the same length as y
y_beats = librosa.clicks(frames=beats, sr=sr, length=len(y))
# Or use timing instead of frame indices
times = librosa.frames_to_time(beats, sr=sr)
y_beat_times = librosa.clicks(times=times, sr=sr)
# Or with a click frequency of 880Hz and a 500ms sample
y_beat_times880 = librosa.clicks(times=times, sr=sr,
                                 click_freq=880, click_duration=0.5)

fig, ax = plt.subplots(nrows=2, sharex=True)
S = librosa.feature.melspectrogram(y=y, sr=sr)
librosa.display.specshow(librosa.power_to_db(S, ref=np.max),
                         x_axis='time', y_axis='mel', ax=ax[0])
librosa.display.waveshow(y_beat_times, sr=sr, label='Beat clicks',
                         ax=ax[1])
ax[1].legend()
ax[0].label_outer()
ax[0].set_title(None)

plt.show()