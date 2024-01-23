import os
import psutil
import shutil

def get_connected_disks():
    partitions = psutil.disk_partitions()

    connected_disks = []

    for partition in partitions:
        if partition.device and 'loop' not in partition.device:
            connected_disks.append(partition.device)

    print("The available harddisk",connected_disks)

    return connected_disks

def copy_file_to_d_drive(file_path):
    d_drive_path = "D:\\"
    destination_directory = "D:\\copiedfiles\\"
    destination_path = os.path.join(destination_directory, os.path.basename(file_path))

    try:
        # Check if the destination directory exists, create it if not
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        shutil.copy(file_path, destination_path)
        print(f"File successfully copied to D drive: {destination_path}")
    except Exception as e:
        print(f"Error copying the file: {e}")

if __name__ == "__main__":
    file_to_copy = "C:\\Automation_Doc\\WindowsAutomation.pptx"

    connected_disks = get_connected_disks()

    if "D:\\" in connected_disks:
        copy_file_to_d_drive(file_to_copy)
    else:
        print("D drive not found. Please ensure it is connected.")
