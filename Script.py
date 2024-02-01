import serial
import time
import struct

ser = serial.Serial('COM4' , baudrate = 115200,timeout = 0.01)
time.sleep(3)

Num_Points = 5
DataList = [0]*Num_Points
string = b''

def getStatus(Command,DataRX) :
    SubSystemDataLen = DataRX
    SubsystemList = [0]*SubSystemDataLen
    for DataIndex in range(0,SubSystemDataLen) :
        ser.write(Command)
        Stm32Data = ser.read(5)
        SubsystemList[DataIndex] = Stm32Data
    return SubsystemList

ExitFlag = False

while 1:
    print('=================== SERIAL TERMINAL ====================\n')
    print('Please Select from the List of Commands to Recieve Data \n')
    print('1] Read Subsytem Status  \n')
    print('2] Read Battery  Status  \n')
    print('3] Read External System Status  \n')
    print('4] Exit Main Program')

    Command = input('Enter Your Choice : ')
    CMD_byte = str.encode(Command)
   
    if Command == '4' :
        break
    elif Command == '1':
        DataList = getStatus(CMD_byte , 4)
        print('Battery Status')
        print(DataList)
    elif Command == '2':
        DataList = getStatus(CMD_byte, 4)
        print('Battery Status')
        print(DataList)
    elif Command == '3':
        DataList = getStatus(CMD_byte , 5)
        print('Battery Status')
        print(DataList)
