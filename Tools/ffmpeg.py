import subprocess
import platform
import time

def record_audio(output_file, duration=10, input_device='default'):
    # Check the operating system to set the appropriate FFmpeg command
    if platform.system() == 'Windows':
        input_format = 'dshow'
        ffmpeg_cmd = 'ffmpeg.exe'
    elif platform.system() == 'Darwin':  # macOS
        input_format = 'avfoundation'
        ffmpeg_cmd = 'ffmpeg'
    else:
        print("Unsupported operating system")
        return

    # FFmpeg command to record audio for a specified duration from a specific input device
    cmd = [
        ffmpeg_cmd,
        '-f', input_format,
        '-i', input_device,  # Specify the input audio device (e.g., 'default' or device index)
        '-t', str(duration),  # Set the recording duration in seconds
        output_file  # Specify the output file path
    ]

    try:
        # Run the FFmpeg command
        subprocess.run(cmd, check=True)
        print(f"Audio recorded successfully to {output_file}")

    except subprocess.CalledProcessError as e:
        print(f"Error while recording audio: {e}")

if __name__ == "__main__":
    # Specify the output file path
    output_file = "output_audio.wav"

    # Specify the recording duration (in seconds)
    duration = 10

    # Specify the input audio device (use 'default' or device index)
    input_device = 'default'

    # Record audio
    record_audio(output_file, duration, input_device)
