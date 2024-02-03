import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget
from mainWindow import MainWindow






def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
