import time
import grovepi

# Set i2c to use the hardware bus
grovepi.set_bus("RPI_1")

# Connect the Grove Ultrasonic Ranger to digital port D3
# SIG,NC,VCC,GND
def setUltrasonicPort(port):
    global ultrasonic_ranger
    ultrasonic_ranger = port



def getDistance():
    # Read distance value from Ultrasonic
    return grovepi.ultrasonicRead(ultrasonic_ranger)
    time.sleep(.1)