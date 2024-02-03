from drivers.LCD import setText, setRGB

class ShutdownAction():

  def shutdownMachine(self):
    setText("")
    setRGB(0,0,0)
    exit(1)