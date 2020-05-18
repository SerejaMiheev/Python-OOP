from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from repository.equipmentrepository import EquipmentRepository
from repository.typerepository import TypeRepository
from views.equipmentsaddwin import EquipmentsAddDialog
from views.equipmentsdialog import Ui_Equipments


class EquipmentsDialog(QDialog):
    def __init__(self):
        super(EquipmentsDialog, self).__init__()
        self.equipment_repository = EquipmentRepository()
        self.type_repository = TypeRepository()
        self.initUI()

    def initUI(self):
        self.ui = Ui_Equipments()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnWidth(0, 205)
        self.ui.tableWidget.setColumnWidth(1, 70)
        self.ui.tableWidget.setSelectionBehavior(1)
        self.ui.tableWidget.setSelectionMode(1)

        self.ui.pushButton.clicked.connect(self.click_add)
        self.ui.pushButton_2.clicked.connect(self.click_edit)
        self.ui.pushButton_3.clicked.connect(self.click_del)
        self.ui.pushButton_4.clicked.connect(self.click_cancel)

        equipment = self.equipment_repository.get_equipments()
        self.ui.tableWidget.setRowCount(len(equipment))
        row = 0
        for i in equipment:
            eq_type = QTableWidgetItem(self.type_repository.get_t(i['eq_type'])['type_of_equipment'])
            eq_type.setData(1000, i['eq_type'])
            eq_type.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 0, eq_type)
            count = QTableWidgetItem(str(i['count']))
            count.setData(1000, i['id'])
            count.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 1, count)
            row += 1

    def click_add(self):
        e_dict = {'id': -1, 'eq_type': -1, 'count': -1}
        self.equipment_repository.set_dict(e_dict)
        equipment_add = EquipmentsAddDialog(self.equipment_repository)
        if (equipment_add.exec()):
            equipment_d = self.equipment_repository.get_dict()
            count_row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(count_row + 1)
            eq_type = QTableWidgetItem(self.type_repository.get_t(equipment_d['eq_type'])['type_of_equipment'])
            eq_type.setData(1000, equipment_d['eq_type'])
            eq_type.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 0, eq_type)
            count = QTableWidgetItem(str(equipment_d['count']))
            count.setData(1000, equipment_d['id'])
            count.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 1, count)

    def click_edit(self):
        edit_list = self.ui.tableWidget.selectedItems()
        if (len(edit_list)):
            select_row = self.ui.tableWidget.currentRow()
            edit_d = {'id': edit_list[1].data(1000), 'eq_type': edit_list[0].data(1000),
                      'count': int(edit_list[1].text())}
            self.equipment_repository.set_dict(edit_d)
            equipment_edit = EquipmentsAddDialog(self.equipment_repository)
            if (equipment_edit.exec()):
                equipment_d = self.equipment_repository.get_dict()
                eq_type = QTableWidgetItem(self.type_repository.get_t(equipment_d['eq_type'])['type_of_equipment'])
                eq_type.setData(1000, equipment_d['eq_type'])
                eq_type.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(select_row, 0, eq_type)
                count = QTableWidgetItem(str(equipment_d['count']))
                count.setData(1000, equipment_d['id'])
                count.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(select_row, 1, count)

    def click_del(self):
        del_list = self.ui.tableWidget.selectedItems()
        if (len(del_list)):
            del_d = {'id': del_list[1].data(1000)}
            self.equipment_repository.del_equipment(del_d)
            self.ui.tableWidget.removeRow(del_list[0].row())

    def click_cancel(self):
        self.accept()
