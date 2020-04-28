from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from controllers.cameracontroller import CameraController
from controllers.equipmentcontroller import EquipmentController
from controllers.roomcontroller import RoomController
from controllers.typecontroller import TypeController
from views.roomadd import Ui_RoomAdd

LastStateRole = QtCore.Qt.UserRole


class RoomAddDialog(QDialog):
    def __init__(self, room_controller: RoomController):
        super(RoomAddDialog, self).__init__()
        self.room_controller = room_controller
        self.room_d = room_controller.get_dict()
        self.equipment_controller = EquipmentController()
        self.camera_controller = CameraController()
        self.type_controller = TypeController()
        self.initUI()

    def initUI(self):
        self.ui = Ui_RoomAdd()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnWidth(0, 170)
        self.ui.tableWidget_2.setColumnWidth(0, 170)
        self.ui.lineEdit.setValidator(QtGui.QIntValidator(1,90000))
        self.ui.tableWidget.setSelectionBehavior(1)
        self.ui.tableWidget.setSelectionMode(1)
        self.eq_list = []
        self.c_list = []

        if (self.room_d['number'] != -1):
            self.ui.lineEdit.setText(str(self.room_d['number']))

        if ((self.room_d['equipments'] == -1) or (len(self.room_d['equipments'])) == 0):
            equipments = self.equipment_controller.get_equipments()
            self.ui.tableWidget.setRowCount(len(equipments))
            row = 0
            for i in equipments:
                eq_column = QTableWidgetItem(
                    self.type_controller.get_t(i['eq_type'])['type_of_equipment'] + ".  Кол-во: " + str(i['count']))
                eq_column.setData(1000, i['id'])
                eq_column.setFlags(QtCore.Qt.ItemIsUserCheckable |
                                   QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(row, 0, eq_column)
                eq_column.setCheckState(QtCore.Qt.Unchecked)
                row += 1

        else:
            equipments = self.equipment_controller.get_equipments()
            self.ui.tableWidget.setRowCount(len(equipments))
            row = 0
            for i in equipments:
                eq_column = QTableWidgetItem(
                    self.type_controller.get_t(i['eq_type'])['type_of_equipment'] + ".  Кол-во: " + str(i['count']))
                eq_column.setData(1000, i['id'])
                eq_column.setFlags(QtCore.Qt.ItemIsUserCheckable |
                                   QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(row, 0, eq_column)
                if (self.room_d['equipments'].count(i['id'])):
                    eq_column.setCheckState(QtCore.Qt.Checked)
                    self.eq_list.append(i['id'])
                else:
                    eq_column.setCheckState(QtCore.Qt.Unchecked)
                row += 1

        if ((self.room_d['cameras'] == -1) or (len(self.room_d['cameras']) == 0)):
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
                if (self.room_d['cameras'].count(i['id'])):
                    c_column.setCheckState(QtCore.Qt.Checked)
                    self.c_list.append(i['id'])
                else:
                    c_column.setCheckState(QtCore.Qt.Unchecked)
                row += 1

        self.ui.tableWidget.cellChanged.connect(self.onCellChangedEq)
        self.ui.tableWidget_2.cellChanged.connect(self.onCellChangedC)
        self.ui.pushButton.clicked.connect(self.click_ok)
        self.ui.pushButton_2.clicked.connect(self.click_cancel)

    def onCellChangedEq(self, row, column):
        item = self.ui.tableWidget.item(row, column)
        lastState = item.data(LastStateRole)
        currentState = item.checkState()
        if currentState != lastState:
            if currentState == QtCore.Qt.Checked:
                self.eq_list.append(item.data(1000))
            else:
                self.eq_list.remove(item.data(1000))
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
        if (self.room_d['id'] == -1):
            if (len(c_number)):
                self.room_d['number'] = c_number
                if (len(self.eq_list)):
                    self.room_d['equipments'] = self.eq_list
                else:
                    self.room_d['equipments'] = -1
                if (len(self.c_list)):
                    self.room_d['cameras'] = self.c_list
                else:
                    self.room_d['cameras'] = -1
                r_d = self.room_controller.new_room(self.room_d)
                self.room_controller.set_dict(r_d)
                self.accept()
        else:
            if (len(c_number)):
                self.room_d['number'] = c_number
                if (len(self.eq_list)):
                    self.room_d['equipments'] = self.eq_list
                else:
                    self.room_d['equipments'] = -1
                if (len(self.c_list)):
                    self.room_d['cameras'] = self.c_list
                else:
                    self.room_d['cameras'] = -1
                self.room_controller.update_room(self.room_d)
                self.room_controller.set_dict(self.room_d)
                self.accept()

    def click_cancel(self):
        self.reject()
