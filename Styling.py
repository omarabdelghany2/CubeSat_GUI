import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QGroupBox
from PyQt6.QtGui import QFont, QColor, QPixmap
from MainTab import Ui1_Form
from AdcsTab import Ui3_Form
from EpsTab import Ui2_Form

class Styling_EpsTab(QWidget,Ui2_Form):
    def __init__(self):
        super(Styling_EpsTab, self).__init__()
        self.setupUi(self)


class Styling_AdcsTab(QWidget,Ui3_Form):
    def __init__(self):
        super(Styling_AdcsTab, self).__init__()
        self.setupUi(self)

class Styling_MainTab(QWidget,Ui1_Form):
    def __init__(self):
        super(Styling_MainTab, self).__init__()
        self.setupUi(self)
