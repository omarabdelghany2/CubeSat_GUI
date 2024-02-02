from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel,  QTabWidget, QWidget
from PyQt6.QtGui import QPixmap
from EPS_TAB import Ui_MainWindow


#->> create the class of the EPS_TAB
#->> edit this class for the specific orders

class Styling_EBSTab(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Set up a QLabel to display the background image
        self.background_label = QLabel(self)
        self.update_background_size()  # Set initial size
        pixmap = QPixmap("background.jpg")  # Replace with the path to your image
        self.background_label.setPixmap(pixmap)

        # Make the label a child of the central widget
        self.background_label.setParent(self.centralWidget())

        # Set a lower stacking order for the background_label
        self.background_label.lower()

    def update_background_size(self):
        # Update the size of the background_label to cover the entire window
        self.background_label.setGeometry(0, 0, self.width(), self.height())

    def resizeEvent(self, event):
        # Override the resizeEvent to update the background size when the window is resized
        self.update_background_size()

        self.setStyleSheet('''

                           
            QPushButton#Sending_Connect_pushButton{
                background-color: #1a5e73; color: white;
            }
            QPushButton#Sending_Disconnect_pushButton{
                background-color: #1a5e73; color: white;
            }
                           
            QPushButton#Receiving_Connect_pushButton{
                background-color: #1a5e73; color: white;
            }
            QPushButton#Receiving_Disconnect_pushButton{
                background-color: #1a5e73; color: white;
            }
                           
            QLabel#BaudRateTX_label{
                 font-size: 16px; font-family: Arial; font-weight: bold; color: white;          
            }
            QLabel#SendingComPort_label{
                 font-size: 16px; font-family: Arial; font-weight: bold;color: white;          
            }
            QLabel#SendCommands_label{
                 font-size: 16px; font-family: Arial; font-weight: bold;color: white;          
            }
                           
            QLabel#BaudRateRX_label{
                 font-size: 16px; font-family: Arial; font-weight: bold;color: white;          
            }
            QLabel#ReceivingComPort_label{
                 font-size: 16px; font-family: Arial; font-weight: bold;color: white;          
            }
            QLabel#ReceivingTerminal_label{
                 font-size: 16px; font-family: Arial; font-weight: bold;color: white;          
            }


            QGroupBox#MainBatteryStatus_groupBox{
                 font-size: 20px; font-family: Arial; font-weight: bold;color: white;          
            }            
            QLabel#BatteryVolt_label{
                 font-size: 16px; font-family: Arial; font-weight: bold;color: white;          
            }
            QLabel#Current_label{
                 font-size: 16px; font-family: Arial; font-weight: bold;color: white;          
            }
            QLabel#Current33_label{
                 font-size: 16px; font-family: Arial; font-weight: bold;color: white;          
            }
            QLabel#Current5_label{
                 font-size: 16px; font-family: Arial; font-weight: bold;color: white;          
            }


            QGroupBox#SubsystemStatus_groupBox{
                 font-size: 20px; font-family: Arial; font-weight: bold;color: white;          
            }            
            QLabel#OBCStatus_label{
                 font-size: 16px; font-family: Arial; font-weight: bold;color: white;          
            }
            QLabel#ADCSStatus_label{
                 font-size: 16px; font-family: Arial; font-weight: bold;color: white;          
            }
            QLabel#PayloadStatus_label{
                 font-size: 16px; font-family: Arial; font-weight: bold;color: white;          
            }
            QLabel#CommAntennaStatus_label{
                 font-size: 16px; font-family: Arial; font-weight: bold;color: white;          
            }
            
            
            QGroupBox#ExternalSystemStatus_groupBox{
                 font-size: 20px; font-family: Arial; font-weight: bold;color: white;          
            }
            QLabel#TempSensorStatus_label{
                 font-size: 16px; font-family: Arial; font-weight: bold;color: white;          
            }
            QLabel#SolarStatus1_label{
                 font-size: 16px; font-family: Arial; font-weight: bold;color: white;          
            }
            QLabel#SolarStatus2_label{
                 font-size: 16px; font-family: Arial; font-weight: bold;color: white;          
            }
            QLabel#SolarStatus3_label{
                 font-size: 16px; font-family: Arial; font-weight: bold;color: white;          
            }
            QLabel#SolarStatus4_label_2{
                 font-size: 16px; font-family: Arial; font-weight: bold;color: white;          
            }
                           
            QLabel#Time_label{
                 font-size: 20px; font-family: Arial; font-weight: bold;color: white;          
            }

           QTabWidget {
                background-color: #00FFFFFF;
            }

            QTabBar::tab {
                background: #00FFFFFF;
                color: white;
                border: 2px solid white;
                padding: 8px;
                margin: 1px;
            }

            QTabBar::tab:selected {
                background: #769eab;
            } 
                                                    
        ''')
