from prettytable import PrettyTable

class memoria:
    def __init__(self):
        self.memoria = []
        self.__initMemory()


    def __initMemory(self):
        self.memoria += [["0000","",[],"0"]]
        self.memoria += [["0001","",[],"0"]]
        self.memoria += [["0010","",[],"0"]]
        self.memoria += [["0011","",[],"0"]]
        self.memoria += [["0100","",[],"0"]]
        self.memoria += [["0101","",[],"0"]]
        self.memoria += [["0110","",[],"0"]]
        self.memoria += [["0111","",[],"0"]]
        self.memoria += [["1000","",[],"0"]]
        self.memoria += [["1001","",[],"0"]]
        self.memoria += [["1010","",[],"0"]]
        self.memoria += [["1011","",[],"0"]]
        self.memoria += [["1100","",[],"0"]]
        self.memoria += [["1101","",[],"0"]]
        self.memoria += [["1110","",[],"0"]]
        self.memoria += [["1111","",[],"0"]]

    def print(self):
        t = PrettyTable(["Estado","Dueño","Dato","Direccion"])
        for x in self.memoria:
            t.add_row([x[1],x[2],x[3],x[0]])
        print(t)

    def read(self,direc,chip):
        for x in range(16):
            if (self.memoria[x][0] == direc):
                if(chip in self.memoria[x][2]):
                    print()
                else:
                    self.memoria[x][2] += [chip]
                    
                return self.memoria[x]

    def write(self,direc,data,chip):
        for x in range(16):
            if (direc == self.memoria[x][0]):
                self.memoria[x][3] = data
                largo = len(self.memoria[x][2])
                for y in range(largo):
                    print(y)
                    if(self.memoria[x][2][y] == chip):
                        print(self.memoria[x][2][0:y] + self.memoria[x][2][y+1:largo])
                        self.memoria[x][2] = self.memoria[x][2][0:y] + self.memoria[x][2][y+1:largo]
                        return self.memoria[x][2]
                    

    def changeState(self,state,direc):
        for x in range(16):
            if (self.memoria[x][0] == direc):
                self.memoria[x][1] = state
