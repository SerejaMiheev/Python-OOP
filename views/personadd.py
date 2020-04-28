# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personadd.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PersonAdd(object):
    def setupUi(self, PersonAdd):
        PersonAdd.setObjectName("PersonAdd")
        PersonAdd.resize(311, 79)
        PersonAdd.setMinimumSize(QtCore.QSize(311, 79))
        PersonAdd.setMaximumSize(QtCore.QSize(311, 79))
        self.label = QtWidgets.QLabel(PersonAdd)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(PersonAdd)
        self.lineEdit.setGeometry(QtCore.QRect(60, 10, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(PersonAdd)
        self.pushButton.setGeometry(QtCore.QRect(120, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(PersonAdd)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(PersonAdd)
        QtCore.QMetaObject.connectSlotsByName(PersonAdd)

    def retranslateUi(self, PersonAdd):
        _translate = QtCore.QCoreApplication.translate
        PersonAdd.setWindowTitle(_translate("PersonAdd", "Person"))
        self.label.setText(_translate("PersonAdd", "ФИО:"))
        self.pushButton.setText(_translate("PersonAdd", "Добавить"))
        self.pushButton_2.setText(_translate("PersonAdd", "Отмена"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PersonAdd = QtWidgets.QDialog()
    ui = Ui_PersonAdd()
    ui.setupUi(PersonAdd)
    PersonAdd.show()
    sys.exit(app.exec_())
