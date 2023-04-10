import cv2
import numpy as np




class MaskMaker:
    """
    Trieda so statickými metódami na vytváranie masiek
    HSV intervaly pre farby si treba pozisťovať pomocou skriptu hsv_trackbar_tello_realtime.py
    """
    @staticmethod
    def make_red_mask(frame):
        red_lower1 = np.array([0, 0, 0])
        red_upper1 = np.array([0, 0, 0])
        red_lower2 = np.array([0, 0, 0])
        red_upper2 = np.array([0, 0, 0])
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask1 = cv2.inRange(hsv, red_lower1, red_upper1)
        mask2 = cv2.inRange(hsv, red_lower2, red_upper2)
        return mask1 + mask2

    @staticmethod
    def make_blue_mask(frame):
        blue_lower = np.array([0, 0, 0])
        blue_upper = np.array([0, 0, 0])
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, blue_lower, blue_upper)
        return mask

    @staticmethod
    def make_green_mask(frame):
        green_lower = np.array([0, 0, 0])
        green_upper = np.array([0, 0, 0])
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, green_lower, green_upper)
        return mask

    @staticmethod
    def make_yellow_mask(frame):
        yellow_lower = np.array([0, 0, 0])
        yellow_upper = np.array([0, 0, 0])
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
        return mask

    @staticmethod
    def make_black_mask(frame):
        lower_black = np.array([0, 0, 0])
        upper_black = np.array([0, 0, 0])
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_black, upper_black)
        return mask

    @staticmethod
    def make_dict_of_colors(frame):
        masks = {
            "Red": MaskMaker.make_red_mask(frame),
            "Blue": MaskMaker.make_blue_mask(frame),
            "Green": MaskMaker.make_green_mask(frame),
            "Yellow": MaskMaker.make_yellow_mask(frame)
        }
        return masks
