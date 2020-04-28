from PyQt5.QtWidgets import QDialog

from controllers.typecontroller import TypeController
from views.typeadd import Ui_TypeAdd


class TypeAddDialog(QDialog):
    def __init__(self, type_controller: TypeController):
        super(TypeAddDialog, self).__init__()
        self.type_controller = type_controller
        self.type_d = type_controller.get_dict()
        self.initUI()

    def initUI(self):
        self.ui = Ui_TypeAdd()
        self.ui.setupUi(self)

        if (len(self.type_d['type_of_equipment'])):
            self.ui.lineEdit.setText(self.type_d['type_of_equipment'])

        self.ui.pushButton.clicked.connect(self.click_add)
        self.ui.pushButton_2.clicked.connect(self.click_cancel)

    def click_add(self):
        c_type = self.ui.lineEdit.text()
        c_type = c_type.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")

        if (self.type_d['id'] == -1):
            if (len(c_type)):
                self.type_d['type_of_equipment'] = c_type
                self.type_d['id'] = self.type_controller.new_type(self.type_d)
                self.type_controller.set_dict(self.type_d)
                self.accept()
        else:
            if (len(c_type)):
                self.type_d['type_of_equipment'] = c_type
                self.type_controller.update_type(self.type_d)
                self.type_controller.set_dict(self.type_d)
                self.accept()

    def click_cancel(self):
        self.reject()
