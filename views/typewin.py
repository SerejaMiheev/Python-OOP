from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from controllers.typecontroller import TypeController
from views.typeaddwin import TypeAddDialog
from views.typesdialog import Ui_Type


class TypeDialog(QDialog):
    def __init__(self):
        super(TypeDialog, self).__init__()
        self.type_controller = TypeController()
        self.initUI()

    def initUI(self):
        self.ui = Ui_Type()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnWidth(0, 315)
        self.ui.tableWidget.setSelectionBehavior(1)
        self.ui.tableWidget.setSelectionMode(1)

        self.ui.pushButton.clicked.connect(self.click_add)
        self.ui.pushButton_2.clicked.connect(self.click_edit)
        self.ui.pushButton_3.clicked.connect(self.click_del)
        self.ui.pushButton_4.clicked.connect(self.click_cancel)

        types = self.type_controller.get_types()
        self.ui.tableWidget.setRowCount(len(types))
        row = 0
        for i in types:
            type_of_equipment = QTableWidgetItem(i['type_of_equipment'])
            type_of_equipment.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 0, type_of_equipment)
            row += 1

    def click_add(self):
        t_dict = {'id': -1, 'type_of_equipment': ""}
        self.type_controller.set_dict(t_dict)
        type_add = TypeAddDialog(self.type_controller)
        if (type_add.exec()):
            type_d = self.type_controller.get_dict()
            count_row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(count_row + 1)
            type_of_equipment = QTableWidgetItem(type_d['type_of_equipment'])
            type_of_equipment.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 0, type_of_equipment)

    def click_edit(self):
        edit_list = self.ui.tableWidget.selectedItems()
        if(len(edit_list)):
            select_row = self.ui.tableWidget.currentRow()
            edit_d = self.type_controller.get_type({'type_of_equipment': edit_list[0].text()})
            self.type_controller.set_dict(edit_d)
            type_edit = TypeAddDialog(self.type_controller)
            if (type_edit.exec()):
                type_d = self.type_controller.get_dict()
                type_of_equipment = QTableWidgetItem(type_d['type_of_equipment'])
                type_of_equipment.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(select_row, 0, type_of_equipment)

    def click_del(self):
        del_list = self.ui.tableWidget.selectedItems()
        if (len(del_list)):
            self.type_controller.del_type({'type_of_equipment': del_list[0].text()})
            self.ui.tableWidget.removeRow(del_list[0].row())

    def click_cancel(self):
        self.reject()
