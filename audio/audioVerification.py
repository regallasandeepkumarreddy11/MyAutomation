import librosa
from scipy.spatial import distance

class AudioComparator:
    def __init__(self):
        pass

    def calculate_mfcc(self, audio_file):
        try:
            # Load the audio file
            audio_data, sample_rate = librosa.load(audio_file)

            # Extract MFCC features
            mfcc = librosa.feature.mfcc(y=audio_data, sr=sample_rate)
            return mfcc

        except Exception as e:
            print(f"Error calculating MFCC features for {audio_file}: {str(e)}")
            return None

    def compare_audio_similarity(self, original_audio_file, forwarded_audio_file):
        try:
            # Calculate MFCC features for both audio files
            mfcc1 = self.calculate_mfcc(original_audio_file)
            mfcc2 = self.calculate_mfcc(forwarded_audio_file)

            if mfcc1 is not None and mfcc2 is not None:
                # Ensure both MFCC arrays have the same length
                min_length = min(mfcc1.shape[1], mfcc2.shape[1])
                mfcc1 = mfcc1[:, :min_length]
                mfcc2 = mfcc2[:, :min_length]

                # Calculate the distance between the two sets of MFCC features
                dist = distance.cosine(mfcc1.flatten(), mfcc2.flatten())
                print(dist)

                # Convert the cosine distance to a similarity percentage
                similarity_percentage = (1 - dist) * 100
                if similarity_percentage >= 100:
                    print("There is a change in the audio")
                else:
                    print("There is no change in the audio file")
                return similarity_percentage

        except Exception as e:
            print(f"Error comparing audio files: {str(e)}")

        return None
