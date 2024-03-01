from serialClass import *
from Styling_MainTab import Styling_MainTab
from Styling_EpsTab import Styling_EpsTab
from Styling_AdcsTab import Styling_AdcsTab
from Styling_CommTab import Styling_CommTab
from Styling_PayTab import Styling_PayTab
from PositionWindow import MapWindow
import base64




class mergeDataWithGui (QtCore.QThread):
    def __init__(self):
           #constructor #1)object from styling.py (stylingObject)
                        #2)object from serial.func.py (serialObject)
                        #3)connect the the recieve button with its handler
            QtCore.QThread.__init__(self)
            self.running = True
                        
            self.serialObject = SerialClass()
            self.Styling_MainTab_Object=Styling_MainTab()
            self.Styling_EpsTab_Object=Styling_EpsTab()
            self.Styling_AdcsTab_Object=Styling_AdcsTab()
            self.Styling_CommTab_Object=Styling_CommTab()
            self.Styling_PayTab_Object=Styling_PayTab()
            self.PositionWindow_Object=MapWindow()

            self.Styling_MainTab_Object.Receiving_Connect_pushButton.clicked.connect(self.ReceiveHandler)
            self.Styling_MainTab_Object.Receiving_Disconnect_pushButton.clicked.connect(self.Disconnect)
            self.Styling_PayTab_Object.pushButton_upload.clicked.connect(self.imaageRequest)
    def Connect(self):
            self.serialObject.baudRateRx = int(self.Styling_MainTab_Object.BaudRateRX_TextEdit.currentText())
            self.serialObject.comPortRx  = self.Styling_MainTab_Object.ReceivingComPort_comboBox.currentText()
    def ConnectImage(self):
            self.serialObject.baudRateTx = int(self.Styling_MainTab_Object.BaudRateTX_TextEdit.currentText())
            self.serialObject.comPortTx  = self.Styling_PayTab_Object.comboBox_Port.currentText()


    def run(self):
          while self.running:
              if(self.serialObject.capture_event and (not(self.serialObject.MergeEvent)) ):       
                     # put the image in gui ----->>
                     image = base64.b64decode(self.serialObject.EncodedImage_Bytes)
                     with open('decoded_imag_Serial.jpg', 'wb') as f:
                            f.write(image)
                     self.serialObject.capture_event = False
                     self.serialObject.MergeEvent = True
                     pixmap = QPixmap("decoded_imag_Serial.jpg")
                     self.Styling_PayTab_Object.label_Photo.setPixmap(pixmap)
              elif(self.serialObject.MergeEvent and (not(self.serialObject.capture_event)) ) :
                                   #1)#here merge data as the next line an example
              #first get the data from gui (baudrate ,comport)
                     self.serialObject.MergeEvent= False
                     self.Styling_MainTab_Object.ReceivingWindow_textEdit.setOverwriteMode(True)
                     self.Styling_MainTab_Object.ReceivingWindow_textEdit.overwriteMode()
                     # put the data in gui ----->>
                     self.Styling_MainTab_Object.ReceivingWindow_textEdit.append(self.serialObject.serial_data)
                     
                     timestamp_str = str(self.serialObject.Time)  # Convert to string
                     year = timestamp_str[0:4]
                     month = timestamp_str[4:6]
                     day = timestamp_str[6:8]
                     hour = timestamp_str[8:10]
                     minute = timestamp_str[10:12]
                     second = timestamp_str[12:14]
                     
                     formatted_time = f"{day}/{month}/{year}/{hour}/{minute}/{second}"
                     
                     self.Styling_MainTab_Object.Time_LineEdit.setText(formatted_time)


                     self.Styling_MainTab_Object.BatteryVolt_LineEdit_3.setText(str(self.serialObject.voltage))
                     self.Styling_MainTab_Object.Current_LineEdit_3.setText(str(self.serialObject.current))
                     self.Styling_MainTab_Object.Current33_LineEdit_3.setText(str(self.serialObject.current3_3))
                     self.Styling_MainTab_Object.Current5_LineEdit_3.setText(str(self.serialObject.current_5))

                     ##adding the oreintatio to 3dMODEL_______________________________________

                     self.Styling_MainTab_Object.Model.yawangle = self.serialObject.GyroZ
                     self.Styling_MainTab_Object.Model.pitchangle = self.serialObject.GyroX  ##we have aproplem here try to detect
                     self.Styling_MainTab_Object.Model.rollangle = self.serialObject.GyroY
                     self.Styling_MainTab_Object.Model.update()

                     # Set the mode and color based on the value
                     if self.serialObject.OBC == 1:
                            # Set color to green
                            self.Styling_MainTab_Object.OBC_LineEdit_3.setStyleSheet("background-color: green;")
                     else:
                            
                            # Set color to red
                            self.Styling_MainTab_Object.OBC_LineEdit_3.setStyleSheet("background-color: red;")

                     if self.serialObject.ADCS == 1:
                            
                            self.Styling_MainTab_Object.ADCS_LineEdit_3.setStyleSheet("background-color: green;")
                     else:
                           
                            self.Styling_MainTab_Object.ADCS_LineEdit_3.setStyleSheet("background-color: red;")

                     if self.serialObject.Payload == 1:
                            
                            self.Styling_MainTab_Object.Payload_LineEdit_3.setStyleSheet("background-color: green;")
                     else:
                           
                            self.Styling_MainTab_Object.Payload_LineEdit_3.setStyleSheet("background-color: red;")

                     if self.serialObject.comm_antennas == 1:
                            
                            self.Styling_MainTab_Object.AntennaStatus_LineEdit_3.setStyleSheet("background-color: green;")
                     else:
                            
                            self.Styling_MainTab_Object.AntennaStatus_LineEdit_3.setStyleSheet("background-color: red;")

                     if self.serialObject.Temp == 1:
                           
                            self.Styling_MainTab_Object.TempSensorStatus_LineEdit_3.setStyleSheet("background-color: green;")
                     else:
                            
                            self.Styling_MainTab_Object.TempSensorStatus_LineEdit_3.setStyleSheet("background-color: red;")

                     if self.serialObject.solar1 == 1:
                           
                            self.Styling_MainTab_Object.SolarStatus1_LineEdit_3.setStyleSheet("background-color: green;")
                     else:
                            
                            self.Styling_MainTab_Object.SolarStatus1_LineEdit_3.setStyleSheet("background-color: red;")

                     if self.serialObject.solar2 == 1:
                            
                            self.Styling_MainTab_Object.SolarStatus2_LineEdit_3.setStyleSheet("background-color: green;")
                     else:
                           
                            self.Styling_MainTab_Object.SolarStatus2_LineEdit_3.setStyleSheet("background-color: red;")

                     if self.serialObject.solar3 == 1:
                            
                            self.Styling_MainTab_Object.SolarStatus3_LineEdit_3.setStyleSheet("background-color: green;")
                     else:
                            
                            self.Styling_MainTab_Object.SolarStatus3_LineEdit_3.setStyleSheet("background-color: red;")

                     if self.serialObject.solar4 == 1:
                            
                            self.Styling_MainTab_Object.SolarStatus4_LineEdit_3.setStyleSheet("background-color: green;")
                     else:
                            
                            self.Styling_MainTab_Object.SolarStatus4_LineEdit_3.setStyleSheet("background-color: red;")


                     # self.Styling_MainTab_Object.position_Pushbutton.clicked.connect(self.show_location)
                     # self.map = None
                     
                     
                     self.Styling_MainTab_Object.position_Pushbutton.clicked.connect(self.PositionWindow_Object.show_map)



              #-----------------------------------------------------------------------
                            #varaibles of the ebs tab                                       -->>>EBSTAB
                            
                     self.Styling_EpsTab_Object.lineEdit_VBAT.setText(str(self.serialObject.voltage))
                     self.Styling_EpsTab_Object.lineEdit_C33.setText(str(self.serialObject.current3_3))
                     self.Styling_EpsTab_Object.lineEdit_C5.setText(str(self.serialObject.current_5))
                     self.Styling_EpsTab_Object.lineEdit_EPST.setText(str(self.serialObject.EbsTemp))

                     if self.serialObject.solar1 == 1:
                            self.Styling_EpsTab_Object.lineEdit_SOLAR1.setStyleSheet("background-color: green;")
                     else:
                            self.Styling_EpsTab_Object.lineEdit_SOLAR1.setStyleSheet("background-color: red;")
                     
                     if self.serialObject.solar2 == 1:
                            self.Styling_EpsTab_Object.lineEdit_SOLAR2.setStyleSheet("background-color: green;")
                     else:
                            self.Styling_EpsTab_Object.lineEdit_SOLAR2.setStyleSheet("background-color: red;")

                     if self.serialObject.solar3 == 1:
                            self.Styling_EpsTab_Object.lineEdit_SOLAR3.setStyleSheet("background-color: green;")
                     else:
                            self.Styling_EpsTab_Object.lineEdit_SOLAR3.setStyleSheet("background-color: red;")

                     if self.serialObject.solar4 == 1:
                            self.Styling_EpsTab_Object.lineEdit_SOLAR4.setStyleSheet("background-color: green;")
                     else:
                            self.Styling_EpsTab_Object.lineEdit_SOLAR4.setStyleSheet("background-color: red;")
                     
                     if self.serialObject.OBC == 1:
                            self.Styling_EpsTab_Object.lineEdit_OBC.setStyleSheet("background-color: green;")
                     else:
                            self.Styling_EpsTab_Object.lineEdit_OBC.setStyleSheet("background-color: red;")
                     
                     if self.serialObject.comm_antennas == 1:
                            self.Styling_EpsTab_Object.lineEdit_COMM.setStyleSheet("background-color: green;")
                     else:
                            self.Styling_EpsTab_Object.lineEdit_COMM.setStyleSheet("background-color: red;")

                     if self.serialObject.ADCS == 1:
                            self.Styling_EpsTab_Object.lineEdit_ADCS.setStyleSheet("background-color: green;")
                     else:

                            self.Styling_EpsTab_Object.lineEdit_ADCS.setStyleSheet("background-color: red;")

                     if self.serialObject.Payload == 1:
                            self.Styling_EpsTab_Object.lineEdit_PAYLOAD.setStyleSheet("background-color: green;")
                     else:
                            self.Styling_EpsTab_Object.lineEdit_PAYLOAD.setStyleSheet("background-color: red;")          
                            
                     if self.serialObject.MotorX == 1:
                            self.Styling_EpsTab_Object.lineEdit_MOTZ.setStyleSheet("background-color: green;")
                     else:
                            self.Styling_EpsTab_Object.lineEdit_MOTZ.setStyleSheet("background-color: red;")
                     
                     if self.serialObject.MotorY == 1:
                            self.Styling_EpsTab_Object.lineEdit_MOTY.setStyleSheet("background-color: green;")
                     else:
                            self.Styling_EpsTab_Object.lineEdit_MOTY.setStyleSheet("background-color: red;")

                     if self.serialObject.MotorZ == 1:
                            self.Styling_EpsTab_Object.lineEdit_MOTX.setStyleSheet("background-color: green;")
                     else:
                            self.Styling_EpsTab_Object.lineEdit_MOTX.setStyleSheet("background-color: red;")

                     if self.serialObject.BatteryHeater == 1:
                            self.Styling_EpsTab_Object.lineEdit_HBAT.setStyleSheet("background-color: green;")
                     else:
                            self.Styling_EpsTab_Object.lineEdit_HBAT.setStyleSheet("background-color: red;") 



              #-----------------------------------------------------------------------
                            #varaibles of the ADCS tab                                       -->>>ADCSTAB
                            
                     self.Styling_AdcsTab_Object.lineEdit_lux1.setText(str(self.serialObject.lux1))
                     self.Styling_AdcsTab_Object.lineEdit_lux2.setText(str(self.serialObject.lux2))
                     self.Styling_AdcsTab_Object.lineEdit_lux3.setText(str(self.serialObject.lux3))
                     self.Styling_AdcsTab_Object.lineEdit_lux4.setText(str(self.serialObject.lux4))
                                                                                           
                     self.Styling_AdcsTab_Object.lineEdit_acc1.setText(str(self.serialObject.AccX))
                     self.Styling_AdcsTab_Object.lineEdit_acc2.setText(str(self.serialObject.AccY))
                     self.Styling_AdcsTab_Object.lineEdit_acc3.setText(str(self.serialObject.AccZ)) 

                     self.Styling_AdcsTab_Object.lineEdit_qyro1.setText(str(self.serialObject.GyroX))
                     self.Styling_AdcsTab_Object.lineEdit_qyro2.setText(str(self.serialObject.GyroY))
                     self.Styling_AdcsTab_Object.lineEdit_qyro3.setText(str(self.serialObject.GyroZ)) 

                     self.Styling_AdcsTab_Object.lineEdit_magn1.setText(str(self.serialObject.MagnX))
                     self.Styling_AdcsTab_Object.lineEdit_magn2.setText(str(self.serialObject.MagnY))
                     self.Styling_AdcsTab_Object.lineEdit_magn3.setText(str(self.serialObject.MagnZ))

                     self.Styling_AdcsTab_Object.lineEdit_ADCSTemp.setText(str(self.serialObject.ADSC_Temp))

                     self.Styling_AdcsTab_Object.lineEdit_Kalman1.setText(str(self.serialObject.Kalmanx))
                     self.Styling_AdcsTab_Object.lineEdit_Kalman2.setText(str(self.serialObject.Kalmany))
                     self.Styling_AdcsTab_Object.lineEdit_Kalman3.setText(str(self.serialObject.Kalmanz)) 

                     self.Styling_AdcsTab_Object.lineEdit_NumberSatellite.setText(str(self.serialObject.Number_of_Satellites))
                     self.Styling_AdcsTab_Object.lineEdit_GPS.setText(str(self.serialObject.GPS_d3_Fix))  

                     self.Styling_AdcsTab_Object.lineEdit_Longitude.setText(str(self.serialObject.Longitude))
                     self.Styling_AdcsTab_Object.lineEdit_Latitude.setText(str(self.serialObject.Latitude))
                     self.Styling_AdcsTab_Object.lineEdit_Altitude.setText(str(self.serialObject.Altitude))  



              #-----------------------------------------------------------------------
                            #varaibles of the COMM tab                    -->>>COMM TAB
                     
                     self.Styling_CommTab_Object.lineEdit_TxBand.setText(str(self.serialObject.PowerTx))
                     self.Styling_CommTab_Object.lineEdit_RxP.setText(str(self.serialObject.PowerRx))
                     self.Styling_CommTab_Object.lineEdit_Mod.setText(str(self.serialObject.ModulationScheme)) 
                     self.Styling_CommTab_Object.lineEdit_Freq.setText(str(self.serialObject.Freq))
                     self.Styling_CommTab_Object.lineEdit_FreqBand.setText(str(self.serialObject.FreqBand))
                     self.Styling_CommTab_Object.lineEdit_Rb.setText(str(self.serialObject.DataRate))

                     if self.serialObject.COMM_Status == 1:
                            self.Styling_CommTab_Object.lineEdit_Status.setText(str("ON"))
                            self.Styling_CommTab_Object.lineEdit_Status.setStyleSheet("background-color: green;")
                     else:
                            self.Styling_CommTab_Object.lineEdit_Status.setText(str("OFF"))
                            self.Styling_CommTab_Object.lineEdit_Status.setStyleSheet("background-color: red;")    
                     
              self.msleep(50)
              
       
              
#     def show_location(self):
#         # Replace these dummy latitude and longitude values with actual values from self.serialObject
#         latitude = 30.077240026307322
#         longitude = 31.018226442330036
#         self.show_map(latitude, longitude)
              

#     def show_map(self, latitude, longitude):
#         self.map = folium.Map(location=[latitude, longitude], zoom_start=10) 
#         folium.Marker([latitude, longitude], popup='Smart Village').add_to(self.map)
#         self.map.save('map.html')

#         webbrowser.open_new_tab('map.html')

#     def show_message_box(self, title, message):
#         msg_box = QMessageBox()
#         msg_box.setWindowTitle(title)
#         msg_box.setText(message)
#         msg_box.exec()
    
    def imaageRequest(self):
       self.ConnectImage()
       self.serialObject.capture_event = True
       self.serialObject.MergeEvent = False
       self.serialObject.running = True
       self.serialObject.start()

    def ReceiveHandler(self):
       self.serialObject.capture_event = False
       self.serialObject.MergeEvent = True
       self.Connect()
       self.serialObject.running = True
       self.serialObject.start()



    def Disconnect(self) :
       print('Disconnect Pressed')
       self.serialObject.running = False

