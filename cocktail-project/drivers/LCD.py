import time
import smbus

bus = smbus.SMBus(1) # I2C bus number : 1

DISPLAY_RGB_ADDR = 0x62 # Show background
DISPLAY_TEXT_ADDR = 0x3e # Show characters

# setRGB : set the color of the background
# Input : red, green, blue (0~255) for each color
# Output : None
def setRGB(red, green, blue):
    # Initialize the device
    bus.write_byte_data(DISPLAY_RGB_ADDR,0x00,0x00)
    bus.write_byte_data(DISPLAY_RGB_ADDR,0x01,0x00)
    bus.write_byte_data(DISPLAY_RGB_ADDR,0x08,0xaa)
    # Set color
    bus.write_byte_data(DISPLAY_RGB_ADDR,4,red)
    bus.write_byte_data(DISPLAY_RGB_ADDR,3,green)
    bus.write_byte_data(DISPLAY_RGB_ADDR,2,blue)
    


# textCommand : send command to the text display
# Input : cmd (command)
# Output : None
def textCommand(cmd):
    bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,cmd)
    time.sleep(0.0001)



# setText : send text to the text display
# Input : text (string) 32 characters max
# Output : None
# Note : \n or 16 characters starts the second line
def setText(text):
    textCommand(0x01) # Clear display
    time.sleep(0.05)
    textCommand(0x08 | 0x04) # Display on, no cursor
    textCommand(0x28) # 2 lines
    time.sleep(0.05)
    count = 0
    row = 0
    for c in text:
        if c == '\n' or count == 16:
            count = 0
            row += 1
            if row == 2:
                return
            textCommand(0xc0)
            if c == '\n':
                continue
        count += 1
        bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))
#---------------------------------
# Testing the display
# setRGB(0,128,64) # Set the color to blue
# setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit.") # Display "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        

# setErrorRGB : set the color to red for 0.5 second
def setErrorRGB():
    setRGB(255, 0, 0)
    time.sleep(0.5)
    setRGB(255, 255, 255)