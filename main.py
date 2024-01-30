import sys
from mergeDataWithGui import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel,  QTabWidget, QWidget

# steps for clean code
    #1) object from merge data with gui  ->done
    #2) call sytlingObject.show         
    #3)while {
        #  loop over merge func}

def main ():
   app = QApplication(sys.argv)
   #1)
   CubeSat=mergeDataWithGui()
   #2)
   CubeSat.StylingObject.show()  
   #3)
    
  # while (1)
   #  CubeSat.merge()
   sys.exit(app.exec())



if __name__ == "__main__":
   main()

 
   
