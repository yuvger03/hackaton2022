from os import listdir
from os.path import isfile, join

from numpy import mean

from brightness import getBrightness
from street import voltage
import threading


class StreetThread(threading.Thread):
    def __init__(self, frames):
        super().__init__()
        self.bright = []
        self.frames = frames

    def run(self):
        # streetThread = threading.Thread(target=getBrightness, args=(self.frames, self.bright))
        # streetThread.start()
        getBrightness(self.frames, self.bright)
        # time.sleep(15)
        print(self.bright)
        meanBright = mean(self.bright)
        print(meanBright)
        voltage(meanBright, 0)


if __name__ == '__main__':
    streets = [r"C:\Users\liri\Desktop\street1", r"C:\Users\liri\Desktop\street2"]
    for streetName in streets:
        videos = [str(join(streetName, f)) for f in listdir(streetName)
                  if (isfile(join(streetName, f)) and str(join(streetName, f)).split(".")[1] == "jpg")]
        print(videos)
        thread = StreetThread(videos)
        thread.start()
