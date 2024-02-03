from multiprocessing import Process
import time
from drivers.Ultrasonic import getDistance
from drivers.Pump import switchOnPump, switchOffPump, pumpDebit
from database.recipe import Recipe
from tortoise.queryset import Q

class ServeDrinkAction():

  # Run a subprocess to serve a drink and check if there is glass during service
  async def serveDrink(self, recipeId, size):
    recipe = await Recipe.get(Q(id=recipeId))
    serveProcess = Process(target=self.physicallyServe, args=(recipe,size,))
    serveProcess.start()

    serveSuccessfully = True
    # Check if there is glass during service
    while serveProcess.is_alive() and serveSuccessfully:
      if not self.checkGlass():
        serveProcess.kill() # Stop service if no glass
        switchOffPump(1) # Reset pump
        switchOffPump(2)
        serveSuccessfully = False
      time.sleep(0.1)
  
    return serveSuccessfully



  # Check if there is glass on the scale
  def checkGlass(self):
    distance1 = getDistance()
    time.sleep(0.05)
    distance2 = getDistance()
    time.sleep(0.05)
    distance3 = getDistance()
    time.sleep(0.05)
    distance4 = getDistance()

    return min(distance1, distance2, distance3, distance4) < 10  #+- 10 cm 
        

        
  # Subprocess function
  def physicallyServe(self, recipe, size):
    rateBottleOne = recipe.rate_bottle_one
    rateBottleTwo = recipe.rate_bottle_two
    
    # Time = quantity / debit
    switchOnDurationBottleOne = (rateBottleOne * size) / pumpDebit
    switchOnDurationBottleTwo = (rateBottleTwo * size) / pumpDebit

    switchOnPump(1)
    switchOnPump(2)

    time.sleep(min(switchOnDurationBottleOne, switchOnDurationBottleTwo))

    if switchOnDurationBottleOne < switchOnDurationBottleTwo:
      switchOffPump(1)
      time.sleep(switchOnDurationBottleTwo - switchOnDurationBottleOne)
      switchOffPump(2)
    else:
      switchOffPump(2)
      time.sleep(switchOnDurationBottleOne - switchOnDurationBottleTwo)
      switchOffPump(1)