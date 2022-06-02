from PIL import Image, ImageStat
import math
import cv2


def getFrame(videoPath):
    cap = cv2.VideoCapture(videoPath)
    i = 0
    bright = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if i % 200 == 0:
            cv2.imwrite('frame' + str(i) + '.jpeg', frame)
            bright.append(brightness('frame' + str(i) + '.jpeg'))
            if i > 200 * 2 * 60 / 8:
                bright.pop(0)
        i += 1

    return bright


def howMuchLight(bright, people):
    avg = sum(bright) / len(bright)
    voltage = 0

    if bright < 100:
        voltage = max
    elif bright < 150:

    if people > 10:
        voltage += x
    elif people > 5:
        voltage += y

    return voltage


def brightness(im_file):
    im = Image.open(im_file)
    stat = ImageStat.Stat(im)
    gs = []
    for r, g, b in im.getdata():
        if (r, g, b) != (255.0, 255.0, 255.0):
            gs.append(math.sqrt(0.241 * (r ** 2) + 0.691 * (g ** 2) + 0.068 * (b ** 2)))
    print(sum(gs) / stat.count[0])
    return sum(gs) / stat.count[0]


if __name__ == '__main__':
    brightness(r"C:\Users\yuvge\OneDrive\Рабочий стол\אוניברסיטה\assembly\abbey-road-london.png")
