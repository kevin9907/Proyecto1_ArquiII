from Chip import *
import random

def randomInstr(cant, lista):
    res = []
    for x in range(cant):
        instr = random.randint(0,1)
        chip = random.randint(0,1)
        proc = random.randint(0,1)
        memoria = random.randint(0,15)
        valor = random.randint(0,19)
        valor = lista[valor]
        if(instr == 1):
            instr = "READ"
            valor = ""
        else:
            instr = "WRITE"
        if(chip == 0):
            chip = "0"
        else:
            chip = "1"
        if(proc == 0):
            proc = "P0"
        else:
            proc = "P1"
        if(memoria == 0):
            memoria = "0000"
        elif(memoria == 1):
            memoria = "0001"
        elif(memoria == 2):
            memoria = "0010"
        elif(memoria == 3):
            memoria = "0011"
        elif(memoria == 4):
            memoria = "0100"
        elif(memoria == 5):
            memoria = "0101"
        elif(memoria == 6):
            memoria = "0110"
        elif(memoria == 7):
            memoria = "0111"
        elif(memoria == 8):
            memoria = "1000"
        elif(memoria == 9):
            memoria = "1001"
        elif(memoria == 10):
            memoria = "1010"
        elif(memoria == 11):
            memoria = "1011"
        elif(memoria == 12):
            memoria = "1100"
        elif(memoria == 13):
            memoria = "1101"
        elif(memoria == 14):
            memoria = "1110"
        elif(memoria == 15):
            memoria = "1111"
        res += [proc+","+chip+":"+instr + " " + memoria + "," + valor]
    print(res)
    return res
        
        
        


def main():
    memoriaP = memoria()
    lista = ["0000","0001","10A1","C010","C001","D001","D000","C000","A110","B001","B000","0101","1000","1111","1010","A0A0","00A0","A000","AAAA","ABCD"]
    chip0 = Chip("0",memoriaP)
    chip1 = Chip("1",memoriaP)
    bus = randomInstr(5,lista)
    for x in bus:
        print(x)
    chip0.updateBus(bus)
    chip1.updateBus(bus)


    
main()
