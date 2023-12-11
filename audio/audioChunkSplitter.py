from pydub import AudioSegment
from audio.audioVerification import AudioComparator
class AudioSplitter:
    def __init__(self, input_audio_file):
        self.audio = AudioSegment.from_file(input_audio_file)
        self.audioVerification = AudioComparator()
        self.originalAudioFile = r"C:\Users\SandeepRegalla\Documents\Audacity\Sine_0_8.wav"
        self.chunkFiles = []

    def splitAudio(self, output_folder, numChunks):
        # Calculate the duration of each chunk
        chunkLength = len(self.audio) // numChunks

        for i in range(numChunks):
            startTime = i * chunkLength
            endTime = (i + 1) * chunkLength

            # Extract the audio chunk
            audioChunk = self.audio[startTime:endTime]

            # Save the audio chunk to the output folder
            chunkFile = f"{output_folder}/chunk_{i + 1}.wav"
            print(chunkFile)
            audioChunk.export(chunkFile, format="wav")
            self.chunkFiles.append(chunkFile)
            print(self.chunkFiles)

    def verifyAudio(self):
        s = 0
        while s <= len(self.chunkFiles) -1:
            if s <= len(self.chunkFiles):
                self.audioVerification.compare_audio_similarity(inputAudioFile, self.chunkFiles[s])
                s = s+1

if __name__ == "__main__":
    inputAudioFile = r'C:\Users\SandeepRegalla\Documents\Audacity\diff.wav'  # Replace with the path to your input audio file
    outputFolder = r'C:\Users\SandeepRegalla\Documents\Audacity'  # Replace with the desired output folder
    numChunks = 5  # Replace with the number of chunks you want

    # Split the audio into chunks
    splitter = AudioSplitter(inputAudioFile)
    splitter.splitAudio(outputFolder, numChunks)
    splitter.verifyAudio()