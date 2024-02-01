from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel,  QTabWidget, QWidget
from PyQt6.QtGui import QPixmap
from MainTab import Ui_MainWindow

class Styling(QMainWindow, Ui_MainWindow):
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

       