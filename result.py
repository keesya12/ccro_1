from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import mysql.connector as mc



class Ui_Dialog(object):
    
    def searchResult(self):
        connection = mc.connect(
                host="localhost",
                user="root",
                passwd="123456",
                database="ccro_cdo"
            )
        try:
         with connection.cursor() as cursor:
            refNo = "SELECT * FROM burial_permit_data where refNum LIKE'%"+refno+"%'"

            cursor.execute(refNo)
            row = cursor.fetchall()
            if len(row)>0:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Search Results")
                msg.setText(str(row))
                x = msg.exec_()
            else:
                self.pop_window("Need Reference Number")
        except Exception as e:
            self.pop_window("Error Occurred!")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 174)
        self.result = QtWidgets.QLineEdit(Dialog)
        self.result.setGeometry(QtCore.QRect(10, 70, 1250, 51))
        self.result.textChanged.connect(self.searchResult)
        self.result.setReadOnly(True)
        self.result.setObjectName("result")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 111, 16))
        self.label.setStyleSheet("font: 12pt \"Arial\";")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Search Results:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
