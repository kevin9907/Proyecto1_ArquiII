from Memoria import *
class CacheL2(memoria):

    def __init__(self):
        memoria.__init__(self)
        self.__initMemory()
        self.__freeMemory = 4

    def __initMemory(self):
        self.memoria = []
        self.memoria += [["","",[],"0"]]
        self.memoria += [["","",[],"0"]]
        self.memoria += [["","",[],"0"]]
        self.memoria += [["","",[],"0"]]

    def writeMem(self, info, direccion,proc):
        #print(self.getFreeMemory())
        for x in range(4):
            if self.memoria[x][0] == "0":
                self.memoria[x][3] = info
                self.memoria[x][0] = direccion
                self.memoria[x][1] = "DM"
                self.__freeMemory -= 1
                if(chip in self.memoria[x][2]):
                    print()
                else:
                    self.memoria[x][2] += [proc]
                time.sleep(2)
                return "Escrito"
            elif(self.memoria[x][0] == direccion):
                self.memoria[x][3] = info
                self.memoria[x][1] = "DM"
                if(proc in self.memoria[x][2]):
                    print()
                else:
                    self.memoria[x][2] += [proc]
                time.sleep(2)
                return "SobreEscrito"

    def getFreeMemory(self):
        return self.__freeMemory


    def readMem(self, direccion, proc):
        for x in range(4):
            print("Leyendo de L2: "+ direccion)
            print(self.memoria[x][0])
            if(self.memoria[x][0]==direccion):
                largo = len(self.memoria[x][2])
                if(largo==1 and (proc not in self.memoria[x][2])):
                    print("Cambia estado")
                    self.memoria[x][1] = "DS"
                    self.memoria[x][2] += [proc]
                elif(proc in self.memoria[x][2]):
                    print("No hacer nada")
                return self.memoria[x]
                
        return "Error"

    def writeinMem(self,direc,data,chip):
        #print("Entra")
        for x in range(4):
            if (direc == self.memoria[x][0]):
                self.memoria[x][3] = data
                self.memoria[x][1] = "DM"
                self.memoria[x][2] = [chip]
                return self.memoria[x][2]

    def write(self,direct,data,chip):
        for x in range(4):
            if(self.memoria[x][0]==""):
                self.memoria[x][3] = data
                self.memoria[x][2] = [chip]
                self.memoria[x][1] = "DM"
                print(self.memoria[x][2])
                self.memoria[x][0] = direct
                break

    def changeState(self,state,direc):
        for x in range(4):
            if (self.memoria[x][0] == direc):
                self.memoria[x][1] = state
            
    
