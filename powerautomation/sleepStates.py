import subprocess

def isHibernateAvailable():
    try:
        # Run the 'powercfg' command to query available sleep states
        result = subprocess.run(['powercfg', '-a'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result)
        if result.returncode == 0:
            # Check if "Hibernation" is listed in the output
            if "Hibernate" in result.stdout:
                print("Hibernation is available on this system.")
            else:
                print("Hibernation is not available on this system.")
        else:
            print("Error running 'powercfg' command:")
            print(result.stderr)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    isHibernateAvailable()
