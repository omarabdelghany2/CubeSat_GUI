from serialClass import *
from Styling_MainTab import *
from Styling_EBSTab import *
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

#todo in this file just youmna need to fill #1 in merge fucntion
class mergeDataWithGui ():
    def __init__(self):
           #constructor #1)object from styling.py (StylingMainTabObject)
                        #2)object from serial.func.py (serialObject)
                        #3)create object from ebs tab
                        #3)connect the the recieve button with its handler
                        
            self.serialObject=serialClass()
            self.StylingMainTabObject=Styling_MainTab()
            self.StylingEbsTabObject=Styling_EBSTab()
            self.StylingMainTabObject.Receiving_Connect_pushButton.clicked.connect(self.ReceiveHandler)
            self.StylingMainTabObject.TabsBar.currentChanged.connect(self.SwitchWindow)
            
    def merge(self):
                                 #1)#here merge data as the next line an example
                                   #first get the data from gui (baudrate ,comport)
            self.serialObject.baudRateRx=int(self.StylingMainTabObject.BaudRateRX_TextEdit.currentText())
            self.serialObject.comPortRx=self.StylingMainTabObject.ReceivingComPort_comboBox.currentText()
                                    # put the data in gui ----->>
            self.StylingMainTabObject.ReceivingWindow_textEdit.append(self.serialObject.serial_data)

            
            timestamp_str = str(self.serialObject.Time)  # Convert to string
            day = timestamp_str[0:2]
            month = timestamp_str[2:4]

            year = timestamp_str[4:8]
            hour = timestamp_str[8:10]
            minute = timestamp_str[10:12]
            second = timestamp_str[12:14]
            
            formatted_time = f"{day}/{month}/{year}/{hour}/{minute}/{second}"
            
            self.StylingMainTabObject.Time_LineEdit.setText(formatted_time)


            self.StylingMainTabObject.BatteryVolt_LineEdit.setText(str(self.serialObject.voltage))
            self.StylingMainTabObject.Current_LineEdit.setText(str(self.serialObject.current))
            self.StylingMainTabObject.Current33_LineEdit.setText(str(self.serialObject.current3_3))
            self.StylingMainTabObject.Current5_LineEdit.setText(str(self.serialObject.current_5))

            # Set the mode and color based on the value
            if self.serialObject.OBC == 1:
                   self.StylingMainTabObject.OBC_LineEdit.setText(str("ON"))
                   # Set color to green
                   self.StylingMainTabObject.OBC_LineEdit.setStyleSheet("background-color: green;")
            else:
                   self.StylingMainTabObject.OBC_LineEdit.setText(str("OFF"))
                   # Set color to red
                   self.StylingMainTabObject.OBC_LineEdit.setStyleSheet("background-color: red;")

            if self.serialObject.ADCS == 1:
                   self.StylingMainTabObject.ADCS_LineEdit.setText(str("ON"))
                   self.StylingMainTabObject.ADCS_LineEdit.setStyleSheet("background-color: green;")
            else:
                   self.StylingMainTabObject.ADCS_LineEdit.setText(str("OFF"))
                   self.StylingMainTabObject.ADCS_LineEdit.setStyleSheet("background-color: red;")

            if self.serialObject.Payload == 1:
                   self.StylingMainTabObject.Payload_LineEdit.setText(str("ON"))
                   self.StylingMainTabObject.Payload_LineEdit.setStyleSheet("background-color: green;")
            else:
                   self.StylingMainTabObject.Payload_LineEdit.setText(str("OFF"))
                   self.StylingMainTabObject.Payload_LineEdit.setStyleSheet("background-color: red;")

            if self.serialObject.comm_antennas == 1:
                   self.StylingMainTabObject.AntennaStatus_LineEdit.setText(str("ON"))
                   self.StylingMainTabObject.AntennaStatus_LineEdit.setStyleSheet("background-color: green;")
            else:
                   self.StylingMainTabObject.AntennaStatus_LineEdit.setText(str("OFF"))
                   self.StylingMainTabObject.AntennaStatus_LineEdit.setStyleSheet("background-color: red;")

            if self.serialObject.Temp == 1:
                   self.StylingMainTabObject.TempSensorStatus_LineEdit.setText(str("ON"))
                   self.StylingMainTabObject.TempSensorStatus_LineEdit.setStyleSheet("background-color: green;")
            else:
                   self.StylingMainTabObject.TempSensorStatus_LineEdit.setText(str("OFF"))
                   self.StylingMainTabObject.TempSensorStatus_LineEdit.setStyleSheet("background-color: red;")

            if self.serialObject.solar1 == 1:
                   self.StylingMainTabObject.SolarStatus1_LineEdit.setText(str("ON"))
                   self.StylingMainTabObject.SolarStatus1_LineEdit.setStyleSheet("background-color: green;")
            else:
                   self.StylingMainTabObject.SolarStatus1_LineEdit.setText(str("OFF"))
                   self.StylingMainTabObject.SolarStatus1_LineEdit.setStyleSheet("background-color: red;")

            if self.serialObject.solar2 == 1:
                   self.StylingMainTabObject.SolarStatus2_LineEdit.setText(str("ON"))
                   self.StylingMainTabObject.SolarStatus2_LineEdit.setStyleSheet("background-color: green;")
            else:
                   self.StylingMainTabObject.SolarStatus2_LineEdit.setText(str("OFF"))
                   self.StylingMainTabObject.SolarStatus2_LineEdit.setStyleSheet("background-color: red;")

            if self.serialObject.solar3 == 1:
                   self.StylingMainTabObject.SolarStatus3_LineEdit.setText(str("ON"))
                   self.StylingMainTabObject.SolarStatus3_LineEdit.setStyleSheet("background-color: green;")
            else:
                   self.StylingMainTabObject.SolarStatus3_LineEdit.setText(str("OFF"))
                   self.StylingMainTabObject.SolarStatus3_LineEdit.setStyleSheet("background-color: red;")

            if self.serialObject.solar4 == 1:
                   self.StylingMainTabObject.SolarStatus4_LineEdit.setText(str("ON"))
                   self.StylingMainTabObject.SolarStatus4_LineEdit.setStyleSheet("background-color: green;")
            else:
                   self.StylingMainTabObject.SolarStatus4_LineEdit.setText(str("OFF"))
                   self.StylingMainTabObject.SolarStatus4_LineEdit.setStyleSheet("background-color: red;")
              


              #-->>todo  add the eps tab elements here merge them>>>>
              
    

    def ReceiveHandler(self):
           self.merge()
           self.serialObject.recieve_serial()
           self.serialObject.Manager_ofRecievedData()
           self.merge()



    def SwitchWindow(self,index):
       if(index==0) :
              self.StylingMainTabObject.show()
              self.StylingEbsTabObject.hide()
       elif(index==2):
              self.StylingMainTabObject.hide()
              self.StylingEbsTabObject.show() 
