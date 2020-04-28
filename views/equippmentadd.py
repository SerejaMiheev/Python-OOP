# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'equippmentadd.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EquipmentAdd(object):
    def setupUi(self, EquipmentAdd):
        EquipmentAdd.setObjectName("EquipmentAdd")
        EquipmentAdd.resize(342, 122)
        EquipmentAdd.setMinimumSize(QtCore.QSize(342, 122))
        EquipmentAdd.setMaximumSize(QtCore.QSize(342, 122))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        EquipmentAdd.setFont(font)
        self.label = QtWidgets.QLabel(EquipmentAdd)
        self.label.setGeometry(QtCore.QRect(10, 4, 141, 31))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(EquipmentAdd)
        self.comboBox.setGeometry(QtCore.QRect(150, 10, 181, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(EquipmentAdd)
        self.label_2.setGeometry(QtCore.QRect(10, 43, 61, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(EquipmentAdd)
        self.lineEdit.setGeometry(QtCore.QRect(70, 50, 101, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(EquipmentAdd)
        self.pushButton.setGeometry(QtCore.QRect(150, 80, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(EquipmentAdd)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 80, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(EquipmentAdd)
        QtCore.QMetaObject.connectSlotsByName(EquipmentAdd)

    def retranslateUi(self, EquipmentAdd):
        _translate = QtCore.QCoreApplication.translate
        EquipmentAdd.setWindowTitle(_translate("EquipmentAdd", "Equipment"))
        self.label.setText(_translate("EquipmentAdd", "Тип оборудования:"))
        self.label_2.setText(_translate("EquipmentAdd", "Кол-во:"))
        self.pushButton.setText(_translate("EquipmentAdd", "Добавить"))
        self.pushButton_2.setText(_translate("EquipmentAdd", "Отмена"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EquipmentAdd = QtWidgets.QDialog()
    ui = Ui_EquipmentAdd()
    ui.setupUi(EquipmentAdd)
    EquipmentAdd.show()
    sys.exit(app.exec_())
