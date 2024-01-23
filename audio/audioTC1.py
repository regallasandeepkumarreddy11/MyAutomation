from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import COMError


def get_default_audio_device():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    # volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Return the friendly name of the default audio device
    return devices.GetFriendlyName()


def set_default_audio_device(device_name):
    try:
        all_devices = AudioUtilities.GetSpeakers()
        print(all_devices)

        for dev in all_devices:
            if dev.GetFriendlyName() == device_name:
                dev.SetDefaultEndpoint()
                print(f"{device_name} set as the default audio device.")
                return

        print(f"Device {device_name} not found.")
    except COMError as e:
        print(f"COMError: {e}")


# Example usage
desired_device_name = "Speakers (Sound Blaster Play! 3)"
set_default_audio_device(desired_device_name)

# Optionally, you can print the default audio device after setting it
default_device = get_default_audio_device()
print(f"Default Audio Device: {default_device}")
