from Styling import *
from mergeDataWithGui import mergeDataWithGui
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.CubeSat = mergeDataWithGui()

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
