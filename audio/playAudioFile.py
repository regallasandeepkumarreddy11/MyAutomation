import os
import pygame
import sounddevice as sd
import time

class AudioManager:
    def __init__(self, wav_file_path):
        self.wav_file_path = wav_file_path

    def get_audio_devices(self):
        devices = sd.query_devices()

        input_devices = [device for device in devices if 'input' in device['name']]
        output_devices = [device for device in devices if 'output' in device['name']]

        print("Available audio input devices:")
        for i, device in enumerate(input_devices):
            print(f"{i + 1}. {device['name']}")

        print("\nAvailable audio output devices:")
        for i, device in enumerate(output_devices):
            print(f"{i + 1}. {device['name']}")

    def play_wav_file(self, duration):
        try:
            pygame.mixer.init()
            sound = pygame.mixer.Sound(self.wav_file_path)

            # Play the WAV file for the specified duration
            sound.play()
            time.sleep(duration)

        except Exception as e:
            print(f"Error playing the WAV file: {e}")
        finally:
            pygame.mixer.quit()

if __name__ == "__main__":
    wav_file_path = r"C:\Users\SandeepRegalla\Documents\Audacity\chunk_1.wav"
    duration_to_play = 4 # Specify the duration in seconds

    if os.path.exists(wav_file_path):
        audio_manager = AudioManager(wav_file_path)
        audio_manager.get_audio_devices()
        audio_manager.play_wav_file(duration_to_play)
    else:
        print("File not found. Please check the path.")
