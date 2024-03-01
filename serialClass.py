import serial
import time
import threading
from PyQt6 import QtWidgets
from PyQt6 import QtCore 
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer


class SerialClass(QtCore.QThread):
    #variables used for recieving and transimitting over serial
    baudRateTx = 1
    Ser_Flag = 0
    Image_Flag = 0
    EncodedImage_Bytes = b''
    capture_event = None
    MergeEvent = None
    timer = QTimer()
    baudRateRx=0
    comPortTx=""
    comPortRx=""
    response = b''
  #variables used for main battery status
    voltage=0.0
    current=0.0
    current3_3=0.0
    current_5=0.0

    #varaibles used for Subsystem status
    OBC=0
    ADCS=0
    Payload=0
    comm_antennas=0
    #External system status variables
    Temp=0
    solar1=0
    solar2=0
    solar3=0
    solar4=0

    #Time
    Time=0

    serial_data=""

#-----------------------------------------------------------------------
    #varaibles of the ebs tab                                       -->>>EBSTAB

    BatteryHeater=0
    EbsTemp=0.0

    MotorX=0
    MotorY=0
    MotorZ=0

#-----------------------------------------------------------------------
    #varaibles of the ADCS tab                                       -->>>ADCSTAB

    lux1 = 0
    lux2 = 0
    lux3 = 0
    lux4 = 0
    AccX = 0.0
    AccY = 0.0
    AccZ = 0.0
    GyroX = 0.0
    GyroY = 0.0
    GyroZ = 0.0
    MagnX = 0.0
    MagnY = 0.0
    MagnZ = 0.0
    ADSC_Temp = 0
    Kalmanx = 0.0
    Kalmany = 0.0
    Kalmanz = 0.0
    GPS_d3_Fix = 0
    Number_of_Satellites = 0
    Longitude = 0.0
    Latitude = 0.0
    Altitude = 0.0

