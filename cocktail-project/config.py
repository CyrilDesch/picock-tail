from enum import Enum

DB_USER = 'pycock_tail'
DB_PASSWORD = 'pycock_tail'
DB_NAME = 'pycock_tail'
DB_HOST = 'cyrildeschamps.fr'
DB_PORT = 3306



class State(Enum):
  HOME = 0
  AUTHENTIFICATION = 1  # Payload : {nextState}
  ACCOUNT_DETAILS = 4  
  SERVE_DRINK = 5
  ERROR = 6
  SHUTDOWN = 7



# Enum of the differents states of the machine accessible with in the menu
# - Label must have a length of 12 characters max
# - Maximum of 9 states
class MenuState(Enum):
  SERVE_DRINK = (State.SERVE_DRINK, "Se servir")
  ACCOUNT_DETAILS = (State.ACCOUNT_DETAILS, "Mon compte")
  SHUTDOWN = (State.SHUTDOWN, "Eteindre")

  def __init__(self, state, label):
    self.state = state
    self.label = label


# Enum of the quantity of the drink
# - First value is the quantity in ml
# - Second value is the label to display (max 12 char)
class ServeQuantity(Enum):
  SMALL = (50, "5cl")
  LARGE = (200, "20cl")

  def __init__(self, quantity, label):
    self.quantity = quantity
    self.label = label