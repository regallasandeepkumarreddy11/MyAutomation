import subprocess

class SoundVolumeViewCommandExecutor:
    def __init__(self, executable_path=r'C:\Users\SandeepRegalla\MyAutomation\MyAutomation\\Tools\soundvolumeview-x64\SoundVolumeView.exe'):
        self.executable_path = executable_path

    def execute_command(self, command):
        sound_volume_command = self.executable_path +" "+ command
        print(sound_volume_command)
        try:
            result = subprocess.run(sound_volume_command, capture_output=True, text=True, check=True)
            output = result.stdout.strip()
            return output
        except subprocess.CalledProcessError as e:
            print(f"Error while executing the command: {e}")
            return None

    def get_percent(self):
        getVolumeCommand = r'C:\Users\SandeepRegalla\MyAutomation\MyAutomation\Tools\getvolume.exe'
        result = subprocess.run(getVolumeCommand).stdout
        result =result
        return result

    def set_volume(self, name, volume):
        command = f'/SetVolume {name} {volume}'
        getVolumeCommand = self.executable_path + command
        result = subprocess.run(getVolumeCommand)
        print(result)
        return result

    # def change_volume(self, name, volume_change):
    #     command = f'/ChangeVolume {name}{volume_change}'
    #     return self.execute_command(command)

    # Add more methods for other commands as needed

if __name__ == "__main__":
    # Example usage:
    executor = SoundVolumeViewCommandExecutor()

    # GetPercent [Name]
    name = "H(Realtek(R) Audio)"
    percent_result = executor.get_percent()
    print(" is the current volume ")

    # SetVolume [Name] [Volume]
    volume = 57
    executor.set_volume(name, volume)
    print(f"Volume set to {volume}")

    # # ChangeVolume [Name] [Volume]
    # volume_change = -10
    # executor.change_volume(name, volume_change)
    # print(f"Volume decreased by {abs(volume_change)}")

    # name = "H(Realtek(R) Audio)"
    # percent_result = executor.get_percent()
    # print(" is the current volume ")

