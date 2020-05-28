from cache import *

class Controller:
    def __init__(self):
        self.cacheL2 = Cache(4,[],2)
        self.execution = 0
        


    def getEx(self):
        return self.execution

    def readMemL2(self,direc):
        print("Entra en controlador de L2 para leer: " + direc)
        data = self.cacheL2.readMem(direc)
        return data

    def writeMemL2(self, data, direc):
        self.cacheL2.writeMem(data,direc)


    def setEx(self,val):
        self.execution = val