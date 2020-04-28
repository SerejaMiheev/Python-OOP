# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'typesdialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Type(object):
    def setupUi(self, Type):
        Type.setObjectName("Type")
        Type.resize(341, 301)
        Type.setMinimumSize(QtCore.QSize(341, 301))
        Type.setMaximumSize(QtCore.QSize(341, 301))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        Type.setFont(font)
        self.pushButton = QtWidgets.QPushButton(Type)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Type)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 10, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Type)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 10, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(Type)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 321, 201))
        self.tableWidget.setMinimumSize(QtCore.QSize(321, 201))
        self.tableWidget.setMaximumSize(QtCore.QSize(321, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.pushButton_4 = QtWidgets.QPushButton(Type)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 260, 81, 31))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Type)
        QtCore.QMetaObject.connectSlotsByName(Type)

    def retranslateUi(self, Type):
        _translate = QtCore.QCoreApplication.translate
        Type.setWindowTitle(_translate("Type", "Types"))
        self.pushButton.setText(_translate("Type", "Добавить"))
        self.pushButton_2.setText(_translate("Type", "Редактировать"))
        self.pushButton_3.setText(_translate("Type", "Удалить"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Type", "Тип"))
        self.pushButton_4.setText(_translate("Type", "Закрыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Type = QtWidgets.QDialog()
    ui = Ui_Type()
    ui.setupUi(Type)
    Type.show()
    sys.exit(app.exec_())
