from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from controllers.cameracontroller import CameraController
from controllers.floorcontroller import FloorController
from controllers.roomcontroller import RoomController
from views.flooradd import Ui_FloorAdd

LastStateRole = QtCore.Qt.UserRole


class FloorAddDialog(QDialog):
    def __init__(self, floor_controller: FloorController):
        super(FloorAddDialog, self).__init__()
        self.floor_controller = floor_controller
        self.floor_d = floor_controller.get_dict()
        self.camera_controller = CameraController()
        self.room_controller = RoomController()
        self.initUI()

    def initUI(self):
        self.ui = Ui_FloorAdd()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnWidth(0, 170)
        self.ui.tableWidget_2.setColumnWidth(0, 170)
        self.ui.lineEdit.setValidator(QtGui.QIntValidator(-50, 300))
        self.ui.tableWidget.setSelectionBehavior(1)
        self.ui.tableWidget.setSelectionMode(1)
        self.r_list = []
        self.c_list = []

        if (self.floor_d['number'] != -1):
            self.ui.lineEdit.setText(str(self.floor_d['number']))

        if ((self.floor_d['rooms'] == -1) or (len(self.floor_d['rooms'])) == 0):
            rooms = self.room_controller.get_rooms()
            self.ui.tableWidget.setRowCount(len(rooms))
            row = 0
            for i in rooms:
                num_r = QTableWidgetItem(str(i['number']))
                num_r.setData(1000, i['id'])
                num_r.setFlags(QtCore.Qt.ItemIsUserCheckable |
                                   QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(row, 0, num_r)
                num_r.setCheckState(QtCore.Qt.Unchecked)
                row += 1

        else:
            rooms = self.room_controller.get_rooms()
            self.ui.tableWidget.setRowCount(len(rooms))
            row = 0
            for i in rooms:
                num_r = QTableWidgetItem(str(i['number']))
                num_r.setData(1000, i['id'])
                num_r.setFlags(QtCore.Qt.ItemIsUserCheckable |
                               QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(row, 0, num_r)
                if (self.floor_d['rooms'].count(i['id'])):
                    num_r.setCheckState(QtCore.Qt.Checked)
                    self.r_list.append(i['id'])
                else:
                    num_r.setCheckState(QtCore.Qt.Unchecked)
                row += 1

        if ((self.floor_d['cameras'] == -1) or (len(self.floor_d['cameras']) == 0)):
            cameras = self.camera_controller.get_cameras()
            self.ui.tableWidget_2.setRowCount(len(cameras))
            row = 0
            for i in cameras:
                c_column = QTableWidgetItem(str(i['id']))
                c_column.setFlags(QtCore.Qt.ItemIsUserCheckable |
                                  QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget_2.setItem(row, 0, c_column)
                c_column.setCheckState(QtCore.Qt.Unchecked)
                row += 1
        else:
            cameras = self.camera_controller.get_cameras()
            self.ui.tableWidget_2.setRowCount(len(cameras))
            row = 0
            for i in cameras:
                c_column = QTableWidgetItem(str(i['id']))
                c_column.setFlags(QtCore.Qt.ItemIsUserCheckable |
                                  QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget_2.setItem(row, 0, c_column)
                if (self.floor_d['cameras'].count(i['id'])):
                    c_column.setCheckState(QtCore.Qt.Checked)
                    self.c_list.append(i['id'])
                else:
                    c_column.setCheckState(QtCore.Qt.Unchecked)
                row += 1

        self.ui.tableWidget.cellChanged.connect(self.onCellChangedR)
        self.ui.tableWidget_2.cellChanged.connect(self.onCellChangedC)
        self.ui.pushButton.clicked.connect(self.click_ok)
        self.ui.pushButton_2.clicked.connect(self.click_cancel)

    def onCellChangedR(self, row, column):
        item = self.ui.tableWidget.item(row, column)
        lastState = item.data(LastStateRole)
        currentState = item.checkState()
        if currentState != lastState:
            if currentState == QtCore.Qt.Checked:
                self.r_list.append(item.data(1000))
            else:
                self.r_list.remove(item.data(1000))
            item.setData(LastStateRole, currentState)

    def onCellChangedC(self, row, column):
        item = self.ui.tableWidget_2.item(row, column)
        lastState = item.data(LastStateRole)
        currentState = item.checkState()
        if currentState != lastState:
            if currentState == QtCore.Qt.Checked:
                self.c_list.append(int(item.text()))
            else:
                self.c_list.remove(int(item.text()))
            item.setData(LastStateRole, currentState)

    def click_ok(self):
        c_number = self.ui.lineEdit.text()
        if (self.floor_d['id'] == -1):
            if (len(c_number)):
                self.floor_d['number'] = c_number
                if (len(self.r_list)):
                    self.floor_d['rooms'] = self.r_list
                else:
                    self.floor_d['rooms'] = -1
                if (len(self.c_list)):
                    self.floor_d['cameras'] = self.c_list
                else:
                    self.floor_d['cameras'] = -1
                f_d = self.floor_controller.new_floor(self.floor_d)
                self.floor_controller.set_dict(f_d)
                self.accept()
        else:
            if (len(c_number)):
                self.floor_d['number'] = c_number
                if (len(self.r_list)):
                    self.floor_d['rooms'] = self.r_list
                else:
                    self.floor_d['rooms'] = -1
                if (len(self.c_list)):
                    self.floor_d['cameras'] = self.c_list
                else:
                    self.floor_d['cameras'] = -1
                self.floor_controller.update_floor(self.floor_d)
                self.floor_controller.set_dict(self.floor_d)
                self.accept()

    def click_cancel(self):
        self.reject()
