import time

from brightness import bright, getBrightness
import threading

cameras = [r"C:\Users\yuvge\OneDrive\Рабочий стол\21.mp4", r"C:\Users\yuvge\OneDrive\Рабочий стол\21.mp4", r"C:\Users\yuvge\OneDrive\Рабочий стол\21.mp4"]


for video in cameras:
    thread = threading.Thread(target=getBrightness, args=(video,))
    thread.start()


time.sleep(15)
print(bright)


