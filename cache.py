import time
from prettytable import PrettyTable

class Cache():

    def __init__(self,cantidad, memoria, tiempo):
        self.cantidad = cantidad
        self.memoria = memoria
        self.iniciarMemoria()
        self.lastTime = 1
        self.__freeMemory = cantidad
        self.tiempo = tiempo

    def iniciarMemoria(self):
        for x in range(self.cantidad):
            self.memoria.append([0,0,"0",""]);

    def readMem(self, direccion):
        for x in range(self.cantidad):
            if(self.memoria[x][2]==direccion):
                time.sleep(self.tiempo)
                self.memoria[x][1] = self.lastTime
                self.lastTime += 1
                return self.memoria[x]
        return "Error"
            

    def __writeLastMem(self):
        
        res = [self.memoria[0][2],0]
        last = self.memoria[0][1];
        for x in range(self.cantidad):
            if self.memoria[x][1] < last:
                res = [self.memoria[x][2],x]
                last = self.memoria[x][1]
        #print(res)
        return res

    def writeMem(self, info, direccion):
        #print(self.getFreeMemory())
        for x in range(self.cantidad):
            if self.memoria[x][2] == "0":
                self.memoria[x][0] = info
                self.memoria[x][1] = self.lastTime
                self.memoria[x][2] = direccion
                self.memoria[x][3] = "M"
                self.__freeMemory -= 1
                self.lastTime += 1
                time.sleep(self.tiempo)
                return "Escrito"
            elif(self.memoria[x][2] == direccion):
                self.memoria[x][0] = info
                self.memoria[x][1] = self.lastTime
                self.memoria[x][2] = direccion
                self.lastTime += 1
                self.memoria[x][3] = "M"
                time.sleep(self.tiempo)
                return "SobreEscrito"
            elif(self.getFreeMemory()  == 0 and x == self.cantidad-1):
                return self.rewrite(direccion,info)

#Reescribe en una memoria que ya está ocupada, la que no se haya usado con mayor antiguedad
    def rewrite(self, direccion, info):
        #print("Entra en rewrite")
        [lastdirec,direc] = self.__writeLastMem()
        deleteInfo = self.readMem(lastdirec)
        if(self.memoria[direc][3]=="M" or self.memoria[direc][3]=="S"):
            self.memoria[direc][0] = info
            self.memoria[direc][1] = self.lastTime
            self.memoria[direc][2] = direccion
            self.memoria[direc][3] = "M"
            self.lastTime += 1
            time.sleep(self.tiempo)
            writeBackInfo = [lastdirec,deleteInfo]
            return writeBackInfo
        else:
            self.memoria[direc][0] = info
            self.memoria[direc][1] = self.lastTime
            self.memoria[direc][2] = direccion
            self.memoria[direc][3] = "M"
            self.lastTime += 1
            time.sleep(self.tiempo)
            writeBackInfo = [lastdirec,deleteInfo]

    def getFreeMemory(self):
        return self.__freeMemory

    def getLastTime(self):
        return self.lastTime

    def getLastOne(self):
        res = self.memoria[0][2]
        last = self.memoria[0][1];
        for x in range(self.cantidad):
            if self.memoria[x][1] < last:
                res = self.memoria[x][2]
                last = self.memoria[x][1]
        #print(res)
        return res


    def changeState(self,direc,newState):
        for x in range(self.cantidad):
            if(self.memoria[x][2]==direc):
                #print("cambia")
                #print("newState")
                self.memoria[x][3] = newState

    def print(self):
        t = PrettyTable(["Estado","Dato","Direccion"])
        for x in self.memoria:
            t.add_row([x[3],x[0],x[2]])
        print(t)
                
        
