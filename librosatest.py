import numpy as np
import librosa.display
import pyaudio
import time
import librosa
import sounddevice
import matplotlib.pyplot as plt
import scipy.io.wavfile as wf

class AudioHandler(object):
    def __init__(self):
        self.FORMAT = pyaudio.paFloat32
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024 * 2
        self.p = None
        self.stream = None
        self.show = False
        self.frames = np.array([], dtype='f')

    def start(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  output=False,
                                  stream_callback=self.callback,
                                  frames_per_buffer=self.CHUNK)

    def stop(self):
        self.stream.close()
        self.p.terminate()
import numpy as np
import librosa.display
import pyaudio
import time
import librosa
import sounddevice
import matplotlib.pyplot as plt

class AudioHandler(object):
    def __init__(self):
        self.FORMAT = pyaudio.paFloat32
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024 * 2
        self.p = None
        self.stream = None
        self.show = False
        self.frames = np.array([], dtype='f')

    def start(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  output=False,
                                  stream_callback=self.callback,
                                  frames_per_buffer=self.CHUNK)

    def stop(self):
        self.stream.close()
        self.p.terminate()

    def save(self):
        wf.write('test.wav', self.RATE, self.frames)

    def callback(self, in_data, frame_count, time_info, flag):
        numpy_array = np.frombuffer(in_data, dtype=np.float32)
        librosa.feature.mfcc(y=numpy_array)
        self.frames = np.append(self.frames, numpy_array)
        # print(len(self.frames))
        return None, pyaudio.paContinue

    def callback(self, in_data, frame_count, time_info, flag):
        numpy_array = np.frombuffer(in_data, dtype=np.float32)
        librosa.feature.mfcc(y=numpy_array)
        self.frames = np.append(self.frames, numpy_array)
        # print(len(self.frames))
        return None, pyaudio.paContinue

    def mainloop(self):
        start = time.time()
        while (self.stream.is_active()):  # if using button you can set self.stream to 0 (self.stream = 0), otherwise you can use a stop condition
            end = time.time()
            if end - start > 6:
                break
            time.sleep(2.0)


audio = AudioHandler()
audio.start()     # open the the stream
audio.mainloop()  # main operations with librosa
audio.stop()
audio.save()


