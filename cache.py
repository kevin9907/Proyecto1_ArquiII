import time
class Cache():

    def __init__(self,cantidad, memoria, tiempo):
        self.cantidad = cantidad
        self.memoria = memoria
        self.iniciarMemoria()
        self.lastTime = 1
        self.freeMemory = cantidad
        self.tiempo = tiempo

    def iniciarMemoria(self):
        for x in range(self.cantidad):
            self.memoria.append([0,0,"0"]);

    def readMem(self, direccion):
        for x in range(self.cantidad):
            if(self.memoria[x][2]==direccion):
                time.sleep(self.tiempo*2)
                self.memoria[x][1] = self.lastTime
                self.lastTime += 1
                return self.memoria[x][0]
        return "Error"
            

    def __writeLastMem(self):
        res = 0
        last = self.memoria[0][1];
        for x in range(self.cantidad):
            if self.memoria[x][1] < last:
                res = x
                last = self.memoria[x][1]
        return res

    def writeMem(self, info, direccion):
        for x in range(self.cantidad):
            if self.memoria[x][2] == "0":
                self.memoria[x][0] = info
                self.memoria[x][1] = self.lastTime
                self.memoria[x][2] = direccion
                self.freeMemory -= 1
                self.lastTime += 1
                time.sleep(self.tiempo)
                return x;
            elif(self.memoria[x][2] == direccion):
                self.memoria[x][0] = info
                self.memoria[x][1] = self.lastTime
                self.memoria[x][2] = direccion
                self.freeMemory -= 1
                self.lastTime += 1
                time.sleep(self.tiempo)
                return x
##            elif (self.memoria[x][2] != 0 and x == (self.cantidad-1)):
##                direc = self.__writeLastMem()
##                self.memoria[direc][0] = info
##                self.memoria[direc][1] = self.lastTime
##                self.memoria[direc][2] = direccion
##                self.lastTime += 1
##                time.sleep(self.tiempo)
##                return direccion

#Reescribe en una memoria que ya está ocupada, la que no se haya usado con mayor antiguedad
    def rewrite(self, direccion, info):
        direc = self.__writeLastMem()
        deleteInfo = self.readMem(direc)
        self.memoria[direc][0] = info
        self.memoria[direc][1] = self.lastTime
        self.memoria[direc][2] = direccion
        self.lastTime += 1
        time.sleep(self.tiempo)
        writeBackInfo = [direc,deleteInfo]
        return deleteInfo

    def getState(self):
        return self.state
