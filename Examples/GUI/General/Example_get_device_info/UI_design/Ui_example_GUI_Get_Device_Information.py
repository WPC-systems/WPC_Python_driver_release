# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Chunglee_WPC\WPC_Python_driver_release\Examples\GUI\General\Example_get_device_info\UI_design\example_GUI_Get_Device_Information.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(909, 804)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_trademark = QtWidgets.QLabel(self.centralwidget)
        self.lb_trademark.setGeometry(QtCore.QRect(10, 0, 81, 81))
        self.lb_trademark.setText("")
        self.lb_trademark.setPixmap(QtGui.QPixmap("d:\\Chunglee_WPC\\WPC_Python_driver_release\\Examples\\GUI\\General\\Example_get_device_info\\UI_design\\../Material/WPC_trademark.jpg"))
        self.lb_trademark.setScaledContents(True)
        self.lb_trademark.setObjectName("lb_trademark")
        self.lb_rights = QtWidgets.QLabel(self.centralwidget)
        self.lb_rights.setGeometry(QtCore.QRect(90, 0, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lb_rights.setFont(font)
        self.lb_rights.setObjectName("lb_rights")
        self.lb_declare = QtWidgets.QLabel(self.centralwidget)
        self.lb_declare.setGeometry(QtCore.QRect(90, 80, 791, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.lb_declare.setFont(font)
        self.lb_declare.setObjectName("lb_declare")
        self.groupBox_connection = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_connection.setGeometry(QtCore.QRect(230, 120, 471, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_connection.setFont(font)
        self.groupBox_connection.setAutoFillBackground(True)
        self.groupBox_connection.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_connection.setFlat(False)
        self.groupBox_connection.setObjectName("groupBox_connection")
        self.btn_connect = QtWidgets.QPushButton(self.groupBox_connection)
        self.btn_connect.setGeometry(QtCore.QRect(170, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_connect.setFont(font)
        self.btn_connect.setStyleSheet("QPushButton {\n"
"    background-color: rgb(61, 79, 99);\n"
"    border-radius : 5px;\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(52, 137, 235);\n"
"}")
        self.btn_connect.setObjectName("btn_connect")
        self.btn_disconnect = QtWidgets.QPushButton(self.groupBox_connection)
        self.btn_disconnect.setGeometry(QtCore.QRect(270, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_disconnect.setFont(font)
        self.btn_disconnect.setStyleSheet("QPushButton {\n"
"    background-color: rgb(61, 79, 99);\n"
"    border-radius : 5px;\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(52, 137, 235);\n"
"}")
        self.btn_disconnect.setObjectName("btn_disconnect")
        self.lb_ip_cnt = QtWidgets.QLabel(self.groupBox_connection)
        self.lb_ip_cnt.setGeometry(QtCore.QRect(10, 30, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lb_ip_cnt.setFont(font)
        self.lb_ip_cnt.setObjectName("lb_ip_cnt")
        self.lineEdit_ipConnect = QtWidgets.QLineEdit(self.groupBox_connection)
        self.lineEdit_ipConnect.setGeometry(QtCore.QRect(50, 30, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_ipConnect.setFont(font)
        self.lineEdit_ipConnect.setObjectName("lineEdit_ipConnect")
        self.lb_led = QtWidgets.QLabel(self.groupBox_connection)
        self.lb_led.setGeometry(QtCore.QRect(410, 20, 51, 51))
        self.lb_led.setText("")
        self.lb_led.setPixmap(QtGui.QPixmap("d:\\Chunglee_WPC\\WPC_Python_driver_release\\Examples\\GUI\\General\\Example_get_device_info\\UI_design\\../../../../../Material/WPC_Led_green.png"))
        self.lb_led.setScaledContents(True)
        self.lb_led.setObjectName("lb_led")
        self.groupBox_driverInfo = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_driverInfo.setGeometry(QtCore.QRect(230, 220, 381, 371))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_driverInfo.setFont(font)
        self.groupBox_driverInfo.setAutoFillBackground(True)
        self.groupBox_driverInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_driverInfo.setFlat(False)
        self.groupBox_driverInfo.setObjectName("groupBox_driverInfo")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_driverInfo)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 21, 115, 341))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_ip = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lb_ip.setFont(font)
        self.lb_ip.setObjectName("lb_ip")
        self.verticalLayout.addWidget(self.lb_ip)
        self.lb_sbk = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lb_sbk.setFont(font)
        self.lb_sbk.setObjectName("lb_sbk")
        self.verticalLayout.addWidget(self.lb_sbk)
        self.lb_serialnumber = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lb_serialnumber.setFont(font)
        self.lb_serialnumber.setObjectName("lb_serialnumber")
        self.verticalLayout.addWidget(self.lb_serialnumber)
        self.lb_mac = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lb_mac.setFont(font)
        self.lb_mac.setObjectName("lb_mac")
        self.verticalLayout.addWidget(self.lb_mac)
        self.lb_model = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lb_model.setFont(font)
        self.lb_model.setObjectName("lb_model")
        self.verticalLayout.addWidget(self.lb_model)
        self.lb_firmware = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lb_firmware.setFont(font)
        self.lb_firmware.setObjectName("lb_firmware")
        self.verticalLayout.addWidget(self.lb_firmware)
        self.lb_rtc = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lb_rtc.setFont(font)
        self.lb_rtc.setObjectName("lb_rtc")
        self.verticalLayout.addWidget(self.lb_rtc)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_driverInfo)
        self.layoutWidget1.setGeometry(QtCore.QRect(160, 10, 161, 371))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_ip = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_ip.setFont(font)
        self.lineEdit_ip.setText("")
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.verticalLayout_2.addWidget(self.lineEdit_ip)
        self.lineEdit_sbk = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_sbk.setFont(font)
        self.lineEdit_sbk.setText("")
        self.lineEdit_sbk.setObjectName("lineEdit_sbk")
        self.verticalLayout_2.addWidget(self.lineEdit_sbk)
        self.lineEdit_serialNum = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_serialNum.setFont(font)
        self.lineEdit_serialNum.setText("")
        self.lineEdit_serialNum.setObjectName("lineEdit_serialNum")
        self.verticalLayout_2.addWidget(self.lineEdit_serialNum)
        self.lineEdit_mac = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_mac.setFont(font)
        self.lineEdit_mac.setText("")
        self.lineEdit_mac.setObjectName("lineEdit_mac")
        self.verticalLayout_2.addWidget(self.lineEdit_mac)
        self.lineEdit_model = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_model.setFont(font)
        self.lineEdit_model.setText("")
        self.lineEdit_model.setObjectName("lineEdit_model")
        self.verticalLayout_2.addWidget(self.lineEdit_model)
        self.lineEdit_version = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_version.setFont(font)
        self.lineEdit_version.setText("")
        self.lineEdit_version.setObjectName("lineEdit_version")
        self.verticalLayout_2.addWidget(self.lineEdit_version)
        self.lineEdit_rtc = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_rtc.setFont(font)
        self.lineEdit_rtc.setText("")
        self.lineEdit_rtc.setObjectName("lineEdit_rtc")
        self.verticalLayout_2.addWidget(self.lineEdit_rtc)
        self.btn_deviceInfo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_deviceInfo.setGeometry(QtCore.QRect(630, 230, 161, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.btn_deviceInfo.setFont(font)
        self.btn_deviceInfo.setStyleSheet("QPushButton {\n"
"    background-color: rgb(61, 79, 99);\n"
"    border-radius : 5px;\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(52, 137, 235);\n"
"}")
        self.btn_deviceInfo.setObjectName("btn_deviceInfo")
        self.groupBox_errormessage = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_errormessage.setGeometry(QtCore.QRect(140, 620, 591, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_errormessage.setFont(font)
        self.groupBox_errormessage.setAutoFillBackground(True)
        self.groupBox_errormessage.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_errormessage.setFlat(False)
        self.groupBox_errormessage.setObjectName("groupBox_errormessage")
        self.lb_err = QtWidgets.QLabel(self.groupBox_errormessage)
        self.lb_err.setGeometry(QtCore.QRect(10, 30, 561, 41))
        self.lb_err.setText("")
        self.lb_err.setObjectName("lb_err")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 909, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Example - Get device information"))
        self.lb_rights.setText(_translate("MainWindow", " Ⓒ2022 WPC Systems Ltd. All right reserved"))
        self.lb_declare.setText(_translate("MainWindow", "This is example for getting device information from WPC DAQ Device."))
        self.groupBox_connection.setTitle(_translate("MainWindow", "Connection Setting"))
        self.btn_connect.setText(_translate("MainWindow", "Connect"))
        self.btn_disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.lb_ip_cnt.setText(_translate("MainWindow", "IP : "))
        self.lineEdit_ipConnect.setText(_translate("MainWindow", "192.168.5.79"))
        self.groupBox_driverInfo.setTitle(_translate("MainWindow", "Device Information"))
        self.lb_ip.setText(_translate("MainWindow", "IP"))
        self.lb_sbk.setText(_translate("MainWindow", "Submask"))
        self.lb_serialnumber.setText(_translate("MainWindow", "S/N"))
        self.lb_mac.setText(_translate("MainWindow", "MAC"))
        self.lb_model.setText(_translate("MainWindow", "Model"))
        self.lb_firmware.setText(_translate("MainWindow", "Firmware ver."))
        self.lb_rtc.setText(_translate("MainWindow", "RTC"))
        self.btn_deviceInfo.setText(_translate("MainWindow", "Get Device Info"))
        self.groupBox_errormessage.setTitle(_translate("MainWindow", "Error Messages"))
