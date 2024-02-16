
from PyQt6.QtGui import QPixmap,QPainter
from PyQt6.QtWidgets import  QWidget
from PyQt6.QtGui import QPixmap
from MainTab import Ui_Form  # Assuming this is generated by PyQt6-uic
import os
class Styling_MainTab(QWidget, Ui_Form):
    def __init__(self):
        super(Styling_MainTab, self).__init__()
        self.setupUi(self)
        
        
        # Set the size of the widget
        self.setGeometry(100, 100, 800, 600)

        background_file_path = os.path.join("images/background.jpg")
        # Load the background image
        self.background_image = QPixmap(background_file_path)

    def paintEvent(self, event):
        painter = QPainter(self)
        
        # Draw the background image
        painter.drawPixmap(self.rect(), self.background_image)
    
    