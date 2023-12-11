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

    def removeSilence(self):
        audio_without_silence = self.audio
        for start, end in self.silenceIntervals:
            audio_without_silence = audio_without_silence[:start] + audio_without_silence[end:]

        return audio_without_silence

    def getTotalSilenceDuration(self):
        silence_duration = sum(end - start for start, end in self.silenceIntervals)
        silence_duration = sum(end - start for start, end in self.silenceIntervals)
        return silence_duration / 1000  # Convert to seconds


    def getSilencePercentage(self):
        total_duration = len(self.audio)
        silence_duration = self.getTotalSilenceDuration()
        return (silence_duration / total_duration) * 100

if __name__ == '__main__':

    audio_file = r'C:\Users\SandeepRegalla\Documents\Audacity\silence.wav'   # Replace with your audio file's path
    analyzer = AudioAnalyzer(audio_file)
    analyzer.detectSilence()

    # Remove silence and save the output with the same name
    audio_without_silence = analyzer.removeSilence()
    audio_without_silence.export(audio_file, format="wav")

    print(f"Total Silence Duration: {analyzer.getTotalSilenceDuration():.2f} seconds")
    print(f"Percentage of Silence: {analyzer.getSilencePercentage():.2f}%")
