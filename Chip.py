from Controller import *
from Procesador import *

class Chip:

    def __init__(self,name):
        self.name = name
        self.initProcs()
        self.controller = Controller()
        self.procesador0 = None
        self.procesador1 = None

    def initProcs(self):
        self.procesador0 = Procesador("P0",name,self.controller)
        self.procesador1 = Procesador("P1", name, self.controller)

    def updateBus(busInst):
        for x in busInst:
            self.procesador0.newInstruccion(x)
            self.procesador1.newInstruccion(x)

    
