import os
import shutil
import subprocess

class FileCopier:
    def __init__(self, file_path):
        self.file_path = file_path
        self.external_devices = self.detect_external_devices()

    def detect_external_devices(self):
        external_devices = []
        # Use subprocess to call system command 'mount'
        try:
            result = subprocess.run(['mount'], text=True, capture_output=True)
            output_lines = result.stdout.splitlines()

            for line in output_lines:
                # Check if the device is removable or cdrom
                if 'removable' in line or 'cdrom' in line:
                    device_info = line.split()
                    external_devices.append(device_info[0])

        except Exception as e:
            print(f"Error detecting external devices: {e}")

        return external_devices

    def copy_file_to_external_device(self, destination_device):
        if os.path.exists(self.file_path):
            destination_path = os.path.join(destination_device, os.path.basename(self.file_path))
            try:
                shutil.copy2(self.file_path, destination_path)
                print(f"File copied successfully to {destination_device}")

                # Confirm the file by checking existence and size
                if os.path.exists(destination_path):
                    original_size = os.path.getsize(self.file_path)
                    copied_size = os.path.getsize(destination_path)
                    if original_size == copied_size:
                        print("File successfully confirmed.")
                    else:
                        print("File size mismatch. Copy may not be successful.")
                else:
                    print("Error: Copied file not found on the destination device.")

            except Exception as e:
                print(f"Error copying file: {e}")
        else:
            print("File not found.")

    def run(self):
        if self.external_devices:
            print("Detected external devices:")
            for idx, device in enumerate(self.external_devices, start=1):
                print(f"{idx}. {device}")

            selected_device_idx = int(input("Enter the number of the device to copy the file to: "))

            if 1 <= selected_device_idx <= len(self.external_devices):
                selected_device = self.external_devices[selected_device_idx - 1]
                self.copy_file_to_external_device(selected_device)
            else:
                print("Invalid selection.")
        else:
            print("No external devices detected.")


if __name__ == "__main__":
    file_to_copy = "C:\Automation_Doc\WindowsAutomation.pptx"  # Replace with the path to your file
    file_copier = FileCopier(file_to_copy)
    file_copier.run()
