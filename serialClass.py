
import serial

class serialClass():
    #variables used for recieving and transimitting over serial
    baudRateTx=1
    baudRateRx=0
    comPortTx=""
    comPortRx=""
    
    #variables used for main battery status
    voltage=0.0
    current=0
    current3_3=0
    current_5=0

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
    Altitude = 0

    #-----------------------------------------------------------------------
    #varaibles of the COMM tab                                       -->>>COMM TAB

    PowerTx = 0
    PowerRx = 0
    COMM_Status = 0
    ModulationScheme = 0
    Freq = 0
    FreqBand = 0
    DataRate = 0

    

    def recieve_serial(self):
        try:
            # Replace 'COMx' with your actual serial port (e.g., COM3 on Windows, /dev/ttyUSB0 on Linux)
            with serial.Serial('/dev/cu.usbserial-1120', self.baudRateRx, timeout=20) as serial_port:
            #with serial.Serial(self.comPortRx, self.baudRateRx, timeout=10) as serial_port:    
                # Read one line from the serial port
                self.serial_data = serial_port.readline().decode('utf-8').strip()
                # Print the received data
                print("Received: {}".format(self.serial_data))
        except serial.SerialException as e:
            print(f"Error: {e}")


    def Manager_ofRecievedData(self):
        # Assuming self.serial_data is a string containing comma-separated values
        self.received_data = self.serial_data.split(',')

        # Assigning values to variables
        Time = int(self.received_data[0])
        voltage = float(self.received_data[1])
        current = int(self.received_data[2])
        current3_3 = int(self.received_data[3])
        current_5 = int(self.received_data[4])
        Payload = int(self.received_data[5])
        OBC = int(self.received_data[6])
        ADCS = int(self.received_data[7])
        Temp = int(self.received_data[8])
        solar1 = int(self.received_data[9])
        solar2 = int(self.received_data[10])
        solar3 = int(self.received_data[11])
        solar4 = int(self.received_data[12])
        comm_antennas = int(self.received_data[13])

        #-->EBS VARAIBLES
        BatteryHeater=int(self.received_data[14])
        EbsTemp=float(self.received_data[15])

        #-->ADCS VARAIBLES

        lux1 = int(self.received_data[16])
        lux2 = int(self.received_data[17])
        lux3 = int(self.received_data[18])
        lux4 = int(self.received_data[19])
        AccX = float(self.received_data[20])
        AccY = float(self.received_data[21])
        AccZ = float(self.received_data[22])
        GyroX = float(self.received_data[23])
        GyroY = float(self.received_data[24])
        GyroZ = float(self.received_data[25])
        MagnX = float(self.received_data[26])
        MagnY = float(self.received_data[27])
        MagnZ = float(self.received_data[28])
        ADSC_Temp = int(self.received_data[29])
        Kalmanx = float(self.received_data[30])
        KalmanY = float(self.received_data[31])
        KalmanZ = float(self.received_data[32])
        GPS_d3_Fix = int(self.received_data[33])
        Number_of_Satellites = int(self.received_data[34])
        Longitude = float(self.received_data[35])
        Latitude = float(self.received_data[36])
        Altitude = int(self.received_data[37])


        #-->EBS VARAIBLES
        
        MotorX=int(self.received_data[38])
        MotorY=int(self.received_data[39])
        MotorZ=int(self.received_data[40])

        #-->COMM VARAIBLES
        PowerTx =int(self.received_data[41])
        PowerRx =int(self.received_data[42])
        COMM_Status =int(self.received_data[43])
        ModulationScheme =str(self.received_data[44])
        Freq =int(self.received_data[45])
        FreqBand =int(self.received_data[46])
        DataRate =int(self.received_data[47])


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


        self.PowerTx = PowerTx
        self.PowerRx = PowerRx
        self.COMM_Status = COMM_Status
        self.ModulationScheme = ModulationScheme
        self.Freq = Freq
        self.FreqBand = FreqBand
        self.DataRate = DataRate








       