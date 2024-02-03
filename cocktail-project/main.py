from config import State
from database import connection
from tortoise import run_async
from drivers import Joystick, LCD, Ultrasonic, Pump
from views.HomeView import HomeView
from views.AuthentificationView import AuthentificationView
from views.AccountDetailsView import AccountDetailsView
from views.ServeDrinkView import ServeDrinkView
from views.ShutdownView import ShutdownView
from views.ErrorView import ErrorView
import signal


# Global variable containing authenticated current tortoise object user
# Note : Set during "State.AUTHENTIFICATION"
user = None



# Main class of the Cocktail Machine
class CocktailMachine():

  def __init__(self):
    self.state = None
    self.payload = None



  # At the start of the machine : 
  # - Init database remote connection
  # - Init state at Home
  async def start(self):
    await connection.initDatabase()
    Joystick.setJoystickPort(0, 1) # Port A0
    Ultrasonic.setUltrasonicPort(3) # Port D3
    Pump.setPumpPort(7,8, None)  # Set the pump port to D7, D8
    LCD.setRGB(255, 255, 255)
    await self.setState(State.HOME)



  # Change state of the machine
  # Args: 
  # - state: State -> the new State
  # - payload: Dict -> datas that we want pass to the next state / Check on config.py for more informations
  async def setState(self, state: State, payload={}):
    self.state = state
    self.payload = payload
    await self.renderView()



  # Render view of the machine based on current state
  # Started auto-managed class and then update to the next state
  # Note : an auto-managed class can call render another view inside it
  async def renderView(self):
    global user
    match self.state:
      case State.HOME:
        selectedState = HomeView().handleMenuSelection()
        await self.setState(selectedState)


      case State.AUTHENTIFICATION:
        success = await AuthentificationView().handleAuthentification()
        #If the user didn't cancel, then go to the nextState(AccountView or ServeDrink)
        if success[0] == True:
          nextState = self.payload["nextState"]
          user = success[1]
        #If the user canceled go back to home
        else :
          nextState = State.HOME

        await self.setState(nextState)


      case State.SERVE_DRINK:
        # Auth
        if user is None:
          await self.setState(State.AUTHENTIFICATION, {"nextState": State.SERVE_DRINK})
          return
        
        await ServeDrinkView(user).startServeDrinkPipeline()
        user = None
        await self.setState(State.HOME)


      case State.ACCOUNT_DETAILS:
        # Auth
        if user is None:
          await self.setState(State.AUTHENTIFICATION, {"nextState": State.ACCOUNT_DETAILS})
          return
        
        await AccountDetailsView().handleDetailsView(user)
        user = None
        await self.setState(State.HOME)


      case State.SHUTDOWN:
        ShutdownView().show()


      case _:
        errorMessage = "Erreur, etat inconnu"
        if "message" in self.payload:
          errorMessage = self.payload["message"]
        ErrorView(errorMessage).show()
        await self.setState(State.HOME)



def exitSensor():
  print('- Extinction des pompes et ecran ...')
  Pump.switchOffPumps()
  LCD.setText("")
  LCD.setRGB(0, 0, 0)

if __name__ == "__main__":
  cocktailMachine = CocktailMachine()
  try:
    run_async(cocktailMachine.start())
  except Exception as e:
    print('CRASH : ')
    print(e)
    exitSensor()

signal.signal(signal.SIGINT, exitSensor)