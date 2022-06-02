import time
from os import listdir
from os.path import isfile, join

from numpy import mean

from brightness import getBrightness
from street import voltage
import threading

streets = [r"C:\Users\yuvge\PycharmProjects\hackaton2022\street1",
           r"C:\Users\yuvge\PycharmProjects\hackaton2022\street2"]


class StreetThread(threading.Thread):
    def __init__(self, video):
        super().__init__()
        self.bright = []
        self.streetVideos = video

    def run(self):
        for video in self.streetVideos:
            print(video)
            streetThread = threading.Thread(target=getBrightness, args=(video, self.bright))
            streetThread.start()

        time.sleep(15)
        print(self.bright)
        meanBright = mean(self.bright)
        print(meanBright)
        voltage(meanBright, 0)


if __name__ == '__main__':
    for streetName in streets:
        videos = [str(join(streetName, f)) for f in listdir(streetName)
                  if (isfile(join(streetName, f)) and str(join(streetName, f)).split(".")[1] == "mp4")]
        print(videos)
        thread = StreetThread(videos)  # threading.Thread(target=currStreet, args=(videos,))
        thread.start()
