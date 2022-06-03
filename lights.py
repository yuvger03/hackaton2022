import serial
import time
from object_detection import run2

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

# arduino.close()
# arduino.open()


def write_read(x):
    # arduino.open()
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(1)
    # arduino.close()


# while True:
#     volt = input()
#     write_read(volt)
# volt = 200
# write_read(str(volt))
# volt = 200
# write_read(str(volt))