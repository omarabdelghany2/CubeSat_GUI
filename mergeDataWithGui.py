from serialClass import *
from Styling import *
from datetime import datetime

#todo in this file just youmna need to fill #1 in merge fucntion
class mergeDataWithGui ():
    def __init__(self):
           #constructor #1)object from styling.py (stylingObject)
                        #2)object from serial.func.py (serialObject)
                        #3)connect the the recieve button with its handler
                        
            self.serialObject=serialClass()
            self.StylingObject=Styling()
            self.StylingObject.Receiving_Connect_pushButton.clicked.connect(self.ReceiveHandler)
    def merge(self):
                                 #1)#here merge data as the next line an example
            #first get the data from gui (baudrate ,comport)
            self.serialObject.baudRateRx=int(self.StylingObject.BaudRateRX_TextEdit.currentText())
            self.serialObject.comPortRx=self.StylingObject.ReceivingComPort_comboBox.currentText()
            # put the data in gui ----->>
            self.StylingObject.ReceivingWindow_textEdit.append(self.serialObject.serial_data)

            
            timestamp_str = str(self.serialObject.Time)  # Convert to string
            day = timestamp_str[0:2]
            month = timestamp_str[2:4]

            year = timestamp_str[4:8]
            hour = timestamp_str[8:10]
            minute = timestamp_str[10:12]
            second = timestamp_str[12:14]
            
            formatted_time = f"{day}/{month}/{year}/{hour}/{minute}/{second}"
            
            self.StylingObject.Time_LineEdit.setText(formatted_time)


            self.StylingObject.BatteryVolt_LineEdit.setText(str(self.serialObject.voltage))
            self.StylingObject.Current_LineEdit.setText(str(self.serialObject.current))
            self.StylingObject.Current33_LineEdit.setText(str(self.serialObject.current3_3))
            self.StylingObject.Current5_LineEdit.setText(str(self.serialObject.current_5))

            # Set the mode and color based on the value
            if self.serialObject.OBC == 1:
                   self.StylingObject.OBC_LineEdit.setText(str("ON"))
                   # Set color to green
                   self.StylingObject.OBC_LineEdit.setStyleSheet("background-color: green;")
            else:
                   self.StylingObject.OBC_LineEdit.setText(str("OFF"))
                   # Set color to red
                   self.StylingObject.OBC_LineEdit.setStyleSheet("background-color: red;")

            if self.serialObject.ADCS == 1:
                   self.StylingObject.ADCS_LineEdit.setText(str("ON"))
                   self.StylingObject.ADCS_LineEdit.setStyleSheet("background-color: green;")
            else:
                   self.StylingObject.ADCS_LineEdit.setText(str("OFF"))
                   self.StylingObject.ADCS_LineEdit.setStyleSheet("background-color: red;")

            if self.serialObject.Payload == 1:
                   self.StylingObject.Payload_LineEdit.setText(str("ON"))
                   self.StylingObject.Payload_LineEdit.setStyleSheet("background-color: green;")
            else:
                   self.StylingObject.Payload_LineEdit.setText(str("OFF"))
                   self.StylingObject.Payload_LineEdit.setStyleSheet("background-color: red;")

            if self.serialObject.comm_antennas == 1:
                   self.StylingObject.AntennaStatus_LineEdit.setText(str("ON"))
                   self.StylingObject.AntennaStatus_LineEdit.setStyleSheet("background-color: green;")
            else:
                   self.StylingObject.AntennaStatus_LineEdit.setText(str("OFF"))
                   self.StylingObject.AntennaStatus_LineEdit.setStyleSheet("background-color: red;")

            if self.serialObject.Temp == 1:
                   self.StylingObject.TempSensorStatus_LineEdit.setText(str("ON"))
                   self.StylingObject.TempSensorStatus_LineEdit.setStyleSheet("background-color: green;")
            else:
                   self.StylingObject.TempSensorStatus_LineEdit.setText(str("OFF"))
                   self.StylingObject.TempSensorStatus_LineEdit.setStyleSheet("background-color: red;")

            if self.serialObject.solar1 == 1:
                   self.StylingObject.SolarStatus1_LineEdit.setText(str("ON"))
                   self.StylingObject.SolarStatus1_LineEdit.setStyleSheet("background-color: green;")
            else:
                   self.StylingObject.SolarStatus1_LineEdit.setText(str("OFF"))
                   self.StylingObject.SolarStatus1_LineEdit.setStyleSheet("background-color: red;")

            if self.serialObject.solar2 == 1:
                   self.StylingObject.SolarStatus2_LineEdit.setText(str("ON"))
                   self.StylingObject.SolarStatus2_LineEdit.setStyleSheet("background-color: green;")
            else:
                   self.StylingObject.SolarStatus2_LineEdit.setText(str("OFF"))
                   self.StylingObject.SolarStatus2_LineEdit.setStyleSheet("background-color: red;")

            if self.serialObject.solar3 == 1:
                   self.StylingObject.SolarStatus3_LineEdit.setText(str("ON"))
                   self.StylingObject.SolarStatus3_LineEdit.setStyleSheet("background-color: green;")
            else:
                   self.StylingObject.SolarStatus3_LineEdit.setText(str("OFF"))
                   self.StylingObject.SolarStatus3_LineEdit.setStyleSheet("background-color: red;")

            if self.serialObject.solar4 == 1:
                   self.StylingObject.SolarStatus4_LineEdit.setText(str("ON"))
                   self.StylingObject.SolarStatus4_LineEdit.setStyleSheet("background-color: green;")
            else:
                   self.StylingObject.SolarStatus4_LineEdit.setText(str("OFF"))
                   self.StylingObject.SolarStatus4_LineEdit.setStyleSheet("background-color: red;")
    
    def ReceiveHandler(self):
           self.merge()
           self.serialObject.recieve_serial()
           self.serialObject.Manager_ofRecievedData()
           self.merge()
