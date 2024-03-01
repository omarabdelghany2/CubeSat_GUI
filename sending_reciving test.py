import sys
import serial
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QTimer


class MainWindow(QMainWindow):
    def __init__(self):
        self.serial_connection = serial.Serial('COM5', 115200)
        super().__init__()
        self.setup_ui()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.read_data_frame)
        self.timer.start(1000)  # Read data every 1000 milliseconds (1 second)
    
    def setup_ui(self):
        self.setWindowTitle("Serial Data Reader")
        self.setGeometry(100, 100, 300, 200)
        
        self.button = QPushButton("Send Data and Wait", self)
        self.button.setGeometry(50, 50, 200, 50)
        self.button.clicked.connect(self.send_data_and_wait)
    
    def read_data_frame(self):
        # Example reading data from COM5 into a list
        self.serial_data = self.serial_connection.readline().strip()
        # Print the received data
        print("Received Data Frame: {}".format(self.serial_data))
        self.received_data = self.serial_data.split(b',')
        return self.serial_data
    
    def send_data_and_wait(self):
        # Example sending data and waiting for response
        self.serial_connection.write(b'PIC')
        response = self.serial_connection.readline().strip()
        print("Received: {}".format(response))
        return response

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
