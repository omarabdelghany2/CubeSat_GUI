
from PyQt6.QtGui import QPixmap,QPainter
from PyQt6.QtWidgets import  QWidget
from PyQt6.QtGui import QPixmap
from AdcsTab import Ui_Form
import os

class Styling_AdcsTab(QWidget,Ui_Form):
    def __init__(self):
        super(Styling_AdcsTab, self).__init__()
        self.setupUi(self)
         # Set the size of the widget
        self.setGeometry(100, 100, 800, 600)

        background_file_path = os.path.join("images/background.jpg")

        # Load the background image
        self.background_image = QPixmap(background_file_path)
        self.setStyleSheet("""
        QTabWidget::pane {
            border: 2px solid rgb(64, 224, 208); /* Border around the entire QTabWidget */
            background-color: #333333; /* Background color of the QTabWidget */
        }
        QTabBar::tab {
            background-color: #444444; /* Background color of each tab */
            color: white; /* Text color of each tab */
        }
        QTabBar::tab:selected {
            background-color: rgb(64, 224, 208); /* Background color of the selected tab */
        }
    """)

    def paintEvent(self, event):
        painter = QPainter(self)
        
        # Draw the background image
        painter.drawPixmap(self.rect(), self.background_image)