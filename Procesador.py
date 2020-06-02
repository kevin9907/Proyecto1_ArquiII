from cache import *
from Controller import *
import time
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
                print(instr)
                proc = instr[0:2]
                chip = instr[3]
                op = instr[5:10]
                self.bus_instrucc = self.bus_instrucc[1:]
                if(chip == self.chip):
                    if(proc == self.name):
                        if(op[0] == "R"):
                            #print("Entra a read el proc: " + proc)
                            if(self.cacheL1.readMem(instr[10:14]) == "Error"):
                                while(self.controller.getEx() == 1):
                                    y=1#print("El procesador " + proc + " Esta Esperando")
                                self.controller.setEx(1)
                                data = self.controller.readMemL2(instr[10:14],self.name)
                                #print("El dato es: ")
                                #print(data)
                                write = self.cacheL1.writeMem(data[3],data[0])
                                #print(write)
                                #print(type(write)==list)
                                if(type(write)==list):
                                    #print("Se eliminará el data: "+ write[0]+ "En L2")
                                    self.borrardeCache(write[0])
                                    self.controller.eraseMem(write[0],self.name)
                                    #print(self.direcList)
                                    #print("La direccion esta en L2?")
                                    #print(self.incache(instr[10:14])==0)
                                    #print(self.incache(instr[10:14]))
                                    if(self.incache(instr[10:14])==0):
                                        #print("In cache = false")
                                        self.direcList.append(instr[10:14])
                                        self.controller.writeMemL2(data[3],instr[10:14],self.name)
                                    else:
                                        r=1
                                
                                #self.controller.cacheL2.print()
                                #self.cacheL1.print()
                                self.cacheL1.changeState(data[0],"S")
                                self.controller.setEx(0)
                                #print ("el dato de "+ proc + "es " + data[3])
                                #print("Terminado el READ")
                            self.imprimir()
                        elif(op == "CALC"):
                            print("Calculando")
                        else:
                            #print("Entra a write el proc: " + proc)
                            #print(self.controller.getEx() == 1)
                            while(self.controller.getEx() == 1):
                                    y=1#print("El procesador " + self.name + " Esta Esperando")
                            
                            self.controller.setEx(1)
                            #print(instr[11:15])
                            if(self.incache(instr[11:15])):
                                self.controller.writeInMemL2(instr[16:20],instr[11:15],self.name)
                                write = self.cacheL1.writeMem(instr[16:20],instr[11:15])
                                if(type(write)==list):
                                  #  print("Se eliminará el data: "+ write[0]+ "En L2")
                                    self.borrardeCache(write[0])
                                    self.controller.eraseMem(write[0],self.name)
                                    self.controller.setEx(0)
                                else:
                                    self.direcList.append(instr[11:15])
                                    self.controller.setEx(0)
                            else:
                                write = self.cacheL1.writeMem(instr[16:20],instr[11:15])
                                #print("Aqui es donde se despicha****")
                                #print(write)
                                if(type(write)==list):
                                 #   print("Se eliminará el data: "+ write[0]+ "En L2")
                                    self.borrardeCache(write[0])
                                    self.controller.eraseMem(write[0],self.name)
                                    self.controller.writeMemL2(instr[16:20],instr[11:15],self.name)
                                    self.controller.setEx(0)
                                else:
                                  #  print("No, es aqui")
                                    self.controller.writeMemL2(instr[16:20],instr[11:15],self.name)
                                    self.controller.setEx(0)
                                #print("Lista de direcciones")
                                self.direcList.append(instr[11:15])
                                #print(self.direcList)
                            #self.controller.cacheL2.print()
                            self.imprimir()
                        while(self.controller.getEx() == 1):
                            y=1#print("El procesador " + self.name + " Esta Esperando")      
                    else:
                        #print("Entra al else el proc: " + self.name+ "Con la direc: " + instr[10:14])
                        time.sleep(1)
                        while(self.controller.getEx() == 1):
                            y=1#print("El procesador " + self.name + " Esta Esperando")
                        self.controller.setEx(1)
                        if(op[0] == "R"):
                         #   print("Si entra")
                          #  print(self.direcList)
                            inCache = self.incache(instr[10:14])
                            #print(instr[10:14])
                            #print(inCache)
                            if(inCache==0):
                                self.direcList.append(instr[10:14])
                           #     print("Pasa")
                            elif(inCache == 1):
                            #    print("Cambiar estado de: " +instr[10:14] + " en L1")
                                self.cacheL1.changeState(instr[10:14],"S")
                            elif(chip != self.chip):
                             #   print("Entra a chip diferente")
                                self.controller.changeState(instr[10:14],"S")
                              #  print("Cambiar estado de: " +instr[10:14] + " en L2")
                        elif(op == "CALC"):
                            y = 1
                        else:
                            if(self.cacheL1.readMem(instr[11:15])!= "Error"):
                                self.cacheL1.changeState(instr[11:15],"I")
                            self.direcList.append(instr[11:15])
                        self.controller.setEx(0)
                                
                                
    def manageData(self,data):
        #print("Entra a manage data")
        if(len(data[2])==2):
         #   print(data[2])
            self.cacheL1.changeState(data[0],"S")



    def incache(self,direc):
        #print(direc)
        for x in self.direcList:
         #   print(x)
            if x == direc:
                return 1
        return 0

    def borrardeCache(self,direc):
        largo = len(self.direcList)
        #print(self.direcList)
        y = 0;
        for x in range(largo):
            if(self.direcList[x] == direc):
                self.direcList = self.direcList[0:x] + self.direcList[x+1:largo]
                break
    def imprimir(self):
        print("Impresion de: " + self.name + " del chip: " + self.chip)
        self.cacheL1.print()
        self.controller.cacheL2.print()
        self.controller.memoria.print()
            
