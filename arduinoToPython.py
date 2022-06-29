from pyfirmata import Arduino ,SERVO,util
from time import sleep
import main
file = open("result.txt", "r")
content = file.readlines()
fileOne = content[2]
confidence = content[3]
fileOne = fileOne[17:len(fileOne)-2]
print("arduinoToPython\nfileOne = " + fileOne)
print(confidence)
fileOneList = list(fileOne)
print(fileOneList)
print(len(fileOneList))
for i in range(0,len(fileOneList)):
    if (fileOneList[i]!=" "):
        print(fileOneList[i])






port = 'COM5'

pin2 = 2
pin3 = 3
pin4 = 4
pin5 = 5
board = Arduino(port)

board.digital[pin2].mode=SERVO
board.digital[pin3].mode=SERVO
board.digital[pin4].mode=SERVO
board.digital[pin5].mode=SERVO

def rotateservo(pin2,angle):
    board.digital[pin2].write(angle)


def rotateservo2(pin3, angle):
    board.digital[pin3].write(angle)


def rotateservo3(pin4, angle):
    board.digital[pin4].write(angle)


def rotateservo4(pin5, angle):
    board.digital[pin5].write(angle)

def default():
    board.digital[pin2].write(0)
    board.digital[pin3].write(0)
    board.digital[pin4].write(0)
    board.digital[pin5].write(0)

default()
def handA():
    for i in range(0, 180):
        rotateservo(pin2, i)
    for i in range(0, 180):
        rotateservo2(pin3, i)
    for i in range(0, 180):
        rotateservo3(pin4, i)
    for i in range(0, 180):
        rotateservo4(pin5, i)
def handB():
    for i in range(0, 0):
        rotateservo(pin2, i)
    for i in range(0, 0):
        rotateservo2(pin3, i)
    for i in range(0, 0):
        rotateservo3(pin4, i)
    for i in range(0, 0):
        rotateservo4(pin5, i)

def handC():
    for i in range(0, 90):
        rotateservo(pin2, i)
    for i in range(0, 90):
        rotateservo2(pin3, i)
    for i in range(0, 90):
        rotateservo3(pin4, i)
    for i in range(0, 90):
        rotateservo4(pin5, i)


def handD():
    for i in range(0, 1):
        rotateservo(pin2, i)
    for i in range(0, 90):
        rotateservo2(pin3, i)
    for i in range(0, 90):
        rotateservo3(pin4, i)
    for i in range(0, 90):
        rotateservo4(pin5, i)

def handE():
    for i in range(0, 90):
        rotateservo(pin2, i)
    for i in range(0, 90):
        rotateservo2(pin3, i)
    for i in range(0, 90):
        rotateservo3(pin4, i)
    for i in range(0, 90):
        rotateservo4(pin5, i)

def handF():
    for i in range(0, 90):
        rotateservo(pin2, i)
    for i in range(0, 1):
        rotateservo2(pin3, i)
    for i in range(0, 1):
        rotateservo3(pin4, i)
    for i in range(0, 1):
        rotateservo4(pin5, i)

def handG():
    for i in range(0, 45):
        rotateservo(pin2, i)
    for i in range(0, 180):
        rotateservo2(pin3, i)
    for i in range(0, 180):
        rotateservo3(pin4, i)
    for i in range(0, 180):
        rotateservo4(pin5, i)

def handH():
    for i in range(0, 90):
        rotateservo(pin2, i)
    for i in range(0, 90):
        rotateservo2(pin3, i)
    for i in range(0, 180):
        rotateservo3(pin4, i)
    for i in range(0, 180):
        rotateservo4(pin5, i)


def handI():
    for i in range(0, 180):
        rotateservo(pin2, i)
    for i in range(0, 180):
        rotateservo2(pin3, i)
    for i in range(0, 180):
        rotateservo3(pin4, i)
    for i in range(0, 1):
        rotateservo4(pin5, i)


