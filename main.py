
from AudioController import AudioController


config = {
    'SILENCE_THRESHOLD': 5  # how long it takes for audioclip to be captured when audio input stops
}


def run():
    controller = AudioController(config)
    controller.listen()


if __name__ == '__main__':
    run()
