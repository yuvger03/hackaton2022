import serial
import time
arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(1)


while True:
    volt = input()
    write_read(volt)
