from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from controllers.cameracontroller import CameraController
from views.cameraaddwin import CameraAddDialog
from views.cameradialog import Ui_Dialog


class CameraDialog(QDialog):
    def __init__(self):
        super(CameraDialog, self).__init__()
        self.cameras_controller = CameraController()
        self.initUI()

    def initUI(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(331, 404)
        self.ui.tableWidget.setColumnWidth(0, 60)
        self.ui.tableWidget.setColumnWidth(1, 208)
        self.ui.tableWidget.setSelectionBehavior(1)
        self.ui.tableWidget.setSelectionMode(1)

        self.ui.pushButton.clicked.connect(self.click_add)
        self.ui.pushButton_2.clicked.connect(self.click_edit)
        self.ui.pushButton_3.clicked.connect(self.click_del)
        self.ui.pushButton_4.clicked.connect(self.click_cancel)

        cameras = self.cameras_controller.get_cameras()
        self.ui.tableWidget.setRowCount(len(cameras))
        row = 0
        for i in cameras:
            id_camera = QTableWidgetItem(str(i['id']))
            id_camera.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            loc_record = QTableWidgetItem(i['loc_record'])
            loc_record.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 0, id_camera)
            self.ui.tableWidget.setItem(row, 1, loc_record)
            row += 1


    def click_add(self):
        c_dict = {'id': -1, 'loc_record': ""}
        self.cameras_controller.set_dict(c_dict)
        camera_add = CameraAddDialog(self.cameras_controller)
        if(camera_add.exec()):
            camera_d = self.cameras_controller.get_dict()
            count_row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(count_row + 1)
            id_camera = QTableWidgetItem(str(camera_d['id']))
            id_camera.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            loc_record = QTableWidgetItem(camera_d['loc_record'])
            loc_record.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 0, id_camera)
            self.ui.tableWidget.setItem(count_row, 1, loc_record)

    def click_edit(self):
        edit_list = self.ui.tableWidget.selectedItems()
        if(len(edit_list)):
            select_row = self.ui.tableWidget.currentRow()
            edit_d = {'id': int(edit_list[0].text()), 'loc_record': edit_list[1].text()}
            self.cameras_controller.set_dict(edit_d)
            camera_edit = CameraAddDialog(self.cameras_controller)
            if(camera_edit.exec()):
                camera_d = self.cameras_controller.get_dict()
                id_camera = QTableWidgetItem(str(camera_d['id']))
                id_camera.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                loc_record = QTableWidgetItem(camera_d['loc_record'])
                loc_record.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(select_row, 0, id_camera)
                self.ui.tableWidget.setItem(select_row, 1, loc_record)

    def click_del(self):
        del_list = self.ui.tableWidget.selectedItems()
        if (len(del_list)):
            del_d = {'id': int(del_list[0].text()),  'loc_record': del_list[1].text()}
            self.cameras_controller.del_camera(del_d)
            self.ui.tableWidget.removeRow(del_list[0].row())

    def click_cancel(self):
        self.accept()