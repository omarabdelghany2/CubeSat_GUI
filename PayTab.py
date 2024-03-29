# Form implementation generated from reading ui file 'pay.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class Ui_Form(object):
    def setupUi(self, Form):
        #list of Ports for RX & TX combobox
        Ports = ["COM5","COM2","COM3","COM4","COM1","COM6","COM7","COM8","COM9","/dev/cu.usbserial-1120","/dev/cu.usbserial-120"]
        Form.setObjectName("Form")
        Form.resize(1103, 865)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_Photo = QtWidgets.QLabel(parent=Form)
        self.label_Photo.setText("")
        self.label_Photo.setObjectName("label_Photo")
        self.label_Photo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_Photo, 0, 0, 1, 1)
        self.pushButton_upload = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_upload.setFont(font)
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.pushButton_upload.setStyleSheet('''
            QPushButton {
                background-color: #333333;
                color: rgb(64, 224, 208);
                border: 2px solid rgb(64, 224, 208);
                border-radius: 10px; /* Rounded border */
                min-width: 200px;
                min-height: 50px;
            }
            QPushButton:hover {
                background-color: green; /* Change the background color on hover */
                color: rgb(0, 0, 0); /* Change the font color on hover */
                border-color: rgb(255, 255, 255); /* Change the border color on hover */
            }
        ''')
        self.gridLayout.addWidget(self.pushButton_upload, 2, 0, 1, 1)
        self.comboBox_Port = QtWidgets.QComboBox(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_Port.setFont(font)
        self.comboBox_Port.setObjectName("comboBox_Port")
        self.gridLayout.addWidget(self.comboBox_Port, 1, 0, 1, 1)
        self.comboBox_Port.addItems(Ports)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_upload.setText(_translate("Form", "Capture"))
