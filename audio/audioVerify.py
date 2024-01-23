from audio.audioVerification import AudioComparator

class AudioVerify:
    def __init__(self):
        # If AudioComparator requires parameters, pass them here
        self.audioVerification = AudioComparator()

    def VerifyAudio(self, originalAudio, recordedAudio):
        # Store percentage as an instance variable if needed later
        self.Percentage = self.audioVerification.compare_audio_similarity(originalAudio, recordedAudio)
        return self.Percentage

if __name__ == '__main__':
    a = AudioVerify()
    originalAudioFile = r"./audio/chunk_1.wav"  # Replace with the path to the original audio
    recordedAudioFile = r"./audio/chunk_1.wav"
    resultPercentage = a.VerifyAudio(originalAudioFile, recordedAudioFile)
    print(f"Audio similarity percentage: {resultPercentage}")
