from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog

from repository.equipmentrepository import EquipmentRepository
from repository.typerepository import TypeRepository
from views.equippmentadd import Ui_EquipmentAdd


class EquipmentsAddDialog(QDialog):
    def __init__(self, equipment_repository: EquipmentRepository):
        super(EquipmentsAddDialog, self).__init__()
        self.equipment_repository = equipment_repository
        self.equipment_d = equipment_repository.get_dict()
        self.type_repository = TypeRepository()
        self.initUI()

    def initUI(self):
        self.ui = Ui_EquipmentAdd()
        self.ui.setupUi(self)
        self.ui.lineEdit.setValidator(QtGui.QIntValidator(0,100000))

        types = self.type_repository.get_types()
        for i in types:
            self.ui.comboBox.addItem(i['type_of_equipment'], i['id'])

        if (self.equipment_d['count'] != -1):
            self.ui.lineEdit.setText(str(self.equipment_d['count']))
            self.ui.comboBox.setCurrentText(
                self.type_repository.get_t(self.equipment_d['eq_type'])['type_of_equipment'])

        self.ui.pushButton.clicked.connect(self.click_add)
        self.ui.pushButton_2.clicked.connect(self.click_cancel)

    def click_add(self):
        c_count = self.ui.lineEdit.text()

        if (self.equipment_d['id'] == -1):
            if (len(c_count)):
                self.equipment_d['count'] = int(c_count)
                self.equipment_d['eq_type'] = self.ui.comboBox.currentData()
                self.equipment_d['id'] = self.equipment_repository.new_equipment(self.equipment_d)
                self.equipment_repository.set_dict(self.equipment_d)
                self.accept()

        else:
            if (len(c_count)):
                self.equipment_d['count'] = int(c_count)
                self.equipment_d['eq_type'] = self.ui.comboBox.currentData()
                self.equipment_repository.update_equipment(self.equipment_d)
                self.equipment_repository.set_dict(self.equipment_d)
                self.accept()

    def click_cancel(self):
        self.reject()
