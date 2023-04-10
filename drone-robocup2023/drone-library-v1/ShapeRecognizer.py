import numpy as np
import cv2
from MaskMaker import MaskMaker
from Action import *

import cv2
import numpy as np
from Shape import *


class ShapeRecognizer:

    def __init__(self):
        self.Q = Quadrilateral()
        self.T = Triangle()
        self.C = Circle()

        self.shapes = [self.Q, self.T, self.C]

        #objekty ktoré nás zaujímajú. Pozri taktiež Shape.py

        self.recognized_shapes_counters = {
            "Blue Quad": 0,
            "Red Quad": 0,
            "Blue Tri": 0,
            "Blue Cir": 0,
            "Red Cir": 0,
            "Red Tri": 0,
            "Yellow Cir": 0,
            "Green Cir": 0
            #QR CODE TO BE ADDED
        }
        #kedze rozoznávanie objektov nie je dokonalé, chce to nejaký room for error :)
        #tu sa nám možno bude hodiť nejaké počítadlo pre rozoznaný objekt.

    def clear_recog_shapes(self):
        for k in self.recognized_shapes_counters.keys():
            self.recognized_shapes_counters[k] = 0
            # keď rozozná nejaký útvar, ostatné vynuluje, toto je len pomocná metódna pre prečistenie chybne rozoznaných útvarov

    def evaluate_frame(self, frame):
        pass
        #tu moze byt napriklad funkcia ktorá bude prechadzat cez masky, zistovat z nich kontury
        #a bude vyhodnocovat ci sa v nom nejaky utvar nachadza (bude sa hodit predprogramovana funkcia Útvarov is_in_frame(masked_img) a taktiež pole dostupných rozoznávaných objektov self.shapes)

