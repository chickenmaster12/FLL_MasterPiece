from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F)
robot = DriveBase(left_motor, right_motor,wheel_diameter=63, axle_track=112)
robot.settings(420, 300, 180, 200)


def stage_spin():
    spotlight_spinner = Motor(Port.A)
    speaker = Motor(Port.E)
    speaker.run_angle(200, 220, wait=False)
    spotlight_spinner.run_angle(600, -520)

stage_spin()


