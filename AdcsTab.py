# Form implementation generated from reading ui file 'AdcsTab.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui3_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1336, 888)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupbox_Accelerometer = QtWidgets.QGroupBox(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.groupbox_Accelerometer.setFont(font)
        self.groupbox_Accelerometer.setObjectName("groupbox_Accelerometer")
        self.layoutWidget_2 = QtWidgets.QWidget(parent=self.groupbox_Accelerometer)
        self.layoutWidget_2.setGeometry(QtCore.QRect(14, 50, 391, 211))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_acc2 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_acc2.setFont(font)
        self.label_acc2.setObjectName("label_acc2")
        self.gridLayout_4.addWidget(self.label_acc2, 1, 0, 1, 1)
        self.lineEdit_acc1 = QtWidgets.QLineEdit(parent=self.layoutWidget_2)
        self.lineEdit_acc1.setReadOnly(True)
        self.lineEdit_acc1.setObjectName("lineEdit_acc1")
        self.gridLayout_4.addWidget(self.lineEdit_acc1, 0, 1, 1, 1)
        self.lineEdit_acc2 = QtWidgets.QLineEdit(parent=self.layoutWidget_2)
        self.lineEdit_acc2.setReadOnly(True)
        self.lineEdit_acc2.setObjectName("lineEdit_acc2")
        self.gridLayout_4.addWidget(self.lineEdit_acc2, 1, 1, 1, 1)
        self.label_acc3 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_acc3.setFont(font)
        self.label_acc3.setObjectName("label_acc3")
        self.gridLayout_4.addWidget(self.label_acc3, 2, 0, 1, 1)
        self.lineEdit_acc3 = QtWidgets.QLineEdit(parent=self.layoutWidget_2)
        self.lineEdit_acc3.setReadOnly(True)
        self.lineEdit_acc3.setObjectName("lineEdit_acc3")
        self.gridLayout_4.addWidget(self.lineEdit_acc3, 2, 1, 1, 1)
        self.label_acc1 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_acc1.setFont(font)
        self.label_acc1.setObjectName("label_acc1")
        self.gridLayout_4.addWidget(self.label_acc1, 0, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.groupbox_Accelerometer)
        self.groupbox_LDRs = QtWidgets.QGroupBox(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.groupbox_LDRs.setFont(font)
        self.groupbox_LDRs.setObjectName("groupbox_LDRs")
        self.widget = QtWidgets.QWidget(parent=self.groupbox_LDRs)
        self.widget.setGeometry(QtCore.QRect(10, 50, 425, 199))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_lux1 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_lux1.setFont(font)
        self.label_lux1.setObjectName("label_lux1")
        self.horizontalLayout.addWidget(self.label_lux1)
        self.lineEdit_lux1 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_lux1.setReadOnly(True)
        self.lineEdit_lux1.setObjectName("lineEdit_lux1")
        self.horizontalLayout.addWidget(self.lineEdit_lux1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_lux2 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_lux2.setFont(font)
        self.label_lux2.setObjectName("label_lux2")
        self.horizontalLayout_2.addWidget(self.label_lux2)
        self.lineEdit_lux2 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_lux2.setReadOnly(True)
        self.lineEdit_lux2.setObjectName("lineEdit_lux2")
        self.horizontalLayout_2.addWidget(self.lineEdit_lux2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_lux3 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_lux3.setFont(font)
        self.label_lux3.setObjectName("label_lux3")
        self.horizontalLayout_4.addWidget(self.label_lux3)
        self.lineEdit_lux3 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_lux3.setReadOnly(True)
        self.lineEdit_lux3.setObjectName("lineEdit_lux3")
        self.horizontalLayout_4.addWidget(self.lineEdit_lux3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_lux4 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_lux4.setFont(font)
        self.label_lux4.setObjectName("label_lux4")
        self.horizontalLayout_3.addWidget(self.label_lux4)
        self.lineEdit_lux4 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_lux4.setReadOnly(True)
        self.lineEdit_lux4.setObjectName("lineEdit_lux4")
        self.horizontalLayout_3.addWidget(self.lineEdit_lux4)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.groupbox_LDRs)
        self.groupbox_gyro_sensor = QtWidgets.QGroupBox(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.groupbox_gyro_sensor.setFont(font)
        self.groupbox_gyro_sensor.setObjectName("groupbox_gyro_sensor")
        self.layoutWidget_3 = QtWidgets.QWidget(parent=self.groupbox_gyro_sensor)
        self.layoutWidget_3.setGeometry(QtCore.QRect(14, 50, 391, 211))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_gyro1 = QtWidgets.QLabel(parent=self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_gyro1.setFont(font)
        self.label_gyro1.setObjectName("label_gyro1")
        self.gridLayout_5.addWidget(self.label_gyro1, 0, 0, 1, 1)
        self.lineEdit_qyro1 = QtWidgets.QLineEdit(parent=self.layoutWidget_3)
        self.lineEdit_qyro1.setReadOnly(True)
        self.lineEdit_qyro1.setObjectName("lineEdit_qyro1")
        self.gridLayout_5.addWidget(self.lineEdit_qyro1, 0, 1, 1, 1)
        self.label_gyro2 = QtWidgets.QLabel(parent=self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_gyro2.setFont(font)
        self.label_gyro2.setObjectName("label_gyro2")
        self.gridLayout_5.addWidget(self.label_gyro2, 1, 0, 1, 1)
        self.lineEdit_qyro2 = QtWidgets.QLineEdit(parent=self.layoutWidget_3)
        self.lineEdit_qyro2.setReadOnly(True)
        self.lineEdit_qyro2.setObjectName("lineEdit_qyro2")
        self.gridLayout_5.addWidget(self.lineEdit_qyro2, 1, 1, 1, 1)
        self.label_gyro3 = QtWidgets.QLabel(parent=self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_gyro3.setFont(font)
        self.label_gyro3.setObjectName("label_gyro3")
        self.gridLayout_5.addWidget(self.label_gyro3, 2, 0, 1, 1)
        self.lineEdit_qyro3 = QtWidgets.QLineEdit(parent=self.layoutWidget_3)
        self.lineEdit_qyro3.setReadOnly(True)
        self.lineEdit_qyro3.setObjectName("lineEdit_qyro3")
        self.gridLayout_5.addWidget(self.lineEdit_qyro3, 2, 1, 1, 1)
        self.horizontalLayout_5.addWidget(self.groupbox_gyro_sensor)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupbox_Magnetometer = QtWidgets.QGroupBox(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.groupbox_Magnetometer.setFont(font)
        self.groupbox_Magnetometer.setObjectName("groupbox_Magnetometer")
        self.layoutWidget_4 = QtWidgets.QWidget(parent=self.groupbox_Magnetometer)
        self.layoutWidget_4.setGeometry(QtCore.QRect(14, 50, 391, 211))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget_4)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_magn3 = QtWidgets.QLabel(parent=self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_magn3.setFont(font)
        self.label_magn3.setObjectName("label_magn3")
        self.gridLayout_6.addWidget(self.label_magn3, 2, 0, 1, 1)
        self.lineEdit_magn3 = QtWidgets.QLineEdit(parent=self.layoutWidget_4)
        self.lineEdit_magn3.setReadOnly(True)
        self.lineEdit_magn3.setObjectName("lineEdit_magn3")
        self.gridLayout_6.addWidget(self.lineEdit_magn3, 2, 1, 1, 1)
        self.lineEdit_magn1 = QtWidgets.QLineEdit(parent=self.layoutWidget_4)
        self.lineEdit_magn1.setReadOnly(True)
        self.lineEdit_magn1.setObjectName("lineEdit_magn1")
        self.gridLayout_6.addWidget(self.lineEdit_magn1, 0, 1, 1, 1)
        self.label_magn2 = QtWidgets.QLabel(parent=self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_magn2.setFont(font)
        self.label_magn2.setObjectName("label_magn2")
        self.gridLayout_6.addWidget(self.label_magn2, 1, 0, 1, 1)
        self.lineEdit_magn2 = QtWidgets.QLineEdit(parent=self.layoutWidget_4)
        self.lineEdit_magn2.setReadOnly(True)
        self.lineEdit_magn2.setObjectName("lineEdit_magn2")
        self.gridLayout_6.addWidget(self.lineEdit_magn2, 1, 1, 1, 1)
        self.label_magn1 = QtWidgets.QLabel(parent=self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_magn1.setFont(font)
        self.label_magn1.setObjectName("label_magn1")
        self.gridLayout_6.addWidget(self.label_magn1, 0, 0, 1, 1)
        self.horizontalLayout_6.addWidget(self.groupbox_Magnetometer)
        self.groupbox_ADCS = QtWidgets.QGroupBox(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.groupbox_ADCS.setFont(font)
        self.groupbox_ADCS.setObjectName("groupbox_ADCS")
        self.layoutWidget_5 = QtWidgets.QWidget(parent=self.groupbox_ADCS)
        self.layoutWidget_5.setGeometry(QtCore.QRect(14, 50, 391, 211))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.layoutWidget_5)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_ADCSTemp = QtWidgets.QLabel(parent=self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ADCSTemp.setFont(font)
        self.label_ADCSTemp.setObjectName("label_ADCSTemp")
        self.gridLayout_7.addWidget(self.label_ADCSTemp, 0, 0, 1, 1)
        self.lineEdit_ADCSTemp = QtWidgets.QLineEdit(parent=self.layoutWidget_5)
        self.lineEdit_ADCSTemp.setReadOnly(True)
        self.lineEdit_ADCSTemp.setObjectName("lineEdit_ADCSTemp")
        self.gridLayout_7.addWidget(self.lineEdit_ADCSTemp, 0, 1, 1, 1)
        self.horizontalLayout_6.addWidget(self.groupbox_ADCS)
        self.groupbox_Kalman = QtWidgets.QGroupBox(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.groupbox_Kalman.setFont(font)
        self.groupbox_Kalman.setObjectName("groupbox_Kalman")
        self.layoutWidget_6 = QtWidgets.QWidget(parent=self.groupbox_Kalman)
        self.layoutWidget_6.setGeometry(QtCore.QRect(14, 50, 391, 211))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.layoutWidget_6)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_kalman1 = QtWidgets.QLabel(parent=self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_kalman1.setFont(font)
        self.label_kalman1.setObjectName("label_kalman1")
        self.gridLayout_8.addWidget(self.label_kalman1, 0, 0, 1, 1)
        self.lineEdit_Kalman1 = QtWidgets.QLineEdit(parent=self.layoutWidget_6)
        self.lineEdit_Kalman1.setReadOnly(True)
        self.lineEdit_Kalman1.setObjectName("lineEdit_Kalman1")
        self.gridLayout_8.addWidget(self.lineEdit_Kalman1, 0, 1, 1, 1)
        self.label_kalman2 = QtWidgets.QLabel(parent=self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_kalman2.setFont(font)
        self.label_kalman2.setObjectName("label_kalman2")
        self.gridLayout_8.addWidget(self.label_kalman2, 1, 0, 1, 1)
        self.lineEdit_Kalman2 = QtWidgets.QLineEdit(parent=self.layoutWidget_6)
        self.lineEdit_Kalman2.setReadOnly(True)
        self.lineEdit_Kalman2.setObjectName("lineEdit_Kalman2")
        self.gridLayout_8.addWidget(self.lineEdit_Kalman2, 1, 1, 1, 1)
        self.label_kalman3 = QtWidgets.QLabel(parent=self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_kalman3.setFont(font)
        self.label_kalman3.setObjectName("label_kalman3")
        self.gridLayout_8.addWidget(self.label_kalman3, 2, 0, 1, 1)
        self.lineEdit_Kalman3 = QtWidgets.QLineEdit(parent=self.layoutWidget_6)
        self.lineEdit_Kalman3.setObjectName("lineEdit_Kalman3")
        self.gridLayout_8.addWidget(self.lineEdit_Kalman3, 2, 1, 1, 1)
        self.horizontalLayout_6.addWidget(self.groupbox_Kalman)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 0, 1, 2)
        self.groupbox_Satelites = QtWidgets.QGroupBox(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.groupbox_Satelites.setFont(font)
        self.groupbox_Satelites.setObjectName("groupbox_Satelites")
        self.layoutWidget_9 = QtWidgets.QWidget(parent=self.groupbox_Satelites)
        self.layoutWidget_9.setGeometry(QtCore.QRect(14, 50, 621, 211))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.layoutWidget_9)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.lineEdit_GPS = QtWidgets.QLineEdit(parent=self.layoutWidget_9)
        self.lineEdit_GPS.setReadOnly(True)
        self.lineEdit_GPS.setObjectName("lineEdit_GPS")
        self.gridLayout_11.addWidget(self.lineEdit_GPS, 1, 1, 1, 1)
        self.lineEdit_NumberSatellite = QtWidgets.QLineEdit(parent=self.layoutWidget_9)
        self.lineEdit_NumberSatellite.setReadOnly(True)
        self.lineEdit_NumberSatellite.setObjectName("lineEdit_NumberSatellite")
        self.gridLayout_11.addWidget(self.lineEdit_NumberSatellite, 0, 1, 1, 1)
        self.label_GPS = QtWidgets.QLabel(parent=self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_GPS.setFont(font)
        self.label_GPS.setObjectName("label_GPS")
        self.gridLayout_11.addWidget(self.label_GPS, 1, 0, 1, 1)
        self.label_NumberSatellite = QtWidgets.QLabel(parent=self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_NumberSatellite.setFont(font)
        self.label_NumberSatellite.setObjectName("label_NumberSatellite")
        self.gridLayout_11.addWidget(self.label_NumberSatellite, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupbox_Satelites, 2, 0, 1, 1)
        self.groupbox_Position = QtWidgets.QGroupBox(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.groupbox_Position.setFont(font)
        self.groupbox_Position.setObjectName("groupbox_Position")
        self.layoutWidget_8 = QtWidgets.QWidget(parent=self.groupbox_Position)
        self.layoutWidget_8.setGeometry(QtCore.QRect(14, 50, 621, 211))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.layoutWidget_8)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_Longitude = QtWidgets.QLabel(parent=self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Longitude.setFont(font)
        self.label_Longitude.setObjectName("label_Longitude")
        self.gridLayout_10.addWidget(self.label_Longitude, 0, 0, 1, 1)
        self.lineEdit_Longitude = QtWidgets.QLineEdit(parent=self.layoutWidget_8)
        self.lineEdit_Longitude.setReadOnly(True)
        self.lineEdit_Longitude.setObjectName("lineEdit_Longitude")
        self.gridLayout_10.addWidget(self.lineEdit_Longitude, 0, 1, 1, 1)
        self.label_Latitude = QtWidgets.QLabel(parent=self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Latitude.setFont(font)
        self.label_Latitude.setObjectName("label_Latitude")
        self.gridLayout_10.addWidget(self.label_Latitude, 1, 0, 1, 1)
        self.lineEdit_Latitude = QtWidgets.QLineEdit(parent=self.layoutWidget_8)
        self.lineEdit_Latitude.setReadOnly(True)
        self.lineEdit_Latitude.setObjectName("lineEdit_Latitude")
        self.gridLayout_10.addWidget(self.lineEdit_Latitude, 1, 1, 1, 1)
        self.label_Altitude = QtWidgets.QLabel(parent=self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Altitude.setFont(font)
        self.label_Altitude.setObjectName("label_Altitude")
        self.gridLayout_10.addWidget(self.label_Altitude, 2, 0, 1, 1)
        self.lineEdit_Altitude = QtWidgets.QLineEdit(parent=self.layoutWidget_8)
        self.lineEdit_Altitude.setReadOnly(True)
        self.lineEdit_Altitude.setObjectName("lineEdit_Altitude")
        self.gridLayout_10.addWidget(self.lineEdit_Altitude, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupbox_Position, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupbox_Accelerometer.setTitle(_translate("Form", "Accelerometer"))
        self.label_acc2.setText(_translate("Form", "Acc Y"))
        self.label_acc3.setText(_translate("Form", "Acc Z"))
        self.label_acc1.setText(_translate("Form", "Acc X"))
        self.groupbox_LDRs.setTitle(_translate("Form", "LDRs"))
        self.label_lux1.setText(_translate("Form", "Lux 1"))
        self.label_lux2.setText(_translate("Form", "Lux 2"))
        self.label_lux3.setText(_translate("Form", "Lux 3"))
        self.label_lux4.setText(_translate("Form", "Lux 3"))
        self.groupbox_gyro_sensor.setTitle(_translate("Form", "Gyro Sensor"))
        self.label_gyro1.setText(_translate("Form", "Gyro X"))
        self.label_gyro2.setText(_translate("Form", "Gyro Y"))
        self.label_gyro3.setText(_translate("Form", "Gyro Z"))
        self.groupbox_Magnetometer.setTitle(_translate("Form", "Magnetometer"))
        self.label_magn3.setText(_translate("Form", "Magn Z"))
        self.label_magn2.setText(_translate("Form", "Magn Y"))
        self.label_magn1.setText(_translate("Form", "Magn X"))
        self.groupbox_ADCS.setTitle(_translate("Form", "ADCS Temp"))
        self.label_ADCSTemp.setText(_translate("Form", "ADCS Temp"))
        self.groupbox_Kalman.setTitle(_translate("Form", "Kalman Filter"))
        self.label_kalman1.setText(_translate("Form", "Kalman X"))
        self.label_kalman2.setText(_translate("Form", "Kalman Y"))
        self.label_kalman3.setText(_translate("Form", "Kalman Z"))
        self.groupbox_Satelites.setTitle(_translate("Form", "Satellites and GPS"))
        self.label_GPS.setText(_translate("Form", "GPS d3 Fix"))
        self.label_NumberSatellite.setText(_translate("Form", "Number of Satellite"))
        self.groupbox_Position.setTitle(_translate("Form", "Position Coordinates"))
        self.label_Longitude.setText(_translate("Form", "Longitude"))
        self.label_Latitude.setText(_translate("Form", "Latitude"))
        self.label_Altitude.setText(_translate("Form", "Altitude"))