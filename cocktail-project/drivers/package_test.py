# This file is used to test drivers connexion and functions

from . import LCD, Joystick, Pump, Ultrasonic
import time

# Test the LCD connexion
LCD.setRGB(255, 255, 255)  # Set the background to white

# Set Joystick connexion
Joystick.setJoystickPort(0,1)  # Set the joystick port to A0

# Set Pumps connexion
Pump.setPumpPort(7,8, None)  # Set the pump port to D7, D8


try:
    while True:
        if Joystick.getJoystickAction() == "UP":
            LCD.setText("UP")
            Pump.switchOnPump(1)
        if Joystick.getJoystickAction() == "DOWN":
            LCD.setText("DOWN")
            Pump.switchOffPump(1)

        time.sleep(5)
        time.sleep(.1)
        
# Interruptions management :
# Keyboard interruption : CTRL + C
except KeyboardInterrupt:

    # TURN OFF ALL DRIVERS :
    # ---------------------------------
    # ---------------------------------

    print("KeyboardInterrupt")
    LCD.setText("Goodbye!")
# Other errors management :
except IOError:
    print("An IO error occurred.")