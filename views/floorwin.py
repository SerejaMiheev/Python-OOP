from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from repository.floorrepository import FloorRepository
from views.flooraddwin import FloorAddDialog
from views.floordialog import Ui_Floor


class FloorDialog(QDialog):
    def __init__(self):
        super(FloorDialog, self).__init__()
        self.floor_repository = FloorRepository()
        self.initUI()

    def initUI(self):
        self.ui = Ui_Floor()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnWidth(1, 155)
        self.ui.tableWidget.setColumnWidth(2, 145)
        self.ui.tableWidget.setSelectionBehavior(1)
        self.ui.tableWidget.setSelectionMode(1)

        self.ui.pushButton.clicked.connect(self.click_add)
        self.ui.pushButton_2.clicked.connect(self.click_del)
        self.ui.pushButton_4.clicked.connect(self.click_edit)
        self.ui.pushButton_5.clicked.connect(self.click_cancel)

        floors = self.floor_repository.get_floors()
        self.ui.tableWidget.setRowCount(len(floors))
        row = 0
        for i in floors:
            num_floor = QTableWidgetItem(str(i['number']))
            num_floor.setData(1000, i['id'])
            num_floor.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 0, num_floor)
            count_r = QTableWidgetItem(str(len(i['rooms'])))
            count_r.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 1, count_r)
            count_c = QTableWidgetItem(str(len(i['cameras'])))
            count_c.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 2, count_c)
            row += 1

    def click_add(self):
        f_dict = {'id': -1, 'number': -1, 'rooms': -1, 'cameras': -1}
        self.floor_repository.set_dict(f_dict)
        floor_add = FloorAddDialog(self.floor_repository)
        if (floor_add.exec()):
            floor_d = self.floor_repository.get_dict()
            count_row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(count_row + 1)
            num_floor = QTableWidgetItem(str(floor_d['number']))
            num_floor.setData(1000, floor_d['id'])
            num_floor.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 0, num_floor)
            if(floor_d['rooms'] != -1):
                count_r = QTableWidgetItem(str(len(floor_d['rooms'])))
            else:
                count_r = QTableWidgetItem(str(0))
            count_r.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 1, count_r)
            if(floor_d['cameras'] != -1):
                count_c = QTableWidgetItem(str(len(floor_d['cameras'])))
            else:
                count_c = QTableWidgetItem(str(0))
            count_c.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 2, count_c)

    def click_del(self):
        del_list = self.ui.tableWidget.selectedItems()
        if (len(del_list)):
            del_d = {'id': del_list[0].data(1000)}
            self.floor_repository.del_floor(del_d)
            self.ui.tableWidget.removeRow(del_list[0].row())

    def click_edit(self):
        edit_list = self.ui.tableWidget.selectedItems()
        if (len(edit_list)):
            select_row = self.ui.tableWidget.currentRow()
            edit_d = self.floor_repository.get_floor({'id': edit_list[0].data(1000)})
            self.floor_repository.set_dict(edit_d)
            floor_edit = FloorAddDialog(self.floor_repository)
            if (floor_edit.exec()):
                floor_d = self.floor_repository.get_dict()
                num_floor = QTableWidgetItem(str(floor_d['number']))
                num_floor.setData(1000, floor_d['id'])
                num_floor.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(select_row, 0, num_floor)
                count_r = QTableWidgetItem(str(len(floor_d['rooms'])))
                count_r.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(select_row, 1, count_r)
                count_c = QTableWidgetItem(str(len(floor_d['cameras'])))
                count_c.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(select_row, 2, count_c)

    def click_cancel(self):
        self.accept()
