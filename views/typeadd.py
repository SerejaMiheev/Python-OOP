# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'typeadd.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TypeAdd(object):
    def setupUi(self, TypeAdd):
        TypeAdd.setObjectName("TypeAdd")
        TypeAdd.resize(218, 84)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        TypeAdd.setFont(font)
        self.label = QtWidgets.QLabel(TypeAdd)
        self.label.setGeometry(QtCore.QRect(10, 6, 41, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(TypeAdd)
        self.lineEdit.setGeometry(QtCore.QRect(45, 13, 161, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(TypeAdd)
        self.pushButton.setGeometry(QtCore.QRect(26, 42, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(TypeAdd)
        self.pushButton_2.setGeometry(QtCore.QRect(126, 42, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(TypeAdd)
        QtCore.QMetaObject.connectSlotsByName(TypeAdd)

    def retranslateUi(self, TypeAdd):
        _translate = QtCore.QCoreApplication.translate
        TypeAdd.setWindowTitle(_translate("TypeAdd", "Type"))
        self.label.setText(_translate("TypeAdd", "Тип:"))
        self.pushButton.setText(_translate("TypeAdd", "Добавить"))
        self.pushButton_2.setText(_translate("TypeAdd", "Отмена"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TypeAdd = QtWidgets.QDialog()
    ui = Ui_TypeAdd()
    ui.setupUi(TypeAdd)
    TypeAdd.show()
    sys.exit(app.exec_())
