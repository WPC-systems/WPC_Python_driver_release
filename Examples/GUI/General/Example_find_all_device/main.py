from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QTableWidget,QApplication
from PyQt5.QtCore import Qt
from UI_design.Ui_example_GUI_Broadcasts import Ui_MainWindow 
from qasync import QEventLoop, asyncSlot
import sys
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc 
import os

COLUMN_WIDTH = 160  

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()  
        QTableWidget.__init__(self)
 
        ## UI initialize
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## Trademark path
        trademark_path = os.getcwd() + "\Material\WPC_trademark.jpg" 
        self.ui.lb_trademark.setPixmap(QtGui.QPixmap(trademark_path))

        ## Initialize table 
        self.initiBroadcastTable()

        ## Define button callback events
        self.ui.btn_broadcast.clicked.connect(self.broadcastEvent)
        
        ## Connect to network device
        dev.connect() 

        ## Get Python driver version
        str_ = f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}'
        print(str_)
  
        ## Initialize list
        self.broadcast_list=[]

    def initiBroadcastTable(self): ## 5 for columns
        for i in range(5):
            self.ui.tableWidget_brst.setColumnWidth(i, COLUMN_WIDTH)
        self.ui.tableWidget_brst.setStyleSheet("selection-background-color: #217536;")

    def loaddata(self): 
        row=0
        self.ui.tableWidget_brst.setRowCount(len(self.broadcast_list))
        for i in self.broadcast_list:
            self.ui.tableWidget_brst.setItem(row, 0, QtWidgets.QTableWidgetItem(i["ip"]))
            self.ui.tableWidget_brst.setItem(row, 1, QtWidgets.QTableWidgetItem(i["submask"]))
            self.ui.tableWidget_brst.setItem(row, 2, QtWidgets.QTableWidgetItem(i["mac"]))
            self.ui.tableWidget_brst.setItem(row, 3, QtWidgets.QTableWidgetItem(i["model"]))
            self.ui.tableWidget_brst.setItem(row, 4, QtWidgets.QTableWidgetItem(i["firmware_ver"]))
            row=row+1
        QApplication.restoreOverrideCursor()
        
    @asyncSlot()      
    async def broadcastEvent(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.broadcast_list.clear()
        self.ui.tableWidget_brst.setRowCount(0) 
        broadcast_info = await dev.brst_getDeviceInfo()
        device_amount = len(broadcast_info) 
        for i in range (device_amount):
            ip      = broadcast_info[i][0]
            submask = broadcast_info[i][1]
            mac     = broadcast_info[i][2]
            model_version = broadcast_info[i][3]
            str_list      = model_version.split('_')
            model   = str_list[0]
            version = str_list[1] 
            self.broadcast_list.append({'ip': ip , 'submask': submask, 'mac':mac, 'model': model, 'firmware_ver': version}) 
        self.loaddata()

    def closeEvent(self, event):
        ## Disconnect network device
        dev.disconnect()
        ## Release device handle
        dev.close()

def main(): 
    app = QtWidgets.QApplication([])
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop) 
    WPC_main_ui = MainWindow()
    WPC_main_ui.show() 
    with loop: 
        loop.run_forever()

if __name__ == "__main__":
    ## Create device handle
    dev = pywpc.Broadcaster()
    main()
   
 