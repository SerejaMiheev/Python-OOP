from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from controllers.eventcontroller import EventController
from controllers.personcontroller import PersonController
from views.eventaddwin import EventAddDialog
from views.eventdialog import Ui_Events


class EventDialog(QDialog):
    def __init__(self):
        super(EventDialog, self).__init__()
        self.event_controller = EventController()
        self.person_controller = PersonController()
        self.initUI()

    def initUI(self):
        self.ui = Ui_Events()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnWidth(0, 120)
        self.ui.tableWidget.setColumnWidth(1, 60)
        self.ui.tableWidget.setColumnWidth(2, 160)
        self.ui.tableWidget.setSelectionBehavior(1)
        self.ui.tableWidget.setSelectionMode(1)

        self.ui.pushButton.clicked.connect(self.click_add)
        self.ui.pushButton_2.clicked.connect(self.click_del)
        self.ui.pushButton_3.clicked.connect(self.click_cancel)

        event = self.event_controller.get_events()
        self.ui.tableWidget.setRowCount(len(event))
        row = 0
        for i in event:
            e_date = QTableWidgetItem(str(i['date']))
            e_date.setData(1000, i['id'])
            e_date.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 0, e_date)
            e_camera = QTableWidgetItem(str(i['camera']))
            e_camera.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 1, e_camera)
            if (i['person'] != None):
                e_person = QTableWidgetItem(self.person_controller.get_person({'id': i['person']})['fio'])
                e_person.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(row, 2, e_person)
            else:
                e_person = QTableWidgetItem("Отсутствует")
                e_person.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(row, 2, e_person)
            row += 1

    def click_add(self):
        e_dict = {'id': -1, 'camera': -1, 'person': -1}
        self.event_controller.set_dict(e_dict)
        event_add = EventAddDialog(self.event_controller)
        if (event_add.exec()):
            event_d = self.event_controller.get_dict()
            count_row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(count_row + 1)
            e_date = QTableWidgetItem(str(event_d['date']))
            e_date.setData(1000, event_d['id'])
            e_date.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 0, e_date)
            e_camera = QTableWidgetItem(str(event_d['camera']))
            e_camera.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 1, e_camera)
            if(event_d['person'] != -1):
                e_person = QTableWidgetItem(self.person_controller.get_person({'id': event_d['person']})['fio'])
                e_person.setData(1000, event_d['person'])
                e_person.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(count_row, 2, e_person)
            else:
                e_person = QTableWidgetItem("Отсутствует")
                e_person.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(count_row, 2, e_person)

    def click_del(self):
        del_list = self.ui.tableWidget.selectedItems()
        if (len(del_list)):
            del_d = {'id': del_list[0].data(1000)}
            self.event_controller.del_event(del_d)
            self.ui.tableWidget.removeRow(del_list[0].row())

    def click_cancel(self):
        self.accept()
