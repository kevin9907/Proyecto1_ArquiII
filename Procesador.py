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
                        elif(op == "CALC"):
                            print("Calculando")
                        else:
                            print("Entra a write")
                            if(self.cacheL1.getFreeMemory() == 0):
                                print("L1 no tiene espacio")
                                if(self.controller.getCacheL2FreeMemory()==0):
                                    print("L2 no tiene espacio")
                                    if(self.controller.getLastOne() > self.cacheL1.getLastOne()):
                                        print("Escribe en L1")
                                        write = self.cacheL1.writeMem(instr[16:20],instr[11:15])
                                        self.borrardeCache(write[0])
                                        self.direcList.append([instr[11:15],"L1"])
                                    else:
                                        print("Escribe en L2")
                                        write = self.controller.writeMemL2(instr[16:20], instr[11:15])
                                        self.borrardeCache(write[0])
                                        self.direcList.append([instr[11:15],"L2"])
                                else:
                                    print("L2 tiene espacio")
                                    self.controller.writeMemL2(instr[16:20], instr[11:15])
                                    self.direcList.append([instr[11:15],"L2"])
                            else:
                                print("L1 tiene espacio")
                                write = self.cacheL1.writeMem(instr[16:20],instr[11:15])
                                self.direcList.append([instr[11:15],"L1"])
                            
                    else:
                        if(op[0] == "R"):
                            inCache = self.incache(instr[10:14]) != 0
                            if(inCache==0):
                                print("Pasa")
                            elif(inCache == "L1"):
                                print("Cambiar estado de: " +instr[10:14] + " en L1")
                                self.cacheL1.changeState(instr[10:14],"S")
                            elif(chip != self.chip):
                                self.controller.changeState(instr[10:14],"S")
                                print("Cambiar estado de: " +instr[10:14] + " en L2")
                                
                                
                                



    def incache(self,direc):
        for x in self.direcList:
            if x[0] == direc:
                return x[1]
        return 0

    def borrardeCache(self,direc):
        direcciones = self.direcList
        y = 0;
        for x in direcciones:
            if(x == direc):
                self.direcList = self.directList[0:y] + direcList[y+1:len(self.direcList)]
                break
            else:
                y += 1
            
                    
            
            
                        
            
            
        
            
