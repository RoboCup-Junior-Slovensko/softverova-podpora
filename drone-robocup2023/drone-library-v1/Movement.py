from djitellopy import Tello

class Movement:
    """
    Trieda ktorá má na starosti držanie aktuálnych dát o pohybe drona/specialnych úkonoch drona
    """
    def __init__(self, drone : Tello):
        self.l_r = 0
        self.fw_bw = 0
        self.up_down = 0
        self.rot = 0

        self.drone = drone

        self.podlet = False
        self.nadlet = False

        self.special_action = False

