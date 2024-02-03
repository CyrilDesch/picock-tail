from drivers.LCD import setText
from drivers.Joystick import listenJoystick

class SelectionMenu():

  # Constructor
  # Args :
  # - menu : List of the menu items (max 12 chars) 
  def __init__(self, title, menu):
    self.title = title
    self.menu = menu
    self.currentIndex = 0
    self.renderView()


    
  # Handle the menu selection
  # Return: index of the selected item on the list
  def handleMenuSelection(self):
    while listenJoystick(callback=self.updateCurrentIndexByJoystickAction): pass
    return self.currentIndex
  


  # Render the view of the menu
  def renderView(self):
    textToPrint = ""
    if self.currentIndex == 0:
      textToPrint += f"{self.title}\n"
      textToPrint += f"{self.currentIndex + 1}.{self.menu[self.currentIndex][:12]} O\n"
    else:
      textToPrint += f"{self.currentIndex + 1}.{self.menu[self.currentIndex][:12]} O\n"
      if self.currentIndex < len(self.menu) - 1:
        textToPrint += f"{self.currentIndex + 2}.{self.menu[self.currentIndex + 1][:12]}\n"
    setText(textToPrint)



  # Update current index of the menu based on joystick action and render the view
  # Return: True if the action is not a click
  def updateCurrentIndexByJoystickAction(self, joystickAction):
    if joystickAction == "CLICK":
      return False
    elif joystickAction == "UP":
      if self.currentIndex > 0:
        self.currentIndex -= 1
      self.renderView()
    elif joystickAction == "DOWN":
      if self.currentIndex < len(self.menu) - 1:
        self.currentIndex += 1
      self.renderView()
    return True