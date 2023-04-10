import time

import cv2
import numpy as np
from Movement import Movement
from ShapeRecognizer import ShapeRecognizer

from Action import *
from PathRecorder import PathRecorder


class PathFollower:
    """
    Hlavná Trieda, obsahuje inštanciu Triedy pohyb, recognizera a recordera, komunikuje priamo s dronom
    """
    def __init__(self, drone: Tello):
        self.drone = drone

        self.mov = Movement(self.drone)
        self.recognizer = ShapeRecognizer()
        self.recorder = PathRecorder(self.drone)

        self.actions = {
            "Blue Quad": RecordEnder(self.recorder),
            "Red Quad": RecordStarter(self.recorder),
            "Blue Tri": RightRotation(self.mov),
            "Red Tri": LeftRotation(self.mov),
            "Blue Cir": Podlet(self.mov),
            "Red Cir": Nadlet(self.mov),
            "Yellow Cir": Pristatie(self.mov),
            "Green Cir": ZdvihObete(self.mov)
        }
        #SLOVNÍK AKCIÍ DRONA, PRAKTICKÁ UKÁŽKA VYUŽITIA VO FUNKCII NIŽŠIE

    def check_recognized_shapes(self):
        """
        keďže sa nedá úplne presne spoľahnúť na to že rozpoznaný útvar sa tam naozaj nachádza, treba aj nejaký ten room pre error.
        Každý útvar má preto vyrobený counter. Konštantu, koľkokrát treba objekt rozoznať si môžte upraviť podľa vašej metodiky rozoznávania.
        :return:
        """
        for s in self.recognizer.recognized_shapes_counters.keys():
            curr = self.recognizer.recognized_shapes_counters[s]
            if curr > 20:
                self.actions[s].vykonaj()
                self.recognizer.recognized_shapes_counters.pop(s)
                # vykoná sa aktivita prislúchajúca útvaru a súčasne sa vyhodí z možných útvarov, keďže každý
                # útvar je na ceste práve raz
                self.recognizer.clear_recog_shapes()
                return



    def send_commands(self):
        self.drone.send_rc_control(self.mov.l_r, self.mov.fw_bw, self.mov.up_down, self.mov.rot)

    def set_movement(self, orig):
        """
        Funkcia ktorá má na starosti nastavovanie všetkých paramentrov triedy Movement.
        :param orig:
        :return:
        """
        pass

