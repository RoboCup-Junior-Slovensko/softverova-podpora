from djitellopy import Tello
import cv2
import pytesseract
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
config = r'--oem 0'

my_delay = 3

def initializeTello():
    myDrone = Tello()
    myDrone.connect()
    myDrone.for_back_velocity = 0
    myDrone.left_right_velocity = 0
    myDrone.left_left_velocity = 0
    myDrone.yaw_velocity = 0
    myDrone.speed = 0
    print(myDrone.get_battery())
    myDrone.streamoff()
    myDrone.streamon()
    return myDrone

def telloGetFrame(myDrone, w=360, h=240):
    myFrame = myDrone.get_frame_read();
    myFrame = myFrame.frame
    img = cv2.resize(myFrame, (w,h))
    return img

def findCommand(img):    

    found_commands = []

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    ret, thresh1 = cv2.threshold(gray, 180, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))

    dilation = cv2.dilate(thresh1, rect_kernel)

    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        if w < 200 and w > 50: # filter noise
            cropped = gray[y:y + h, x:x + w]
            text = pytesseract.image_to_string(cropped)

            rect = cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if text != '':
                found_commands.append(text)

        cv2.imshow('Thresh', thresh1)
        cv2.imshow('gray', gray)
        cv2.imshow('dilation', dilation)
        cv2.imshow('rect', gray)

    return found_commands

def decodeCommand(drone, found_commands):
    found = False
    for fc in found_commands:
        # print(fc)
        if('Takeoff' in fc):
            drone.connect()
            time.sleep(my_delay)
            drone.takeoff()
            break
        elif('Flip' in fc):
            print('found flip')
            drone.connect()
            time.sleep(my_delay)
            drone.flip_back()
            break
        elif('Land' in fc):
            drone.connect()
            time.sleep(my_delay)
            drone.land()
            break
        if('Rotate' in fc):
            drone.connect()
            time.sleep(my_delay)
            drone.rotate_clockwise(90)
            break
    
