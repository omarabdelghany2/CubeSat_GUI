
from PyQt6.QtWidgets import  QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl


class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Map Window")
        

        # Create web engine view to display the map
        self.webview = QWebEngineView()
        self.setCentralWidget(self.webview)
        

    def show_map(self):
        
        self.latitude = 30.077240026307322
        self.longitude = 31.018226442330036
        map_url = f"https://maps.google.com/?q={self.latitude},{self.longitude}&ll={self.latitude},{self.longitude}&z=3"
        # map_url = f"https://www.openstreetmap.org/?mlat={self.latitude}&mlon={self.longitude}#map=15/{self.latitude}/{self.longitude}"
        self.webview.setUrl(QUrl(map_url))
        
        self.show()
        
    

