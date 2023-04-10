import threading
import time

import cv2
from djitellopy import Tello
from time import sleep
from PathRecorder import PathRecorder
from Movement import Movement
from MaskMaker import MaskMaker
from threading import Thread
import numpy as np


# SÚBOR S TRIEDAMI KTORÉ MAJÚ VŠETKY SPOLOČNÚ FUNKCIU vykonaj(). NIEKTORÉ UŽ SÚ NAPROGRAMOVANÉ, ZVYŠOK JE NA VÁS
# IMPLEMENTÁCIU NÁJDETE V SÚBORE PathFollower.py


class RightRotation:
    """
    Otočka 360 stupňov vpravo
    """

    def __init__(self, mov: Movement):
        self.mov = mov
        self.threadik = Thread(target=self.spinuj)

    def vykonaj(self):
        self.threadik.start()
        self.threadik.join()

    def spinuj(self):
        self.mov.drone.send_rc_control(0, 0, 0, 90)
        print("SPIUJEM DOPRAVA")
        time.sleep(4)
        print("DOSPINOVAL SOM")


class LeftRotation:
    """
    Otočka 360 stupňov vľavo
    """
    def __init__(self, mov: Movement):
        self.mov = mov
        self.threadik = Thread(target=self.spinuj)

    def vykonaj(self):
        self.threadik.start()
        self.threadik.join()

    def spinuj(self):
        self.mov.drone.send_rc_control(0, 0, 0, -90)
        print("SPIUJEM DOLAVA")
        time.sleep(4)
        print("DOSPINOVAL SOM")


class RecordStarter:
    """
    Zapnutie nahrávania videa
    """

    def __init__(self, recorder: PathRecorder):
        self.recorder = recorder

    def vykonaj(self):
        if not self.recorder.recording:
            self.recorder.recording = True
            self.recorder.start()


class RecordEnder:

    """
    Vyypnutie nahrávania videa
    """
    def __init__(self, recorder: PathRecorder):
        self.recorder = recorder

    def vykonaj(self):
        if self.recorder.recording:
            self.recorder.recording = False
            self.recorder.stop()


class Podlet:
    """
    kludne si dodefinujte svoje vlastné metódy, jeden zo sposobov je napriklad si dodefinovať ešte jeden Thread, ktorý
    nejako bude upravovať výšku letu drona

    syntax :
    premenna = threading.Thread(target=funkcia_ktoru_ma_thread_vykonat)
    premenna.start() spustí thread
    premenna.join() sposobí, že hlavný thread bude čakať, kým sa thread "premenna" dokonci (toto ale nie vzdy/hned chceme vyuzit)
    """
    def __init__(self, mov: Movement):
        self.mov = mov
        self.dlzka_podletu = None

    def vykonaj(self):
        pass




class Nadlet:
    """
    platí to isté čo o triedu vyššie
    """
    def __init__(self, mov: Movement):
        self.mov = mov
        self.dlzka_nadletu = None

    def vykonaj(self):
        pass




class ZdvihObete:

    def __init__(self, mov: Movement):
        self.mov = mov

    def vykonaj(self):
        pass
        # Váš kód na zdvihnutie obete


class Pristatie:

    def __init__(self, mov: Movement):
        self.mov = mov

    def vykonaj(self):
        pass
        # Váš kód na pristátie drona
