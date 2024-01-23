import sounddevice as sd
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def get_audio_devices():
    devices = sd.query_devices()

    input_devices = [device for device in devices if 'input' in device['name']]
    output_devices = [device for device in devices if 'output' in device['name']]

    return input_devices, output_devices


def set_default_playback_device(device_index):
    all_devices = AudioUtilities.GetSpeakers()

    try:
        device = all_devices.GetItem(device_index)
    except IndexError:
        print("Invalid device index.")
        return

    interface = device.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)

    volume.SetMute(0, None)
    volume.SetMasterVolumeLevelScalar(1.0, None)


if __name__ == "__main__":
    input_devices, output_devices = get_audio_devices()

    print("Available audio output devices:")
    for i, device in enumerate(output_devices):
        print(f"{i + 1}. {device['name']}")

    selected_device_index = int(input("Enter the index of the desired output device to set as default: ")) - 1

    if 0 <= selected_device_index < len(output_devices):
        set_default_playback_device(selected_device_index)
        print(f"Default playback device set to {output_devices[selected_device_index]['name']}")
    else:
        print("Invalid device index.")
