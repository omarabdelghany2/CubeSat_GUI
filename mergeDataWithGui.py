from serialClass import *
from Styling import *

#todo in this file just youmna need to fill #3 in merge fucntion
class mergeDataWithGui ():

    def __init__(self):
           #constructor #1)object from styling.py (stylingObject)->youmna
                       #2)object from serial.func.py (serialObject) ->omar
            self.serialObject=serialClass()
            self.StylingObject=Styling()
                
        
        
        
        #create func merge 
        # 1)serialobect.receiveserial()  ->done
        # 2)serialobject.manager()       ->done
        # 3)styulingoBJECT.LINEDIT1.SETDATA(Serialobject.sola1) do this to all data u want to show in gui  ->being done
        
    def merge(self):
            #1)
            self.serialObject.recieve_serial()
            #2)
            self.serialObject.Manager_ofRecievedData()
            #3)#here merge data as the next line an example  --> youmna do this             #note youmna u have to replace line edit with qlabel because line Edit can be changed by the user in gui
            self.StylingObject.SolarStatus1_LineEdit.setText(str(self.serialObject.solar1))
    
