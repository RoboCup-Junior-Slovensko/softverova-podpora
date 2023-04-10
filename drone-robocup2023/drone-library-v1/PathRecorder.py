import time, cv2
from threading import Thread
from djitellopy import Tello


class PathRecorder:

    def __init__(self, tello: Tello):
        """
        Trieda slúžiaca na ukladanie videa zo steamu (obraz je už aj obrátený).
        metódy start a stop spustia/ukončia paralelný thread pre ukladanie frameov.
        :param tello: instancia tello
        """
        self.thread = None
        self.recording = False
        self.tello = tello
        self.fps = 30
        self.thread = Thread(target=self.read_video_stream)

    def read_video_stream(self):
        self.tello.streamon()
        frame_input = self.tello.get_frame_read()
        resolution = (960, 720)

        video = cv2.VideoWriter('output.avi',
                                cv2.VideoWriter_fourcc(*'MJPG'),
                                self.fps,
                                resolution)

        while self.recording:
            flipped_frame = cv2.flip(frame_input.frame, 0)
            video.write(flipped_frame)
            time.sleep(1 / self.fps)

        video.release()

    def start(self):
        self.recording = True
        self.thread.start()

    def stop(self):
        self.recording = False
        self.thread.join()
