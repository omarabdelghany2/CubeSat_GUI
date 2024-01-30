
import serial

class serialClass():
    #variables used for recieving and transimitting over serial
    baudRateTx=1
    baudRateRx=0
    comPortTx=0
    comPortRx=0
    
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

    def recieve_serial(self):
        
        # Replace 'COM3' with the appropriate serial port for your device
        ser = serial.Serial("COM"+str(self.comPortRx), self.baudRateRx)  # You might need to adjust the baud rate

        try:
            while True:
                # Read a line from the serial port
                self.line = ser.readline().decode('utf-8').strip()
                
                # Print the received data
                self.Manager_ofRecievedData(self.line)
                print("Received:", self.line)

        except KeyboardInterrupt:
            # Close the serial port when the script is interrupted
            ser.close()
            print("Serial port closed.")

    def Manager_ofRecievedData(self):
        #GET THE RECIEVE DATA AND EQUAL IT WITH THE VARAABLES IN THIS CLASS
        #get the data from the self.line and equal it with the specific varaible
        #u have many recieved variable so manage them in this functions by equal to the self.solar1 as example
        #an example ----->>self.solar1=self.recieved_char 
        self.received_char=self.line