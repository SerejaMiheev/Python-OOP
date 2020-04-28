from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from controllers.roomcontroller import RoomController
from views.roomaddwin import RoomAddDialog
from views.roomsdialog import Ui_Rooms


class RoomsDialog(QDialog):
    def __init__(self):
        super(RoomsDialog, self).__init__()
        self.room_controller = RoomController()
        self.initUI()

    def initUI(self):
        self.ui = Ui_Rooms()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnWidth(0, 268)
        self.ui.tableWidget.setSelectionBehavior(1)
        self.ui.tableWidget.setSelectionMode(1)

        self.ui.pushButton.clicked.connect(self.click_add)
        self.ui.pushButton_2.clicked.connect(self.click_edit)
        self.ui.pushButton_3.clicked.connect(self.click_del)
        self.ui.pushButton_4.clicked.connect(self.click_cancel)

        rooms = self.room_controller.get_rooms()
        self.ui.tableWidget.setRowCount(len(rooms))
        row = 0
        for i in rooms:
            num_room = QTableWidgetItem(str(i['number']))
            num_room.setData(1000, i['id'])
            num_room.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 0, num_room)
            row += 1

    def click_add(self):
        r_dict = {'id': -1, 'number': -1, 'equipments': -1, 'cameras': -1}
        self.room_controller.set_dict(r_dict)
        room_add = RoomAddDialog(self.room_controller)
        if (room_add.exec()):
            room_d = self.room_controller.get_dict()
            count_row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(count_row + 1)
            num_room = QTableWidgetItem(str(room_d['number']))
            num_room.setData(1000, room_d['id'])
            num_room.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 0, num_room)

    def click_edit(self):
        edit_list = self.ui.tableWidget.selectedItems()
        if (len(edit_list)):
            select_row = self.ui.tableWidget.currentRow()
            edit_d = self.room_controller.get_room({'id': edit_list[0].data(1000)})
            self.room_controller.set_dict(edit_d)
            room_edit = RoomAddDialog(self.room_controller)
            if (room_edit.exec()):
                room_d = self.room_controller.get_dict()
                num_room = QTableWidgetItem(str(room_d['number']))
                num_room.setData(1000, room_d['id'])
                num_room.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(select_row, 0, num_room)

    def click_del(self):
        del_list = self.ui.tableWidget.selectedItems()
        if (len(del_list)):
            del_d = {'id': del_list[0].data(1000)}
            self.room_controller.del_room(del_d)
            self.ui.tableWidget.removeRow(del_list[0].row())

    def click_cancel(self):
        self.accept()