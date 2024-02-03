from actions.ServeDrinkAction import ServeDrinkAction
from components.SelectionMenu import SelectionMenu
from drivers.LCD import setText
from database.recipe import Recipe
from database.order import Order
from config import ServeQuantity
import time

class ServeDrinkView():

  currentUser = None

  def __init__(self, user):
    self.actions = ServeDrinkAction()
    self.currentUser = user



  # Ask user to choose a recipe and a size then serve the drink
  # Return true if service succeed
  async def startServeDrinkPipeline(self):

    # Wait for a glass to be put on the scale and write message
    self.waitForGlass()

    recipe = await self.chooseRecipe()
    quantityMl = self.chooseQuantity()

    # Serve the drink
    setText("Service en cours\n...")
    serveResult = await self.actions.serveDrink(recipeId=recipe.id, size=quantityMl)
    if serveResult:
      setText("Service termine")
      await Order.create(quantity=quantityMl, user=self.currentUser, recipe=recipe)
      time.sleep(3)
      return True
    else:
      setText("Erreur durant\nle service")
      time.sleep(3)
      return False 
   


  # Ask a recipe and return the id of the recipe
  async def chooseRecipe(self):
    recipes = await Recipe.all()
    index = SelectionMenu(title="Choix recette:", menu=[drink.name for drink in recipes]).handleMenuSelection()
    return recipes[index]
  


  # Ask a recipe and return the quantity (in ml)
  def chooseQuantity(self):
    selectedIndex = SelectionMenu(title="Choix boisson:", menu=[member.label for member in ServeQuantity]).handleMenuSelection()
    return list(ServeQuantity)[selectedIndex].value[0]



  # Wait for a glass to be put on the scale
  # and print a message while waiting
  def waitForGlass(self):
    firstIter = True
    while not self.actions.checkGlass():
      if firstIter:
        setText("Veuillez poser\nun verre ...")
        firstIter = False
      time.sleep(1)