##def main():
##    c = Controller(memoria(),"C0")
##    x = Procesador("P0","0",c)
##    y = Procesador("P1","0",c)
##    #print("*************************************")
##    #x.newInstruccion("P0,0:READ 1100")
##    #print("**************************************")
##    x.controller.cacheL2.print()
##    #print("---------------------------------------")
##    x.newInstruccion("P0,0:READ 1010")
##    y.newInstruccion("P0,0:READ 1010")
##    #print(x.bus_instrucc)
##    #print("-------------------------------------")
##    x.controller.cacheL2.print()
##    y.newInstruccion("P1,0:WRITE 1111,abcd")
##    x.newInstruccion("P1,0:WRITE 1111,abcd")
##    y.newInstruccion("P1,0:WRITE 1001,abcd")
##    x.newInstruccion("P1,0:WRITE 1001,abcd")
##    x.newInstruccion("P0,0:READ 1001")
##    x.newInstruccion("P0,0:READ 1111")
##    y.newInstruccion("P0,0:READ 1001")
##    y.newInstruccion("P0,0:READ 1111")
##    y.newInstruccion("P1,0:WRITE 1111,abcd")
##    x.newInstruccion("P1,0:WRITE 1111,abcd")
##    y.newInstruccion("P0,0:WRITE 1010,abcd")
##    x.newInstruccion("P0,0:WRITE 1010,abcd")
##    y.newInstruccion("P0,0:WRITE 0101,abcd")
##    x.newInstruccion("P0,0:WRITE 0101,abcd")
##    y.newInstruccion("P1,0:READ 0101,abcd")
##    x.newInstruccion("P1,0:READ 0101,abcd")
##    
##    #y.newInstruccion("P1,0:READ 0001,abcd")
##    #y.newInstruccion("P1,0:READ 0011,abcd")
##    time.sleep(30)
##    x.controller.cacheL2.print()
##    x.controller.memoria.print()
##    x.controller.cacheL2.print()
##    x.controller.memoria.print()
##    x.cacheL1.print()
##    y.cacheL1.print()
