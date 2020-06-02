from cacheL2 import *
from Memoria import *
import time
import random

#CAmbiar todoooooooooooo
class Controller:
    def __init__(self, memoria, chip):
        self.cacheL2 = CacheL2()
        self.execution = 0
        self.chip = chip
        self.memoria = memoria
        
        


    def getEx(self):
        return self.execution

    def readMemL2(self,direc,proc):
        print("Entra en controlador de L2 para leer: " + direc)
        print("+++++++++++++++++++++++++++++++++")
        self.cacheL2.print()
        data = self.cacheL2.readMem(direc,proc)
        if (data == "Error"):
            data = self.memoria.read(direc,self.chip)
            self.cacheL2.write(data[0],data[3],proc)
            print("Entra a Error")
            return data
        else:
            for x in range(4):
                ##print(x)
                if (self.cacheL2.memoria[x][0]==direc):
                    #print("______")
                    if(proc not in self.cacheL2.memoria[x][2]):
                        self.cacheL2.memoria[x][2] += proc
                        self.cacheL2.memoria[x][1] = "DS"
        print(self.cacheL2.memoria[x])
        print(data)
        return data
        

    def writeMemL2(self, data, direc,proc):
        data = self.cacheL2.write(direc,data,proc)
        #print(data)
        return data
    
    def writeInMemL2(self,data,direc,proc):
        data = self.cacheL2.writeinMem(direc,data,proc)
        print(data)
        return data

    def eraseMem(self,direc,proc):
        for x in range(4):
            if(self.cacheL2.memoria[x][0] == direc):
                largo = len(self.cacheL2.memoria[x][2])
                if(largo == 2):
                    for y in range(largo):
                        if(self.cacheL2.memoria[x][2][y] == proc):
                            #print(self.cacheL2.memoria[x][2][0:y] + self.cacheL2.memoria[x][2][y+1:largo])
                            self.cacheL2.memoria[x][2] = self.cacheL2.memoria[x][2][0:y] + self.cacheL2.memoria[x][2][y+1:largo]
                            return
                elif(largo==1 and self.cacheL2.memoria[x][1]=="DM"):
                    self.memoria.write(direc,self.cacheL2.memoria[x][3],self.chip)
                    self.cacheL2.memoria[x] = ["","",[],"0"]
                    time.sleep(4)
                else:
                    self.cacheL2.memoria[x] = ["","",[],"0"]
                return
        


    def setEx(self,val):
        self.execution = val

    def getCacheL2FreeMemory(self):
        return self.cacheL2.getFreeMemory()

    def getLastTime(self):
        return self.cacheL2.getLastTime()

    def getLastOne(self):
        return self.cacheL2.getLastOne()

    def changeState(self,direc,newState):
        self.cacheL2.changeState(newState,direc)
