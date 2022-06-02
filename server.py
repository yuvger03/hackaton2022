import time
from os import listdir
from os.path import isfile, join

from numpy import mean

from brightness import bright, getBrightness
from street import voltage
import threading

streets = [r"street1", r"street2"]


def currStreet(streetVideos):
    for video in streetVideos:
        streetThread = threading.Thread(target=getBrightness, args=(video,))
        streetThread.start()

    time.sleep(15)
    print(bright)
    meanBright = mean(bright)
    print(meanBright)
    voltage(meanBright, 0)


if __name__ == '__main__':

    for street in streets:
        videos = [str(join(street, f)) for f in listdir(street) if (isfile(join(street, f))
                                                                    and str(join(street, f)).split(".")[1] == "mp4")]
        thread = threading.Thread(target=currStreet, args=(videos,))
