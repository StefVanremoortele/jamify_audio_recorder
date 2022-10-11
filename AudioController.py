
import pyaudio
import helpers
import constants
from datetime import datetime
from AudioClipStore import Store


class AudioController():

    def __init__(self, config):
        self.SILENCE_THRESHOLD = config.get('SILENCE_THRESHOLD')
        self.audioclip_handler = Store()
        self._pa = pyaudio.PyAudio()

        self.FORMAT = pyaudio.paInt16 #  data type formate
        self.CHANNELS = 2  # Adjust to your number of channels
        self.RATE = 44100  # Sample Rate
        self.CHUNK = 1024  # Block Size
        self.RECORD_SECONDS = 3600  # Record time
        self.WAVE_OUTPUT_FILENAME = helpers.generate_filename()
        self.frames = []

    def listen(self):
        # start pyaudio, listen for input
        stream = self._pa.open(format=self.FORMAT, channels=self.CHANNELS,
                               rate=self.RATE, input=True,
                               frames_per_buffer=self.CHUNK)
        for i in range(0,   int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            self.frames.append(data)
        
        # if constant audio input for 5 seconds, start recording
        # watch audio input stream
        # when no audio input for 5 seconds, stop recording
        
        # write audioclip to disk
        # audioclip = None
        # self.audioclip_handler.handle(audioclip)