def handJ():
    for i in range(0, 180):
        rotateservo(pin2, i)
    for i in range(0, 180):
        rotateservo2(pin3, i)
    for i in range(0, 180):
        rotateservo3(pin4, i)
    for i in range(0, 1):
        rotateservo4(pin5, i)

def handK():
    for i in range(0, 1):
        rotateservo(pin2, i)
    for i in range(0, 1):
        rotateservo2(pin3, i)
    for i in range(0, 180):
        rotateservo3(pin4, i)
    for i in range(0, 180):
        rotateservo4(pin5, i)


def handL():
    for i in range(0, 1):
        rotateservo(pin2, i)
    for i in range(0, 180):
        rotateservo2(pin3, i)
    for i in range(0, 180):
        rotateservo3(pin4, i)
    for i in range(0, 180):
        rotateservo4(pin5, i)



def handM():
    for i in range(0, 1):
        rotateservo(pin2, i)
    for i in range(0, 1):
        rotateservo2(pin3, i)
    for i in range(0, 1):
        rotateservo3(pin4, i)
    for i in range(0, 180):
        rotateservo4(pin5, i)


def handN():
    for i in range(0, 1):
        rotateservo(pin2, i)
    for i in range(0, 1):
        rotateservo2(pin3, i)
    for i in range(0, 180):
        rotateservo3(pin4, i)
    for i in range(0, 180):
        rotateservo4(pin5, i)


def handO():
    for i in range(0, 45):
        rotateservo(pin2, i)
    for i in range(0, 45):
        rotateservo2(pin3, i)
    for i in range(0, 45):
        rotateservo3(pin4, i)
    for i in range(0, 45):
        rotateservo4(pin5, i)


def handP():
    for i in range(0, 1):
        rotateservo(pin2, i)
    for i in range(0, 45):
        rotateservo2(pin3, i)
    for i in range(0, 180):
        rotateservo3(pin4, i)
    for i in range(0, 180):
        rotateservo4(pin5, i)

def handQ():
    for i in range(0, 180):
        rotateservo(pin2, i)
    for i in range(0, 30):
        rotateservo2(pin3, i)
    for i in range(0, 180):
        rotateservo3(pin4, i)
    for i in range(0, 180):
        rotateservo4(pin5, i)


def handR():
    for i in range(0, 1):
        rotateservo(pin2, i)
    for i in range(0, 1):
        rotateservo2(pin3, i)
    for i in range(0, 180):
        rotateservo3(pin4, i)
    for i in range(0, 180):
        rotateservo4(pin5, i)


def handS():
    for i in range(0, 180):
        rotateservo(pin2, i)
    for i in range(0, 180):
        rotateservo2(pin3, i)
    for i in range(0, 180):
        rotateservo3(pin4, i)
    for i in range(0, 180):
        rotateservo4(pin5, i)


def handT():
    for i in range(0, 1):
        rotateservo(pin2, i)
    for i in range(0, 180):
        rotateservo2(pin3, i)
    for i in range(0, 180):
        rotateservo3(pin4, i)
    for i in range(0, 180):
        rotateservo4(pin5, i)


def handU():
    for i in range(0, 1):
        rotateservo(pin2, i)
    for i in range(0, 1):
        rotateservo2(pin3, i)
    for i in range(0, 180):
        rotateservo3(pin4, i)
    for i in range(0, 180):
        rotateservo4(pin5, i)

def handV():
    for i in range(0, 1):
        rotateservo(pin2, i)
    for i in range(0, 1):
        rotateservo2(pin3, i)
    for i in range(0, 180):
        rotateservo3(pin4, i)
    for i in range(0, 180):
        rotateservo4(pin5, i)

def handW():
    for i in range(0, 1):
        rotateservo(pin2, i)
    for i in range(0, 1):
        rotateservo2(pin3, i)
    for i in range(0, 1):
        rotateservo3(pin4, i)
    for i in range(0, 180):
        rotateservo4(pin5, i)

