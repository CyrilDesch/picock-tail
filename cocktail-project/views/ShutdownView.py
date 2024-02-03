from actions.ShutdownAction import ShutdownAction
from drivers.LCD import setText, setRGB
import colorsys


def hsv_to_rgb(h, s, v):
  return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))



class ShutdownView():

  def __init__(self):
    self.actions = ShutdownAction()



  def show(self):
    countDown = 3
    while countDown > 0:
      setText(f"Extinction dans\n   {countDown}")
  
      # Générer et afficher 1000 couleurs différentes
      for i in range(750):
          h = i / 1000  # teinte variant de 0 à 1
          r, g, b = hsv_to_rgb(h, 1, 1)  # saturation et valeur maximales pour des couleurs vives
          setRGB(r, g, b)

      countDown -= 1

    self.actions.shutdownMachine()