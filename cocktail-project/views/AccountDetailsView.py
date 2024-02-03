from drivers.Joystick import getJoystickAction
from drivers.LCD import setText
from database.order import Order
from datetime import datetime

class AccountDetailsView():
  # Global variables for the view
  currentIndex = 0
  currentUser = None

  def __init__(self):
    self.currentIndex = 0


  # handleDetailsView : show the account details view
  # and allow the user to navigate through the different
  # Input : User
  # Output : None
  # Diplays
  async def handleDetailsView(self, user):
    # Set the global variables and assign the user
    global currentUser
    currentUser = user
    # Set the joystick action to an empty
    joystickAction = ""
    # print("Account Details View")
    # If the user is None, then the user is not authentificated (should not happen)
    if user is None:
      username = None
    else :
      username = user.username

    
    # print("Of : " + username)
    # Display the view for the first time
    await self.renderView()

    # While the user doesn't click, wait for a joystick action
    while joystickAction != "CLICK":
      joystickAction = getJoystickAction()
      await self.updateIndex(joystickAction)
    # If the user clicks, then go back to the main menu


  # updateIndex : update the index of the view
  # Input : JoystickAction
  # Return : None
  async def updateIndex(self, joystickAction):
    # Set the global variables
    global currentIndex

    if joystickAction == "UP":
      # print("UP")
      # If the index is not 0, then decrement it
      if self.currentIndex > 0:
        self.currentIndex -= 1
      # Render the view  
      await self.renderView()

    # If the joystick action is down
    elif joystickAction == "DOWN":
      # print("DOWN")
      # If the index is not 4, then increment it (max = 4)
      if self.currentIndex < 4:
        self.currentIndex += 1
      # Render the view  
      await self.renderView()
  

  # renderView : render the view with the current index
  # scrolls the text if needed
  # Input : None (but uses the global variables)
  # Displays
  async def renderView(self):
    # Set the global variables
    # Assign the user
    global currentUser
    user = currentUser
    # Get the total orders of the user
    total_orders = await Order.filter(user=user).count()
    # Get the orders of the day
    today = datetime.now().strftime("%Y-%m-%d")
    today_orders = await Order.filter(user=user, created_at__contains=today).count()
    # Get the username of the user
    username = user.username

    # Create the lines to display in the list lines[]
    lines = []
    lines.append("Nom :")
    lines.append(username)
    lines.append("Commandes auj. :")
    lines.append(str(today_orders))
    lines.append("Commandes tot. :")
    lines.append(str(total_orders))

    # Create the text to display with the current index
    textToDisplay = ""
    textToDisplay += lines[self.currentIndex]
    textToDisplay += "\n"
    textToDisplay += lines[self.currentIndex + 1]

    # Dsplays the text
    setText(textToDisplay)  
