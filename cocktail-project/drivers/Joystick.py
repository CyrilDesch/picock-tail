import time
import grovepi

# Connect the Grove Joystick to analog port A0
yPin = None # Y axis pin
xPin = None # X axis pin

def setJoystickPort(setxPin, setyPin):
    global xPin, yPin
    xPin = setxPin
    yPin = setyPin
    grovepi.pinMode(xPin,"INPUT")
    grovepi.pinMode(yPin,"INPUT")



def getJoystickPosition():
    # Get joystick position
    x = grovepi.analogRead(xPin)
    y = grovepi.analogRead(yPin)

    # Calculate X,Y coordinates
    xScaled = (x - 512) / 10.24
    yScaled = (y - 512) / 10.24

    # Print the values
    return xScaled, yScaled



# getJoystickAction()
# Output : Joystick click or direction (String)
def getJoystickAction():
    x, y = getJoystickPosition()
    if x >= 40:
        return "CLICK"
    elif x >= 20:
        return "LEFT"
    elif x <= -20:
        return "RIGHT"
    elif y >= 20:
        return "DOWN"
    elif y <= -20:
        return "UP"
    else:
        return "CENTER"
    


# listenJoystick(callback) -> boolean
# Input : callback function taking joystickAction as parameter, and returning boolean (True if continue to listen)
# Output : True if continue to listen
def listenJoystick(callback):
    joystickAction = getJoystickAction()
    continueListening = callback(joystickAction)
    time.sleep(0.1)
    return continueListening