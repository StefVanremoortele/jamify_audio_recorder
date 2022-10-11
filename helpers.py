import constants
import datetime


def generate_filename():
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    return f"{constants.OUTPUT_DIR}/{timestamp}.wav"
