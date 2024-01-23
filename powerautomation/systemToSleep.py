# import psutil
# import sys
# import platform
# import ctypes
#
# def put_system_to_sleep():
#     try:
#         if platform.system() == "Windows":
#             # On Windows, use the SetSuspendState function
#             ctypes.windll.powrprof.SetSuspendState(0, 1, 0)
#         else:
#             # On Linux/Mac, use the psutil library
#             psutil.os.system("sudo pm-suspend")
#     except Exception as e:
#         print(f"Error putting system to sleep: {e}")
#
# if __name__ == "__main__":
#     try:
#         put_system_to_sleep()
#     except KeyboardInterrupt:
#         print("Sleep interrupted.")
#         sys.exit(0)
import ctypes

def put_system_to_sleep():
    ctypes.windll.powrprof.SetSuspendState(0, 1, 0)

if __name__ == "__main__":
    put_system_to_sleep()