#-----------------------------------------------------------------------
    #varaibles of the COMM tab                                       -->>>COMM TAB

    PowerTx = 0
    PowerRx = 0
    COMM_Status = 0
    ModulationScheme = 0
    Freq = 0
    FreqBand = 0
    DataRate = 0
    sttt = 0
    
    data =0

    def __init__(self): # Initialise with serial port details
        QtCore.QThread.__init__(self)
        self.running = True
    
    def run(self):          
                        # Run serial reader thread
        try:
            if self.MergeEvent:
                self.ser = serial.Serial(self.comPortRx, self.baudRateRx, timeout = 1)
            else:
                self.ser = serial.Serial(self.comPortTx, self.baudRateTx, timeout = 1)
            self.ser.flushInput()

            if not self.ser:
                print("Can't open port")
                self.running = False
            while self.running:
              i=0
              if(self.MergeEvent and (not(self.capture_event)) ) :
                # Flush Input and Ouptut Buffers
                self.ser.flushInput()
                self.ser.flushOutput()
                # Read one line from the serial port
                self.serial_data = self.ser.readline().decode('utf-8').strip()
                # Print the received data
                print("Received: {}".format(self.serial_data))

                self.received_data = self.serial_data.split(',')
                # print(self.received_data)
                if(len(self.received_data) > 40) :

                            # Assigning values to variables
                            # Assigning values to variables
                            data = (self.received_data[i])
                            i+=1
                            Time = int(self.received_data[i])
                            i+=1
                            voltage = float(self.received_data[i])
                            i+=1
                            current = float(self.received_data[i])
                            i+=1
                            current3_3 = float(self.received_data[i])
                            i+=1
                            current_5 = float(self.received_data[i])
                            i+=1
                            Payload = int(self.received_data[i])
                            i+=1
                            OBC = int(self.received_data[i])
                            i+=1
                            ADCS = int(self.received_data[i])
                            i+=1
                            Temp = int(self.received_data[i])
                            i+=1
                            sttt = int(self.received_data[i])
                            i+=1
                            solar1 = int(self.received_data[i])
                            i+=1
                            solar2 = int(self.received_data[i])
                            i+=1
                            solar3 = int(self.received_data[i])
                            i+=1
                            solar4 = int(self.received_data[i])
                            i+=1
                            comm_antennas = int(self.received_data[i])
                            i+=1

                            #-->EBS VARAIBLES
                            BatteryHeater=int(self.received_data[i])
                            i+=1
                            EbsTemp=float(self.received_data[i])
                            i+=1

                            #-->ADCS VARAIBLES

                            lux1 = int(self.received_data[i])
                            i+=1
                            lux2 = int(self.received_data[i])
                            i+=1
                            lux3 = int(self.received_data[i])
                            i+=1
                            lux4 = int(self.received_data[i])
                            i+=1
                            AccX = float(self.received_data[i])
                            i+=1
                            AccY = float(self.received_data[i])
                            i+=1
                            AccZ = float(self.received_data[i])
                            i+=1
                            GyroX = float(self.received_data[i])
                            i+=1
                            GyroY = float(self.received_data[i])
                            i+=1
                            GyroZ = float(self.received_data[i])
                            i+=1
                            MagnX = float(self.received_data[i])
                            i+=1
                            MagnY = float(self.received_data[i])
                            i+=1
                            MagnZ = float(self.received_data[i])
                            i+=1
                            ADSC_Temp = float(self.received_data[i])
                            i+=1
                            Kalmanx = float(self.received_data[i])
                            i+=1
                            KalmanY = float(self.received_data[i])
                            i+=1
                            KalmanZ = float(self.received_data[i])
                            i+=1
                            GPS_d3_Fix = float(self.received_data[i])
                            i+=1

                            Number_of_Satellites = float(self.received_data[i])
                            i+=1

                            Longitude = float(self.received_data[i])
                            i+=1
                            Latitude = float(self.received_data[i])
                            i+=1
                            Altitude = float(self.received_data[i])
                            i+=1


                            #-->EBS VARAIBLES
                            
                            MotorX=int(self.received_data[i])
                            i+=1
                            MotorY=int(self.received_data[i])
                            i+=1
                            MotorZ=int(self.received_data[i])


                            # Assigning values to instance variables
                            self.Time = Time
                            self.voltage = voltage
                            self.current = current
                            self.current3_3 = current3_3
                            self.current_5 = current_5
                            self.Payload = Payload
                            self.OBC = OBC
                            self.ADCS = ADCS
                            self.Temp = Temp
                            self.solar1 = solar1
                            self.solar2 = solar2
                            self.solar3 = solar3
                            self.solar4 = solar4
                            self.comm_antennas = comm_antennas

                            #-->EBS
                            self.lux1 =lux1
                            self.lux2 = lux2
                            self.lux3 = lux3
                            self.lux4 = lux4
                            self.AccX = AccX
                            self.AccY = AccY
                            self.AccZ = AccZ
                            self.GyroX = GyroX
                            self.GyroY = GyroY
                            self.GyroZ = GyroZ
                            self.MagnX = MagnX
                            self.MagnY = MagnY
                            self.MagnZ = MagnZ
                            self.ADSC_Temp = ADSC_Temp
                            self.Kalmanx = Kalmanx
                            self.Kalmany = KalmanY
                            self.Kalmanz = KalmanZ
                            self.GPS_d3_Fix = GPS_d3_Fix
                            self.Number_of_Satellites = Number_of_Satellites
                            self.Longitude = Longitude
                            self.Latitude = Latitude
                            self.Altitude = Altitude

                            #-->EBS
                            self.BatteryHeater=BatteryHeater
                            self.EbsTemp=EbsTemp
                            self.MotorX=MotorX
                            self.MotorY=MotorY
                            self.MotorZ=MotorZ
    
                            self.msleep(10)
              else:
                self.ser.cancel_read
                self.ser.write(b'PIC')
                while self.response == b'':
                    self.response = self.ser.readline().strip()
                self.EncodedImage_Bytes = self.response
                print("Received Image data: {}".format(self.response)) 
                self.response =b''                      
              self.MergeEvent = True              
            if self.ser:                                    # Close serial port when thread finished
                self.ser.close()
                self.ser = None
        except serial.serialutil.SerialException:
            print("Port Exception")
                

