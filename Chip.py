from Controller import *
from Procesador import *

class Chip:

    def __init__(self,name,memoria):
        self.name = name
        self.memoria = memoria
        self.controller = Controller(self.memoria,self.name)
        self.controller.cacheL2.print()
        self.procesador0 = None
        self.procesador1 = None
        self.initProcs()

    def initProcs(self):
        self.procesador0 = Procesador("P0",self.name,self.controller)
        self.procesador1 = Procesador("P1", self.name, self.controller)

    def updateBus(self,busInst):
        for x in busInst:
            self.procesador0.newInstruccion(x)
            self.procesador1.newInstruccion(x)

    
