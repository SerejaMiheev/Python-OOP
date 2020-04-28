from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog

from controllers.equipmentcontroller import EquipmentController
from controllers.typecontroller import TypeController
from views.equippmentadd import Ui_EquipmentAdd


class EquipmentsAddDialog(QDialog):
    def __init__(self, equipment_controller: EquipmentController):
        super(EquipmentsAddDialog, self).__init__()
        self.equipment_controller = equipment_controller
        self.equipment_d = equipment_controller.get_dict()
        self.type_controller = TypeController()
        self.initUI()

    def initUI(self):
        self.ui = Ui_EquipmentAdd()
        self.ui.setupUi(self)
        self.ui.lineEdit.setValidator(QtGui.QIntValidator(0,100000))

        types = self.type_controller.get_types()
        for i in types:
            self.ui.comboBox.addItem(i['type_of_equipment'], i['id'])

        if (self.equipment_d['count'] != -1):
            self.ui.lineEdit.setText(str(self.equipment_d['count']))
            self.ui.comboBox.setCurrentText(
                self.type_controller.get_t(self.equipment_d['eq_type'])['type_of_equipment'])

        self.ui.pushButton.clicked.connect(self.click_add)
        self.ui.pushButton_2.clicked.connect(self.click_cancel)

    def click_add(self):
        c_count = self.ui.lineEdit.text()

        if (self.equipment_d['id'] == -1):
            if (len(c_count)):
                self.equipment_d['count'] = int(c_count)
                self.equipment_d['eq_type'] = self.ui.comboBox.currentData()
                self.equipment_d['id'] = self.equipment_controller.new_equipment(self.equipment_d)
                self.equipment_controller.set_dict(self.equipment_d)
                self.accept()

        else:
            if (len(c_count)):
                self.equipment_d['count'] = int(c_count)
                self.equipment_d['eq_type'] = self.ui.comboBox.currentData()
                self.equipment_controller.update_equipment(self.equipment_d)
                self.equipment_controller.set_dict(self.equipment_d)
                self.accept()

    def click_cancel(self):
        self.reject()
