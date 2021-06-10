from utils import *
import cv2
import time

w = 360
h = 240

drone = initializeTello()

while True:
    drone.connect()
    
    img = telloGetFrame(drone, w, h)

    cv2.imshow('Image', img)

    found_commands = findCommand(img)

    decodeCommand(drone, found_commands)

    # cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        drone.land();
        break