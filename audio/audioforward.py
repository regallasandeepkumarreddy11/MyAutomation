from pydub import AudioSegment
import numpy as np

class AudioVerifier:
    def __init__(self, original_audio_file, forwarded_audio_file):
        self.original_audio = AudioSegment.from_file(original_audio_file)
        self.forwarded_audio = AudioSegment.from_file(forwarded_audio_file)

    def compareAudio(self):
        # Check if the lengths are the same
        if len(self.original_audio) != len(self.forwarded_audio):
            return False

        # Convert to numpy arrays for comparison
        originalArray = np.array(self.original_audio.get_array_of_samples())
        forwardedArray = np.array(self.forwarded_audio.get_array_of_samples())

        # Calculate the mean absolute error (MAE) between the two audio files
        mae = np.mean(np.abs(originalArray - forwardedArray))

        # Set a threshold based on your use case
        threshold = 1000  # Adjust as needed

        if mae < threshold:
            return True  # The audio appears to be original
        else:
            return False  # The audio may have been tampered with

if __name__ == '__main__':
    original_audio_file = r'C:\Users\SandeepRegalla\Documents\Audacity\silence.wav'  # Replace with the path to the original audio
    forwarded_audio_file = r'C:\Users\SandeepRegalla\Documents\Audacity\chunk_5.wav'  # Replace with the path to the forwarded audio

    verifier = AudioVerifier(original_audio_file, forwarded_audio_file)
    isOriginal = verifier.compareAudio()

    if isOriginal:
        print("The audio appears to be original.")
    else:
        print("The audio may have been forwarded with.")

