from PyQt5.QtWidgets import QDialog

from controllers.personcontroller import PersonController
from views.personadd import Ui_PersonAdd


class PersonAddDialog(QDialog):
    def __init__(self, person_controller: PersonController):
        super(PersonAddDialog, self).__init__()
        self.persons_controller = person_controller
        self.person_d = person_controller.get_dict()
        self.initUI()

    def initUI(self):
        self.ui = Ui_PersonAdd()
        self.ui.setupUi(self)

        if (len(self.person_d['fio'])):
            self.ui.lineEdit.setText(self.person_d['fio'])

        self.ui.pushButton.clicked.connect(self.click_ok)
        self.ui.pushButton_2.clicked.connect(self.click_cancel)

    def click_ok(self):
        c_person = self.ui.lineEdit.text()
        c_person = c_person.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")

        if (self.person_d['id'] == -1):
            if (len(c_person)):
                self.person_d['fio'] = c_person
                self.person_d['id'] = self.persons_controller.new_person(self.person_d)
                self.persons_controller.set_dict(self.person_d)
                self.accept()
        else:
            if (len(c_person)):
                self.person_d['fio'] = c_person
                self.persons_controller.update_person(self.person_d)
                self.persons_controller.set_dict(self.person_d)
                self.accept()

    def click_cancel(self):
        self.reject()
