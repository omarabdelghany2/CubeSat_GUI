import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QGroupBox
from PyQt6.QtGui import QFont, QColor, QPixmap
from AdcsTab import Ui_Form

class Styling_AdcsTab(QWidget,Ui_Form):
    def __init__(self):
        super(Styling_AdcsTab, self).__init__()
        self.setupUi(self)