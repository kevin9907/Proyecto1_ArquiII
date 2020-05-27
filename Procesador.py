from cache import *

class Procesador:

    def __init__(self, name, chip):
        self.memoria = []
        self.cacheL1 = Cache(2,self.memoria,1)
        self.bus_instrucc = []
        self.name = name
        self.chip = chip
        self.readInstruccion()


    def newInstruccion(self,intr):
        self.bus_instrucc.append(intr)

    def readInstruccion(self):
        for instr in self.bus_instrucc:
            proc = instr[0:2]
            chip = instr[3]
            op = instr[5:10]
            if(proc == self.name):
                if(chip == self.chip):
                    print(op[0] == "R")
                    if(op[0] == "R"):
                        print("Entra a read")
                        print(self.cacheL1.readMem(instr[10:14]))
                        #if == Error buscar en L2
                    elif(op == "CALC"):
                        print("Calculando")
                    else:
                        print("Entra a write")
                        print(self.cacheL1.writeMem(instr[16:20],instr[11:15]))
                        
            
            
            
            
            
