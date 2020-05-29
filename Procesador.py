from cache import *
from Controller import *
import threading

class Procesador:

    def __init__(self, name, chip, controller):
        self.cacheL1 = Cache(2,[],1)
        self.controller = controller
        self.bus_instrucc = []
        self.name = name
        self.direcList = []
        self.chip = chip
        self.read = threading.Thread(target = self.readInstruccion, args=())
        self.read.start()


    def newInstruccion(self,intr):
        self.bus_instrucc.append(intr)

    def readInstruccion(self):
        while(1):
            for instr in self.bus_instrucc:
                proc = instr[0:2]
                chip = instr[3]
                op = instr[5:10]
                self.bus_instrucc = self.bus_instrucc[1:]
                if(proc == self.name):
                    if(chip == self.chip):
                        print(op[0] == "R")
                        if(op[0] == "R"):
                            print("Entra a read")
                            print(self.cacheL1.readMem(instr[10:14]))
                            if(self.cacheL1.readMem(instr[10:14]) == "Error"):
                                print(self.controller.getEx())
                                while(self.controller.getEx() == 1):
                                    print("El procesador " + proc + " Esta Esperando")

                                self.controller.setEx(1)
                                data = self.controller.readMemL2(instr[10:14])
                                self.controller.setEx(0)
                                print ("el dato de "+ proc + "es " + data)
                                return data
                        elif(op == "CALC"):
                            print("Calculando")
                        else:
                            print("Entra a write")
                            print(self.cacheL1.writeMem(instr[16:20],instr[11:15]))
                    else:
                        if(op[0] == "R"):
                            if(self.incache(instr[10:14])):
                                self.cacheL1.changeState()



        def incache(self,direc):
            
            
                        
            
            
        
            
