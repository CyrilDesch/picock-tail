from drivers.LCD import setText
from drivers.Joystick import getJoystickAction
from drivers.NFC import read_card
from database.user import User
from tortoise.queryset import Q
from components.VirtualKeyboard import VirtualKeyboard
import time


class AuthentificationView():

  def __init__(self):
    self.renderView()


  def renderView(self):
    setText("Presentez votre carte\n click pour annuler")
  
  # handleAuth : setText instructions to auth
  # If user is not known : register the user 
  # Return true if the user is authentificated
  # Return false if user cancelled
  async def handleAuthentification(self):

    joystickAction = ""
    uid = False, None

    while (joystickAction == "CLICK" or uid[0])!= True: #If the user clicks or the uid is known then stop
      joystickAction = getJoystickAction()
      uid = self.cardAuthentification()
  
    
    if uid[0] == True: # If the user didn't cancel
      #print("Card detected (in handleAuthentification)")
      #print (uid[1])
      user = await self.getUserWithUID(uid[1])

      #Register new user
      if user is None:
        #Instructions for the user
        setText("Enregistrement\n de la carte")
        time.sleep(1)
        setText("Entrez votre\n nom")
        time.sleep(1)

        #Get the username from the virtual keyboard (View)
        newUserUsername = VirtualKeyboard().getInput()

        #print("Enregistrement de " + newUserUsername)
        # Create the user in the database
        await User.create(username=newUserUsername, cardUID=uid[1])

        #Get the user from the database
        user = await self.getUserWithUID(uid[1])
        #Greet the user
        setText("Bienvenue \n " + user.username)
        time.sleep(2)
        #Return the user
        return True, user

      #User is known
      #print("User : ", user.username)
      return True , user
    
    #User cancelled
    #print("Return to home")
    return False, None

  # cartAuthentification : void -> bool, hex (like 0x7 ...) check if a card is detected
  def cardAuthentification (self):
    uid = read_card()
    if uid is None:
      #print("No card detected")
      return False, None
    else:
      #print("Card detected (in cardAuthentification)")
      return True, [hex(i) for i in uid]


  # getUserWithUID : hex -> User
  # Return the user with the given UID or None if no user is found
  async def getUserWithUID(self, UID):
    try :
      user = await User.get(Q(cardUID=UID)) #Checks if the user exists
    except Exception as e:
      return None #If the user doesn't exist
    return user #If the user exists
