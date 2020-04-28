# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eventdialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Events(object):
    def setupUi(self, Events):
        Events.setObjectName("Events")
        Events.resize(400, 290)
        Events.setMinimumSize(QtCore.QSize(400, 290))
        Events.setMaximumSize(QtCore.QSize(400, 290))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        Events.setFont(font)
        self.pushButton = QtWidgets.QPushButton(Events)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Events)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 10, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(Events)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 381, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton_3 = QtWidgets.QPushButton(Events)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 250, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Events)
        QtCore.QMetaObject.connectSlotsByName(Events)

    def retranslateUi(self, Events):
        _translate = QtCore.QCoreApplication.translate
        Events.setWindowTitle(_translate("Events", "Events"))
        self.pushButton.setText(_translate("Events", "Создать"))
        self.pushButton_2.setText(_translate("Events", "Удалить"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Events", "Дата"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Events", "Камера"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Events", "Человек"))
        self.pushButton_3.setText(_translate("Events", "Закрыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Events = QtWidgets.QDialog()
    ui = Ui_Events()
    ui.setupUi(Events)
    Events.show()
    sys.exit(app.exec_())
