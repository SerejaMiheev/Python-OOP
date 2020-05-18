from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from repository.personrepository import PersonRepository
from views.perondialog import Ui_Dialog
from views.personaddwin import PersonAddDialog


class PersonDialog(QDialog):
    def __init__(self):
        super(PersonDialog, self).__init__()
        self.person_repository = PersonRepository()
        self.initUI()

    def initUI(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnWidth(1, 259)
        self.ui.tableWidget.setSelectionBehavior(1)
        self.ui.tableWidget.setSelectionMode(1)

        self.ui.pushButton.clicked.connect(self.click_add)
        self.ui.pushButton_2.clicked.connect(self.click_edit)
        self.ui.pushButton_3.clicked.connect(self.click_del)
        self.ui.pushButton_4.clicked.connect(self.click_cancel)

        persons = self.person_repository.get_persons()
        self.ui.tableWidget.setRowCount(len(persons))
        row = 0
        for i in persons:
            id_person = QTableWidgetItem(str(i['id']))
            id_person.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            fio_person = QTableWidgetItem(i['fio'])
            fio_person.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 0, id_person)
            self.ui.tableWidget.setItem(row, 1, fio_person)
            row += 1

    def click_add(self):
        p_dict = {'id': -1, 'fio': ""}
        self.person_repository.set_dict(p_dict)
        person_add = PersonAddDialog(self.person_repository)
        if (person_add.exec()):
            person_d = self.person_repository.get_dict()
            count_row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(count_row + 1)
            id_person = QTableWidgetItem(str(person_d['id']))
            id_person.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            fio_person = QTableWidgetItem(person_d['fio'])
            fio_person.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 0, id_person)
            self.ui.tableWidget.setItem(count_row, 1, fio_person)

    def click_edit(self):
        edit_list = self.ui.tableWidget.selectedItems()
        if(len(edit_list)):
            select_row = self.ui.tableWidget.currentRow()
            edit_d = {'id': int(edit_list[0].text()), 'fio': edit_list[1].text()}
            self.person_repository.set_dict(edit_d)
            person_edit = PersonAddDialog(self.person_repository)
            if (person_edit.exec()):
                person_d = self.person_repository.get_dict()
                id_person = QTableWidgetItem(str(person_d['id']))
                id_person.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                fio_person = QTableWidgetItem(person_d['fio'])
                fio_person.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(select_row, 0, id_person)
                self.ui.tableWidget.setItem(select_row, 1, fio_person)

    def click_del(self):
        del_list = self.ui.tableWidget.selectedItems()
        if (len(del_list)):
            del_d = {'id': int(del_list[0].text()), 'fio': del_list[1].text()}
            self.person_repository.del_person(del_d)
            self.ui.tableWidget.removeRow(del_list[0].row())

    def click_cancel(self):
        self.accept()
