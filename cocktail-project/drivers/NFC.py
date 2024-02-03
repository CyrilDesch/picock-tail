import RPi.GPIO as GPIO
from drivers.python_pn532.pn532 import *

GPIO.setwarnings(False)

# pn532 = PN532_SPI(debug=False, reset=20, cs=4)
pn532 = PN532_I2C(debug=False, reset=20, req=16)
# pn532 = PN532_UART(debug=False, reset=20)

ic, ver, rev, support = pn532.get_firmware_version()
# print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

# Configure PN532 to communicate with MiFare cards
pn532.SAM_configuration()

def read_card():
    # Check if a card is available to read
    uid = pn532.read_passive_target(timeout=0.1)
    if uid is None:
        return None
    else:
        return uid