import os

import psutil

def getStorageInfo():
    # Get all partitions
    partitions = psutil.disk_partitions(all=True)

    for partition in partitions:
        print(f"Device: {partition.device}")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File System Type: {partition.fstype}")

        try:
            partitionInfo = psutil.disk_usage(partition.mountpoint)

            print(f"  Total: {getSize(partitionInfo.total)}")
            print(f"  Used: {getSize(partitionInfo.used)}")
            print(f"  Free: {getSize(partitionInfo.free)}")
            print(f"  Percentage Used: {partitionInfo.percent}%")

        except Exception as e:
            print(f"  Error: {e}")

        print("\n")


def getSize(bytes, suffix="B"):
    # Convert bytes to a human-readable format
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}{suffix}"
        bytes /= 1024


# Example usage
getStorageInfo()


import pygame
import time

def play_audio(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Sleep while the music is playing
        while pygame.mixer.music.get_busy():
            time.sleep(1)

    except pygame.error as e:
        print(f"Error playing audio: {e}")

    pygame.mixer.quit()

if __name__ == "__main__":
    # Replace 'path_to_your_audio_file' with the actual path to your audio file
    audio_file_path = r"C:\Users\SandeepRegalla\Documents\Audacity\silence.wav"

    # Check if the file exists before attempting to play it
    if pygame.mixer.get_init() is None:
        print("Error initializing the mixer. Please check your audio configuration1.")
    elif not pygame.mixer.get_init():
        print("Error initializing the mixer. Please check your audio configuration.")
    elif os.path.exists(audio_file_path):
        play_audio(audio_file_path)
    else:
        print(f"File not found in the specified location else check for the file : {audio_file_path}")

from pydub import AudioSegment
import simpleaudio as sa

def play_audio(file_path):
    # Load the audio file using pydub
    sound = AudioSegment.from_file(file_path)

    # Convert the audio data to bytes
    audio_bytes = sound.raw_data

    # Play the audio using simpleaudio
    play_obj = sa.play_buffer(audio_bytes, 1, 2, sound.frame_rate)

    # Wait for the audio to finish playing
    play_obj.wait_done()

if __name__ == "__main__":
    # Replace 'path_to_your_audio_file' with the actual path to your audio file
    audio_file_path = r"C:\Users\SandeepRegalla\Documents\Audacity\Lost-Civilization-NEW024201.wav"

    # Check if the file exists before attempting to play it
    if os.path.exists(audio_file_path):
        play_audio(audio_file_path)
    else:
        print(f"File not found: {audio_file_path}")

