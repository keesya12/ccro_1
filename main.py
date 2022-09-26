from sqlite3 import Cursor
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from PyQt5.Qt import *
from deathdashboard import *
from mysql import connector as mc
from mysql.connector import Error
import resources

class Ui_adminloginscreen(object):
    
    def deathdashboard(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self.window)
        self.window.show()
        adminloginscreen.hide()
   

    def setupUi(self, adminloginscreen):
        adminloginscreen.setObjectName("adminloginscreen")
        adminloginscreen.resize(800, 600)
        adminloginscreen.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/resources/CCRO Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        adminloginscreen.setWindowIcon(icon)
        adminloginscreen.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(adminloginscreen)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 110, 141, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(381, 381))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("resource/CCRO Logo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 110, 141, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resource/cdo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 160, 191, 41))
        self.label_4.setStyleSheet("font: 87 14pt \"Arial Black\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 190, 231, 41))
        self.label_5.setStyleSheet("font: 87 15pt \"Arial Black\";")
        self.label_5.setObjectName("label_5")
        self.usernamelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernamelineEdit.setGeometry(QtCore.QRect(290, 290, 255, 41))
        self.usernamelineEdit.setStyleSheet("border-radius:7px;\n"
"font: 11pt \"Arial\";")
        self.usernamelineEdit.setCursorPosition(0)
        self.usernamelineEdit.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.usernamelineEdit.setObjectName("usernamelineEdit")
        self.passwordlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordlineEdit.setGeometry(QtCore.QRect(290, 360, 255, 41))
        self.passwordlineEdit.setStyleSheet("border-radius:7px;\n"
"font: 11pt \"Arial\";")
        self.passwordlineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordlineEdit.setClearButtonEnabled(False)
        self.passwordlineEdit.setObjectName("passwordlineEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 360, 41, 41))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/icons/resources/password_icon.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.login)
        #self.pushButton.keyPressEvent(self.login)
        self.pushButton.setGeometry(QtCore.QRect(330, 430, 171, 41))
        self.pushButton.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 79);\n"
"background-color: rgb(245, 198, 62);\n"
"border-radius: 7px;")
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 130, 121, 121))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/logos/resources/cdo.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(520, 130, 121, 121))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/logos/resources/CCRO Logo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 290, 41, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/resources/admin_icon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(110, 90, 601, 441))
        self.frame.setStyleSheet("background: rgba(121,121,121,0.3);\n"
"border-radius: 25px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(360, 560, 101, 16))
        self.label_9.setStyleSheet("font: 11pt \"arial\";")
        self.label_9.setObjectName("label_9")
        self.frame.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.usernamelineEdit.raise_()
        self.passwordlineEdit.raise_()
        self.label_6.raise_()
        self.pushButton.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_2.raise_()
        self.label_9.raise_()
        adminloginscreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(adminloginscreen)
        QtCore.QMetaObject.connectSlotsByName(adminloginscreen)

    def retranslateUi(self, adminloginscreen):
        _translate = QtCore.QCoreApplication.translate
        adminloginscreen.setWindowTitle(_translate("adminloginscreen", "Admin"))
        self.label_4.setText(_translate("adminloginscreen", "City Civil Registry"))
        self.label_5.setText(_translate("adminloginscreen", "Cagayan de Oro City"))
        self.usernamelineEdit.setPlaceholderText(_translate("adminloginscreen", "username"))
        self.passwordlineEdit.setPlaceholderText(_translate("adminloginscreen", "password"))
        self.pushButton.setText(_translate("adminloginscreen", "LOGIN"))
        self.label_9.setText(_translate("adminloginscreen", "ⓒ 2022 ClarKe"))

    def openWindow(self):
        self.deathdashboard()
    def pop_window(self, text):

        msg = QtWidgets.QMessageBox()

        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("{}".format(text))
        msg.setWindowTitle("{}".format(text))

        msg.exec_()


    def login(self):
        try:
            username = self.usernamelineEdit.text()
            password = self.passwordlineEdit.text()
            connection = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="ccro_cdo"
            )
            
            mydb = connection.cursor()
            mydb.execute("SELECT username,password from users where username like '"+username+ "'and password like '"+password+"'")
            result = mydb.fetchone()

            if result == None:
                        self.pop_window("Incorrect username or password")
            else:
                        self.openWindow()
            print ("DB Connection Success!")
        except Error as e:
            self.pop_window("Error occurred")

    #def keyPressEvent(self, e):
    #    if e.key() == Qt.Key_Enter:
    #        self.login()                             





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminloginscreen = QtWidgets.QMainWindow()
    ui = Ui_adminloginscreen()
    ui.setupUi(adminloginscreen)
    adminloginscreen.show()
    sys.exit(app.exec_())
