from os import listdir
from os.path import isfile, join

from numpy import mean

from brightness import getBrightness
from street import voltage
from object_detection import run1, run2
import threading
import multiprocessing
from camera import write_read


import time


class StreetThread(threading.Thread):
    def __init__(self, frames, people):
        super().__init__()
        self.bright = []
        self.frames = frames
        self.people = people

    def run(self):
        # streetThread = threading.Thread(target=getBrightness, args=(self.frames, self.bright))
        # streetThread.start()
        getBrightness(self.frames, self.bright)
        # time.sleep(15)
        # print(self.bright)
        meanBright = mean(self.bright)
        print(meanBright)
        volt = voltage(meanBright, self.people)
        print(volt)
        write_read(volt)


def getDataVolt(streetNames):
    time.sleep(5)
    durationInSec = 10

    old_time = int(time.time())
    while True:
        if (int(time.time()) - old_time) % durationInSec == 0:
            for streetName in streetNames:
                videos = [str(join(streetName, f)) for f in listdir(streetName)
                          if (isfile(join(streetName, f)) and str(join(streetName, f)).split(".")[1] == "jpg")]
                # print(videos)

                with open(streetName+"\\max_ppl.txt", "r") as peopleFile:
                    peopleList = peopleFile.readline().split()
                    peopleListInt = [int(people) for people in peopleList]
                    avgPeople = mean(peopleListInt)

                    thread = StreetThread(videos, avgPeople)
                    thread.start()
                    thread.join()

                time.sleep(1)
                # delete whole data in the dir - for the new data that about to come
                # for f in os.listdir(streetName):
                #     os.remove(os.path.join(streetName, f))


if __name__ == '__main__':
    streets = [r"C:\Users\liri\PycharmProjects\hackaton2022\street1"]

    i = 0
    for streetName in streets:
        thread_detect = multiprocessing.Process(target=run1, args=(streetName, i))
        thread_detect.start()
        i += 1

    threadGetVolt = multiprocessing.Process(target=getDataVolt, args=(streets,))
    threadGetVolt.start()
