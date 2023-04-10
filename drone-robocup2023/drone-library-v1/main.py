from PathFollower import PathFollower
from djitellopy import tello

tello = tello.Tello()
tello.connect()
tello.streamon()

PF = PathFollower(tello)

# tello.takeoff()
# time.sleep(2)


# A TU NECH SA DEJE MÁGIA :)

