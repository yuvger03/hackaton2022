import cv2
import matplotlib.pyplot as plt
import cvlib as cv
import urllib.request
import numpy as np
from cvlib.object_detection import draw_bbox
import concurrent.futures
import time
import os
 
im=None
 
def run1():
    cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))
    cam = cv2.VideoCapture(0)
    while True:
        check, im = cam.read()
        out.write(im)
        bbox, label, conf = cv.detect_common_objects(im)
        num_of_people = len([l for l in label if l == 'person'])
        print("num_of_people", num_of_people)
        im = draw_bbox(im, bbox, label, conf)
 
        cv2.imshow('detection',im)
        key=cv2.waitKey(5)
        if key==ord('q'):
            break
    out.release()        
    cv2.destroyAllWindows()
        
def run2():
    url='http://192.168.43.172/cam-lo.jpg'

    cv2.namedWindow("detection", cv2.WINDOW_AUTOSIZE)
    path = 'D:\check'
    cam_index = 1
    duration_in_sec = 5

    frames = []
    people_num = []
    old_time = int(time.time())
    os.chdir(path)
    while True:
        img_resp=urllib.request.urlopen(url)
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        im = cv2.imdecode(imgnp,-1)
        frames.append(im)
        bbox, label, conf = cv.detect_common_objects(im)
        num_of_people = len([l for l in label if l == 'person'])
        people_num.append(num_of_people)
        # print("num_of_people", num_of_people)
        # im2 = draw_bbox(im, bbox, label, conf)
        if((int(time.time()) - old_time) % duration_in_sec == 0):
            for i, frame in enumerate(frames):
                cv2.imwrite(f"frame_{cam_index}_{i}.jpg", frame)

            with open("max_ppl.txt", 'a') as file:
                file.write(f" {str(max(people_num))}")
            
            frames = []
            num_of_people = []
        
        cv2.imshow('detection',im)
        key=cv2.waitKey(5)
        if key==ord('q'):
            break

    cv2.destroyAllWindows()
    # print(frames, max(people_num))
    return frames, max(people_num)
 
 
 
if __name__ == '__main__':
    print("started")
    with concurrent.futures.ProcessPoolExecutor() as executer:
            # f1= executer.submit(run1)
            f2 = executer.submit(run2)