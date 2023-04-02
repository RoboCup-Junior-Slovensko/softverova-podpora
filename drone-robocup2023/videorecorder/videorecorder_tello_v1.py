import cv2
import threading
import time
from djitellopy import Tello

tello = Tello()
tello.connect()
tello.streamon()

filename = 'output.avi'
frames_per_second = 45
frame_size = (960, 720)
video_writer = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'MJPG'), frames_per_second, frame_size)

def read_video_stream():
    while True:
        frame = tello.get_frame_read().frame
        video_writer.write(frame)
        cv2.imshow("f",frame)
        cv2.waitKey(1)

        if not recording:
            break

recording = True
video_thread = threading.Thread(target=read_video_stream)
video_thread.start()

time.sleep(10)

recording = False
video_thread.join()
print("donatacane")

video_writer.release()
tello.streamoff()