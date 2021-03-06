import time

from numpy import mean

from brightness import getBrightness
import threading

cameras = [r"C:\Users\yuvge\OneDrive\Рабочий стол\21.mp4", r"C:\Users\yuvge\OneDrive\Рабочий стол\21.mp4",
           r"C:\Users\yuvge\OneDrive\Рабочий стол\21.mp4"]


def voltage(meanBrightness, people):
    timeNow = time.localtime()
    hourNow = int(time.strftime("%H", timeNow))
    minutesNow = int(time.strftime("%M", timeNow))
    totalTime = hourNow * 60 + minutesNow
    # print(hourNow, minutesNow, meanBrightness, people)
    if (totalTime < 6*60 + 30) or (totalTime > 17*60 + 30):
        if meanBrightness < 180:
            volt = 200
        elif meanBrightness < 200:
            volt = 150
        else:
            volt = 0

        if people > 10:
            volt += 50
        elif people > 5:
            volt += 25

    else:
        volt = 0

    return volt


if __name__ == '__main__':
    for video in cameras:
        thread = threading.Thread(target=getBrightness, args=(video,))
        thread.start()

    # time.sleep(15)
    # print(bright)
    # meanBright = mean(bright)
    # print(meanBright)
