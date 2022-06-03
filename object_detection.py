import cv2
import cvlib as cv
import urllib.request
import numpy as np
from cvlib.object_detection import draw_bbox
import time
# import os


# im = None


def run1(path, cam_index):
    cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)

    cam = cv2.VideoCapture(0)
    frames = []
    people_num = []
    old_time = int(time.time())
    duration_in_sec = 5
    while True:
        check, im = cam.read()
        frames.append(im)
        bbox, label, conf = cv.detect_common_objects(im)
        num_of_people = len([l for l in label if l == 'person'])
        people_num.append(num_of_people)
        print("run2: ", max(people_num))
        # print("num_of_people", num_of_people)
        im2 = draw_bbox(im, bbox, label, conf)
        if (int(time.time()) - old_time) % duration_in_sec == 0:
            for i, frame in enumerate(frames):
                cv2.imwrite(f"{path}\\frame_{cam_index}_{i}.jpg", frame)

            with open(f"{path}\\max_ppl.txt", 'a') as file:
                file.write(f" {str(max(people_num))}")

            frames = []
            people_num = []

        cv2.imshow('detection', im2)
        key = cv2.waitKey(5)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()
    # print(frames, max(people_num))
    return frames, max(people_num)
    #
    #     bbox, label, conf = cv.detect_common_objects(im)
    #     num_of_people = len([l for l in label if l == 'person'])
    #     print("run1: num_of_people", num_of_people)
    #     im = draw_bbox(im, bbox, label, conf)
    #
    #     cv2.imshow('detection', im)
    #     key = cv2.waitKey(5)
    #     if key == ord('q'):
    #         break
    #
    # cv2.destroyAllWindows()


def run2(path=r"C:\Users\liri\PycharmProjects\hackaton2022\street1", cam_index=1):
    url = 'http://192.168.207.171/cam-lo.jpg'

    cv2.namedWindow("detection", cv2.WINDOW_AUTOSIZE)
    # path = 'D:\check'
    # cam_index = 1
    duration_in_sec = 5

    frames = []
    people_num = []
    old_time = int(time.time())
    # os.chdir(path)
    print("hello")
    while True:
        img_resp = urllib.request.urlopen(url)
        imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        im = cv2.imdecode(imgnp, -1)
        frames.append(im)
        bbox, label, conf = cv.detect_common_objects(im)
        num_of_people = len([l for l in label if l == 'person'])
        people_num.append(num_of_people)
        print("run2: ", max(people_num))
        # print("num_of_people", num_of_people)
        im2 = draw_bbox(im, bbox, label, conf)
        if (int(time.time()) - old_time) % duration_in_sec == 0:
            for i, frame in enumerate(frames):
                cv2.imwrite(f"{path}\\frame_{cam_index}_{i}.jpg", frame)

            with open(f"{path}\\max_ppl.txt", 'a') as file:
                file.write(f" {str(max(people_num))}")

            frames = []
            people_num = []

        cv2.imshow('detection', im2)
        key = cv2.waitKey(5)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()
    # print(frames, max(people_num))
    return frames, max(people_num)


# if __name__ == '__main__':
#     print("started")
#     # with concurrent.futures.ProcessPoolExecutor() as executer:
#     #     # f1= executer.submit(run1)
#     #     f2 = executer.submit(run2)
#     run2()
