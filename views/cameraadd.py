# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cameraadd.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CameraAdd(object):
    def setupUi(self, CameraAdd):
        CameraAdd.setObjectName("CameraAdd")
        CameraAdd.resize(532, 91)
        CameraAdd.setMinimumSize(QtCore.QSize(532, 91))
        CameraAdd.setMaximumSize(QtCore.QSize(532, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        CameraAdd.setFont(font)
        self.label_2 = QtWidgets.QLabel(CameraAdd)
        self.label_2.setGeometry(QtCore.QRect(10, 15, 61, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(CameraAdd)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 17, 291, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(CameraAdd)
        self.pushButton.setGeometry(QtCore.QRect(382, 11, 139, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(CameraAdd)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 50, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(CameraAdd)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 50, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(CameraAdd)
        QtCore.QMetaObject.connectSlotsByName(CameraAdd)

    def retranslateUi(self, CameraAdd):
        _translate = QtCore.QCoreApplication.translate
        CameraAdd.setWindowTitle(_translate("CameraAdd", "Camera"))
        self.label_2.setText(_translate("CameraAdd", "Каталог:"))
        self.pushButton.setText(_translate("CameraAdd", "Выбрать каталог"))
        self.pushButton_2.setText(_translate("CameraAdd", "Добавить"))
        self.pushButton_3.setText(_translate("CameraAdd", "Отмена"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CameraAdd = QtWidgets.QDialog()
    ui = Ui_CameraAdd()
    ui.setupUi(CameraAdd)
    CameraAdd.show()
    sys.exit(app.exec_())
