from PyQt5.QtWidgets import QDialog, QFileDialog

from controllers.cameracontroller import CameraController
from views.cameraadd import Ui_CameraAdd


class CameraAddDialog(QDialog):
    def __init__(self, camera_controller: CameraController):
        super(CameraAddDialog, self).__init__()
        self.camera_controller = camera_controller
        self.camera_d = camera_controller.get_dict()
        self.initUI()

    def initUI(self):
        self.ui = Ui_CameraAdd()
        self.ui.setupUi(self)
        self.ui.lineEdit_2.setReadOnly(True)

        if (len(self.camera_d['loc_record'])):
            self.ui.lineEdit_2.setText(self.camera_d['loc_record'])

        self.ui.pushButton.clicked.connect(self.click_choose)
        self.ui.pushButton_2.clicked.connect(self.click_add)
        self.ui.pushButton_3.clicked.connect(self.click_cancel)

    def click_choose(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.DirectoryOnly)

        if dialog.exec_():
            file_name = dialog.selectedFiles()
            self.ui.lineEdit_2.setText(file_name[0])

    def click_add(self):
        c_dir = self.ui.lineEdit_2.text()

        if (self.camera_d['id'] == -1):
            if (len(c_dir)):
                self.camera_d['loc_record'] = c_dir
                self.camera_d['id'] = self.camera_controller.new_camera(self.camera_d)
                self.camera_controller.set_dict(self.camera_d)
                self.accept()
        else:
            if (len(c_dir)):
                self.camera_d['loc_record'] = c_dir
                self.camera_controller.update_camera(self.camera_d)
                self.camera_controller.set_dict(self.camera_d)
                self.accept()

    def click_cancel(self):
        self.reject()
