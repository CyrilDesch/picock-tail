import grovepi

# Connect the pumps to digital ports {"D7", "D8", "FLOP"}
pump1 = None # Pump 1 port
pump2 = None # Pump 2 port
pump3 = None # Pump 3 port
pumpDebit = 25 # ml/s

# setPumpPort : set the pumps port
# Input : Numbers of ports (Int), port (int) or nil if no pump
def setPumpPort(port1, port2, port3):
    global pump1, pump2, pump3
    if port1 != None:
        grovepi.pinMode(port1,"OUTPUT")
    if port2 != None:
        grovepi.pinMode(port2,"OUTPUT")
    if port3 != None:
        grovepi.pinMode(port3,"OUTPUT")
    # print("Pump port set to A" + str(port1) + ", A" + str(port2) + ", A" + str(port3))
    pump1 = port1
    pump2 = port2
    pump3 = port3
    


# switchOnPump : switch on the pump
def switchOnPump(pump):
    match pump:
        case 1:
            grovepi.digitalWrite(pump1,1) # Send HIGH to switch on
        case 2:
            grovepi.digitalWrite(pump2,1) # Send HIGH to switch on
        case 3:
            grovepi.digitalWrite(pump3,1) # Send HIGH to switch on
        case _:
            print("Error : pump not found") # Error message



# switchOffPump : switch off the pump
def switchOffPump(pump):
    match pump:
        case 1:
            grovepi.digitalWrite(pump1,0) # Send LOW to switch off
        case 2:
            grovepi.digitalWrite(pump2,0) # Send LOW to switch off
        case 3:
            grovepi.digitalWrite(pump3,0) # Send LOW to switch off
        case _:
            print("Error : pump not found") # Error message

def switchOffPumps():
    if pump1 != None:
        grovepi.digitalWrite(pump1,0)
    if pump2 != None:
        grovepi.digitalWrite(pump2,0)
    if pump3 != None:
        grovepi.digitalWrite(pump3,0)

#---------------------------------
# Warning : DO NOT LEAVE THE PUMP ON ON EXCEPT/INTERRUPT    