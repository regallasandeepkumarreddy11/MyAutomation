import ctypes
import os
import sys
import platform
import subprocess

class SystemControlls:
    def __init__(self):
        self.adminPrivilegesEnabled = False

    def isSystemInOs(self):
        # Check if the system is in an operating system.
        print(platform.system())
        if platform.system() == "Windows":
            print("system is in OS")

    def requestAdminPrivileges(self):
        if ctypes.windll.shell32.IsUserAnAdmin() == 0:
            # If not running as admin, request elevation and restart script with admin privileges.
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
            sys.exit(0)
        self.adminPrivilegesEnabled = True

    def enableHibernateMode(self):
        if not self.adminPrivilegesEnabled:
            self.requestAdminPrivileges()
        os.system('powercfg -h on')
        print("Hibernate mode has been enabled.")

    def isHibernateAvailable(self):
            try:
                # Run the 'powercfg' command to query available sleep states
                result = subprocess.run(['powercfg', '-a'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                if result.returncode == 0:
                    output_lines = result.stdout.split('\n')
                    print(output_lines)
                    available_states = []
                    unavailable_states = []

                    for line in output_lines:
                        if "hibernate" in line:
                            if "available" in line:
                                available_states.append("Hibernate")
                            else:
                                unavailable_states.append("Hibernate")

                    if available_states:
                        print("The following sleep states are available on this system:")
                        for state in available_states:
                            print(f"    {state}")
                    else:
                        print("Hibernate is not available on this system.")

                    if unavailable_states:
                        print("\nThe following sleep states are not available on this system:")
                        for state in unavailable_states:
                            print(f"    {state}")
                    else:
                        print("All other sleep states are available on this system.")

                else:
                    print("Error running 'powercfg' command:")
                    print(result.stderr)

            except Exception as e:
                print(f"An error occurred: {str(e)}")


    def putSystemToHibernation(self):
        if not self.adminPrivilegesEnabled:
            self.requestAdminPrivileges()
        os.system('shutdown /h')

    def disableAdminPrivileges(self):
        if self.adminPrivilegesEnabled:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 0)
            sys.exit(0)

    def disableHibernateMode(self):
        if not self.adminPrivilegesEnabled:
            self.requestAdminPrivileges()
        os.system('powercfg -h off')
        print("Hibernate mode has been enabled.")

    def performHibernationProcess(self):
        self.enableHibernateMode()
        self.putSystemToHibernation()
        self.disableAdminPrivileges()

if __name__ == "__main__":
    controller = SystemControlls()
    controller.isHibernateAvailable()
