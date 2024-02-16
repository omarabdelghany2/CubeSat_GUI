import os
import sys 
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QLabel
from mergeDataWithGui import mergeDataWithGui



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        icon_file_path = os.path.join(os.path.dirname(__file__), "images", "swiftAct.ico")

        self.setWindowTitle("Ground Station")
        self.setWindowIcon(QIcon(icon_file_path))

        self.CubeSat = mergeDataWithGui()
        self.CubeSat.start()

        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)

        self.main_tab = self.CubeSat.Styling_MainTab_Object
        self.eps_tab = self.CubeSat.Styling_EpsTab_Object
        self.adcs_tab = self.CubeSat.Styling_AdcsTab_Object
        self.comm_tab = self.CubeSat.Styling_CommTab_Object

        self.tabs.addTab(self.main_tab, "MainWindow_tab")
        self.tabs.addTab(self.eps_tab, "EPS_tab")
        self.tabs.addTab(self.adcs_tab, "ADCS_tab")
        self.tabs.addTab(self.comm_tab, "COMM_tab")
        self.tabs.setStyleSheet("""
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

        self.tabs.currentChanged.connect(self.tab_changed)
    def tab_changed(self, index):
        if index == 0:
            self.main_tab.show()
            self.adcs_tab.hide()
            self.eps_tab.hide()
            self.comm_tab.hide()
        elif index == 1:
            self.eps_tab.show()
            self.main_tab.hide()
            self.adcs_tab.hide()
            self.comm_tab.hide()
        elif index == 2:
            self.adcs_tab.show()
            self.eps_tab.hide()
            self.main_tab.hide()
            self.comm_tab.hide()
        elif index == 3:
            self.comm_tab.show()
            self.eps_tab.hide()
            self.main_tab.hide()
            self.adcs_tab.hide()


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())



if __name__ == "__main__":
     main()
