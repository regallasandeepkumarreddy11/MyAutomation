from pydub import AudioSegment
class AudioAnalyzer:
    def __init__(self, audio_file, silence_threshold=-40):
        self.audio = AudioSegment.from_file(audio_file)
        self.silenceThreshold = silence_threshold
        self.silenceIntervals = []

    def detectSilence(self):
        start_time = None

        for i, chunk in enumerate(self.audio):
            if chunk.dBFS < self.silenceThreshold:
                if start_time is None:
                    start_time = i
            elif start_time is not None:
                end_time = i
                self.silenceIntervals.append((start_time, end_time))
                start_time = None

    def printSilenceInstances(self):
        if not self.silenceIntervals:
            print("No silence detected.")
        else:
            for i, (start, end) in enumerate(self.silenceIntervals):
                print(f"Silence instance {i+1}: {start/1000} ms to {end/1000} ms")

    def getTotalSilenceDuration(self):
        total_duration = len(self.audio)
        silence_duration = sum(end - start for start, end in self.silenceIntervals)
        return silence_duration / 1000  # Convert to seconds

    def getSilencePercentage(self):
        total_duration = len(self.audio)
        silence_duration = self.getTotalSilenceDuration()
        return (silence_duration / total_duration) * 100

if __name__ == '__main__':

    audio_file = r'C:\Users\SandeepRegalla\Documents\Audacity\silenceorig.mp3'  # Replace with your audio file's path
    analyzer = AudioAnalyzer(audio_file)
    analyzer.detectSilence()

    print(f"Total Silence Duration: {analyzer.getTotalSilenceDuration():.2f} seconds")
    print(f"Percentage of Silence: {analyzer.getSilencePercentage():.2f}%")
    analyzer.printSilenceInstances()

# print(f"Total Silence Duration: {silence_duration / 1000:.2f} seconds")
# print(f"Percentage of Silence: {silence_percentage:.2f}%")