def handX():
    for i in range(0, 45):
        rotateservo(pin2, i)
    for i in range(0, 180):
        rotateservo2(pin3, i)
    for i in range(0, 180):
        rotateservo3(pin4, i)
    for i in range(0, 180):
        rotateservo4(pin5, i)

def handY():
    for i in range(0, 180):
        rotateservo(pin2, i)
    for i in range(0, 180):
        rotateservo2(pin3, i)
    for i in range(0, 180):
        rotateservo3(pin4, i)
    for i in range(0, 1):
        rotateservo4(pin5, i)

def handZ():
    for i in range(0, 1):
        rotateservo(pin2, i)
    for i in range(0, 180):
        rotateservo2(pin3, i)
    for i in range(0, 180):
        rotateservo3(pin4, i)
    for i in range(0, 180):
        rotateservo4(pin5, i)


for i in range(0, len(fileOneList)):
    if (fileOneList[i] == "a"):
        handA()

    elif (fileOneList[i] == "b"):
        handB()

    elif (fileOneList[i] == "c"):
        handC()

    elif (fileOneList[i] == "d"):
        handD()

    elif (fileOneList[i] == "e"):
        handE()
    elif (fileOneList[i] == "f"):
        handF()
    elif (fileOneList[i] == "g"):
        handG()
    elif (fileOneList[i] == "h"):
        handH()
    elif (fileOneList[i] == "i"):
        handI()
    elif (fileOneList[i] == "j"):
        handJ()
    elif (fileOneList[i] == "k"):
        handK()
    elif (fileOneList[i] == "l"):
        handL()
    elif (fileOneList[i] == "m"):
        handM()
    elif (fileOneList[i] == "n"):
        handN()
    elif (fileOneList[i] == "o"):
        handO()
    elif (fileOneList[i] == "p"):
        handP()
    elif (fileOneList[i] == "q"):
        handQ()
    elif (fileOneList[i] == "r"):
        handR()
    elif (fileOneList[i] == "s"):
        handS()
    elif (fileOneList[i] == "t"):
        handT()
    elif (fileOneList[i] == "u"):
        handU()

    elif (fileOneList[i] == "v"):
        handV()
    elif (fileOneList[i] == "w"):
        handW()
    elif (fileOneList[i] == "x"):
        handX()
    elif (fileOneList[i] == "y"):
        handY()
    elif (fileOneList[i] == "z"):
        handZ()
    elif (fileOneList[i] == " "):
        sleep(0.1)
    sleep(2)
# while True:
#     #default()
#     angle2 = input("input pin 2: ")
#     angle3 = input("input pin 3 : ")
#     angle4 = input("input pin 4 : ")
#     angle5 = input("input pin 5 : ")
#
#     if angle2== "1":
#         for i in range(0,180):
#             rotateservo(pin2,i)
#     elif angle2 == "2":
#         for i in range(0,90):
#             rotateservo(pin2,i)
#     elif angle2 == "3":
#         for i in range(0, 180):
#             rotateservo(pin2, i)
#     if angle3== "1":
#         for i in range(0,180):
#             rotateservo2(pin3,i)
#     elif angle3 == "2":
#         for i in range(0,90):
#             rotateservo2(pin3,i)
#     elif angle3== "3":
#         for i in range(0, 270):
#             rotateservo2(pin3, i)
#     if angle4== "1":
#         for i in range(0, 180):
#             rotateservo3(pin4,i)
#     elif angle4 == "2":
#         for i in range(0,90):
#             rotateservo3(pin4,i)
#     elif angle4== "3":
#         for i in range(0,270):
#             rotateservo3(pin4, i)
#     if angle5== "1":
#         for i in range(0, 180):
#             rotateservo4(pin5,i)
#     elif angle5 == "2":
#         for i in range(0,90):
#             rotateservo4(pin5,i)
#     elif angle5== "3":
#         for i in range(0,270):
#             rotateservo4(pin5, i)

