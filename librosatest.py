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
        self.start_time = time.time()
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
    
    def elapsed_time(self):
        return round(time.time() - self.start_time)

    def callback(self, in_data, frame_count, time_info, flag):
        numpy_array = np.frombuffer(in_data, dtype=np.float32)
        self.frames = np.append(self.frames, numpy_array)
        # librosa.feature.mfcc(y=numpy_array)
        # avg_power = np.average(librosa.feature.rms(y=numpy_array)) * 100000
        # if not self.elapsed_time() % 5:
        #     print(len(self.frames))
        # if avg_power > 5:
        #     ...
        return None, pyaudio.paContinue

    def mainloop(self):
        start = time.time()
        while (self.stream.is_active()):  # if using button you can set self.stream to 0 (self.stream = 0), otherwise you can use a stop condition
            end = time.time()
            # if end - start > 10:
            #     break
            # time.sleep(2.0)

    def save(self):
        wf.write('test.wav', self.RATE, self.frames)

audio = AudioHandler()
audio.start()     # open the the stream
audio.mainloop()  # main operations with librosa
audio.stop()
audio.save()


