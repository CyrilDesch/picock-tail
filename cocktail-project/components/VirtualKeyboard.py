from drivers.LCD import setErrorRGB, setText
from drivers.Joystick import listenJoystick

class VirtualKeyboard():
  
  def __init__(self):
    # currentText : String -> Text inputed by user
    self.currentText = ""

    # currentInputIndex : Int -> Index of the current character in the virtual keyboard
    self.currentInputIndex = 0

    # charactersUppercase : List of 26 characters + back and enter in uppercase
    self.charactersUppercase = [chr(ord('A') + i) for i in range(26)]
    self.newCurrentInputIndex = None

    

  # Start the VirtualKeyboardView
  # Return text inputed by user
  def getInput(self):
    self.renderView()
    self.handleInput()
    return self.currentText



  # Render the LCD View :
  # - First line : currentText
  # - Second line : line of the virtual keyboard where the current character is uppercase
  def renderView(self):
    setText(self.currentText + "\n" + self.getInputHelperLine(self.currentInputIndex))



  # Handle input of the user on the virtual keyboard
  # End : update self.currentText
  def handleInput(self):
    # while user is inputing text
    while listenJoystick(callback=self.updateTextByJoystickAction): pass



  # Update the LCD View according to the joystick action
  def updateTextByJoystickAction(self, joystickAction):
    #Checks if the index has changed and if the text has changed
    indexChanged = False
    textChanged = False

    if joystickAction == "CLICK":
      # If index is in range of alphabet, add current character to currentText
      if self.currentInputIndex in range (0, 26):
        if len(self.currentText) < 16:
          newCurrentText = self.currentText + self.getCurrentCharacter(self.currentInputIndex)
          textChanged = True #Text has changed
        else :
          #print("DEBUG : Text too long")
          setErrorRGB()
      elif self.currentInputIndex == 26: # If index is 26, remove last character of currentText
        newCurrentText = self.currentText[:-1]
        textChanged = True #Text has changed
      elif self.currentInputIndex == 27:  # If index is 27, validate currentText and stop inputing
        return False

    elif joystickAction == "LEFT":
      # print("LEFT")
      if self.currentInputIndex > 0:
        newCurrentInputIndex = self.currentInputIndex - 1
        indexChanged = True #Index has changed

    elif joystickAction == "RIGHT":
      # print("RIGHT") 
      if self.currentInputIndex < 27:
        newCurrentInputIndex = self.currentInputIndex + 1
        indexChanged = True #Index has changed

    # Update currentInputIndex and display if needed
    if indexChanged:
      if newCurrentInputIndex != None:
        self.currentInputIndex = newCurrentInputIndex
        newCurrentInputIndex = None
        self.renderView()
    if textChanged:    
      if newCurrentText != None:
        self.currentText = newCurrentText
        newCurrentText = None
        self.renderView()

    return True
  


  # getInputHelperLine(index) -> String
  # Input : index (Int)
  # Output : String of 16 characters with index in Uppercase
  def getInputHelperLine(self, index):

    # Verify if index is in range
    if index < 0 and index > 27:
      index = index % 27
      # print("ERROR : Index out of range")

    # Create line with all characters in lowercase except selected character
    characters = [chr(ord('a') + i) for i in range(26)]
    characters.append("<")
    characters.append("+")
    if index < 26:
      characters[index] = self.charactersUppercase[index]
    
    # Set current line "centered" on index when possible
    currentLine = ""
    if index >= 8 and index <= 19:
        for i in range(index - 7, index + 8):
            currentLine += characters[i]
    if index < 8:
        for i in range(0, 15):
            currentLine += characters[i]
    if index > 19:
        for i in range(13, 28):
            currentLine += characters[i]
            
    return currentLine
  


  # getCurrentCharacter(index) -> String (1 character)
  # Input : index (Int)
  # Output : String of 1 character in Uppercase
  # Only for alphabet (index between 0 and 25), do not handle back and enter
  def getCurrentCharacter(self, index):
    return self.charactersUppercase[index]