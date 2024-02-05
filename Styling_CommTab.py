import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QGroupBox
from PyQt6.QtGui import QFont, QColor, QPixmap
from COMM_Tab import Ui_Form

class Styling_CommTab(QWidget,Ui_Form):
    def __init__(self):
        super(Styling_CommTab, self).__init__()
        self.setupUi(self)