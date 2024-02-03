from config import MenuState
from components.SelectionMenu import SelectionMenu

class HomeView():

  # Handle the menu selection and return the selected state
  def handleMenuSelection(self):
    index = SelectionMenu(title="Menu :", menu=[member.label for member in MenuState]).handleMenuSelection()
    return list(MenuState)[index].state
