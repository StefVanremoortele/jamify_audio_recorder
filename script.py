import pyaudio # Soundcard audio I/O access library
import wave # Python 3 module for reading / writing simple .wav files
import sounddevice
import constants
from datetime import datetime
import time

# Setup channel info
FORMAT = pyaudio.paInt16 # data type formate
CHANNELS = 2 # Adjust to your number of channels
RATE = 44100 # Sample Rate
CHUNK = 1024 # Block Size
RECORD_SECONDS = 3600 # Record time
WAVE_OUTPUT_FILENAME = f"{constants.OUTPUT_DIR}/{datetime.now().strftime('%Y%m%d-%H%M%S')}.wav"

# Startup pyaudio instance
audio = pyaudio.PyAudio()

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print("recording...")
frames = []

# Record for RECORD_SECONDS
start = time.time()
for i in range(0,   int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
    if (time.time() - start) == 3:  # record for 3 seconds
        break
    # if (i / int(RATE / CHUNK * RECORD_SECONDS) * 100) > 0.1: # record for 5 seconds
    #     break


# Stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
print("finished recording")

# Write your new .wav file with built in Python 3 Wave module
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()