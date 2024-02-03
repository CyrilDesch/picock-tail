import time
from drivers.LCD import setText, setErrorRGB

class ErrorView():

  def __init__(self, errorMessage):
    self.errorMessage = errorMessage



  def show(self):
    setText(self.errorMessage)
    setErrorRGB()
    time.sleep(5)