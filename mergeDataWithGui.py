from serialClass import *
from Styling import *

#todo in this file just youmna need to fill #1 in merge fucntion
class mergeDataWithGui ():
    def __init__(self):
           #constructor #1)object from styling.py (stylingObject)->youmna
                        #2)object from serial.func.py (serialObject) ->omar
                        #3)connect the the recieve button with its handler
                        
            self.serialObject=serialClass()
            self.StylingObject=Styling()
            self.StylingObject.Receiving_Connect_pushButton.clicked.connect(self.ReceiveHandler)
    def merge(self):
                                 #1)#here merge data as the next line an example  --> youmna do this 
            #first get the data from gui (baudrate ,comport)
            self.serialObject.baudRateRx=int(self.StylingObject.BaudRateRX_TextEdit.currentText())
            self.serialObject.comPortRx=self.StylingObject.ReceivingComPort_comboBox.currentText()
            # put the data in gui ----->>youmna #todo
            self.StylingObject.ReceivingWindow_textEdit.append(self.serialObject.serial_data)
            self.StylingObject.BatteryVolt_LineEdit.setText(str(self.serialObject.voltage))
    
    def ReceiveHandler(self):
           self.merge()
           self.serialObject.recieve_serial()
           self.serialObject.Manager_ofRecievedData()
           self.merge()
