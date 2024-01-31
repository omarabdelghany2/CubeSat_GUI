
import serial

class serialClass():
    #variables used for recieving and transimitting over serial
    baudRateTx=1
    baudRateRx=0
    comPortTx=""
    comPortRx=""
    
    #variables used for main battery status
    voltage=0
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
    solar5=0 

    serial_data=""


    def recieve_serial(self):
        # Replace 'COMx' with your actual serial port (e.g., COM3 on Windows, /dev/ttyUSB0 on Linux)
        #serial_port =  serial.Serial(str(self.comPortRx), self.baudRateRx, timeout=1) #uncomment for windows
        serial_port =  serial.Serial('/dev/cu.usbserial-130', self.baudRateRx, timeout=1) #uncomment on mac

        # Read one line from the serial port
        self.serial_data = serial_port.readline().decode('utf-8').strip()
        # Print the received data
        print("Received: {}".format(self.serial_data))



    def Manager_ofRecievedData(self):
        #GET THE RECIEVE DATA AND EQUAL IT WITH THE VARAABLES IN THIS CLASS
        #get the data from the self.line and equal it with the specific varaible
        #u have many recieved variable so manage them in this functions by equal to the self.solar1 as example
        #an example ----->>self.solar1=self.recieved_char 
        self.received_data=self.serial_data






       