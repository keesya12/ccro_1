import this
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import mysql.connector as mc
from PyQt5.QtPrintSupport import *
from burial import *
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
import resources
import sys
import pandas as pd
from xlwt import *
import xlsxwriter

class Ui_Dashboard(object):
    def burialForm(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_BurialForm()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def loadData(self):
        connection = mc.connect(
                host="localhost",
                user="root",
                passwd="123456",
                database="ccro_cdo"
            )
            
        with connection:
                cur = connection.cursor()
                tablerow = 0
                row = cur.execute("SELECT * FROM burial_permit_data")
                data = cur.fetchall()

                for row in data:
                        
                        self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
                        self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                        self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
                        self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
                        self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
                        self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
                        self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))
                        self.tableWidget.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(row[8]))
                        self.tableWidget.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(row[9]))
                        self.tableWidget.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(row[10]))
                        self.tableWidget.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(row[11]))
                        self.tableWidget.setItem(tablerow, 12, QtWidgets.QTableWidgetItem(row[12]))
                        self.tableWidget.setItem(tablerow, 13, QtWidgets.QTableWidgetItem(row[13]))
                        self.tableWidget.setItem(tablerow, 14, QtWidgets.QTableWidgetItem(row[14]))
                        self.tableWidget.setItem(tablerow, 15, QtWidgets.QTableWidgetItem(row[15]))
                        self.tableWidget.setItem(tablerow, 16, QtWidgets.QTableWidgetItem(row[16]))


                        
                        tablerow += 1


    def searchResult(self):
            connection = mc.connect(
                    host="localhost",
                    user="root",
                    passwd="123456",
                    database="ccro_cdo"
                )
            try:
                with connection.cursor() as cursor:
                    refno = "SELECT * FROM burial_permit_data where refNum LIKE'%"+self.search_lineEdit.text()+"%'"

                    cursor.execute(refno)
                    row = cursor.fetchall()
                    if len(row)>0:
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle("Search Results of Ref #: "+self.search_lineEdit.text())
                        msg.setStyleSheet("font: 12pt")
                        msg.setBaseSize(QSize(1350, 120))
                        msg.setText(str(row))
                        x=msg.exec_()
                    
                    else:
                        self.pop_window("Need Reference Number")
            except Exception as e:
                    self.pop_window("Error Occurred!")

    def handlePrint(self):
        fn, _ = QFileDialog.getSaveFileName(self, 'Export PDF', None, 'PDF files (.pdf);;All Files()')
        if fn != '':
            if QFileInfo(fn).suffix() == "" : fn += '.pdf'
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.tableWidget.document().print_(printer)

    
    def setupUi(self, Dashboard):
        Dashboard.setObjectName("Dashboard")
        Dashboard.resize(1280, 700)
        Dashboard.setMaximumSize(QtCore.QSize(1280, 700))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        Dashboard.setFont(font)
        Dashboard.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/resources/CCRO Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dashboard.setWindowIcon(icon)
        Dashboard.setDocumentMode(True)
        Dashboard.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.xl_file = ""
        self.xl_file_name = ""
        self.centralwidget = QtWidgets.QWidget(Dashboard)
        self.centralwidget.setObjectName("centralwidget")
        
        self.search_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.search_lineEdit.setPlaceholderText("Search by Reference Number")
        self.search_lineEdit.setGeometry(QtCore.QRect(890, 10, 350, 30))
        self.search_lineEdit.setStyleSheet("border-radius: 7px;")
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.clicked.connect(self.searchResult)
        self.search.setGeometry(QtCore.QRect(1200, 13, 41, 23))
        self.search.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/resources/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search.setIcon(icon1)
        self.search.setDefault(True)
        self.search.setFlat(True)
        self.search.setObjectName("search")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.clicked.connect(self.burialForm)
        self.add.setGeometry(QtCore.QRect(10, 10, 131, 30))
        self.add.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.add.setStyleSheet("background-color: rgb(238, 210, 2);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 7px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/resources/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add.setIcon(icon2)
        self.add.setObjectName("add")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 49, 1280, 631))
        self.tableWidget.setMouseTracking(True)
        self.tableWidget.setTabletTracking(True)
        self.tableWidget.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tableWidget.setStyleSheet("font: 11pt \"Arial\";")
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(2)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(1048576)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(17)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        Dashboard.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dashboard)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setGeometry(QtCore.QRect(169, 125, 172, 150))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        Dashboard.setMenuBar(self.menubar)
        self.actionPrint = QtWidgets.QAction(Dashboard)
        self.actionPrint.setObjectName("actionPrint")
        self.actionPrint.triggered.connect(self.saveFile)
        self.actionPrint_2 = QtWidgets.QAction(Dashboard)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/resources/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint_2.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.actionPrint_2.setFont(font)
        self.actionPrint_2.setObjectName("actionPrint_2")
        self.actionExport = QtWidgets.QAction(Dashboard)
        self.actionExport.triggered.connect(self.saveFile)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/resources/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.actionExport.setFont(font)
        self.actionExport.setObjectName("actionExport")
        self.actionLogout = QtWidgets.QAction(Dashboard)
        self.actionLogout.triggered.connect(qApp.quit)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.actionLogout.setFont(font)
        self.actionLogout.setObjectName("actionLogout")
        self.actionRefresh = QtWidgets.QAction(Dashboard)
        self.actionRefresh.triggered.connect(self.loadData)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/resources/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.actionRefresh.setFont(font)
        self.actionRefresh.setObjectName("actionRefresh")
        self.menuFile.addAction(self.actionRefresh)
        self.menuFile.addAction(self.actionPrint_2)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLogout)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Dashboard)
        QtCore.QMetaObject.connectSlotsByName(Dashboard)
    
    def retranslateUi(self, Dashboard):
        _translate = QtCore.QCoreApplication.translate
        Dashboard.setWindowTitle(_translate("Dashboard", "Death Dashboard"))
        self.add.setText(_translate("Dashboard", "Add New"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dashboard", "Reference Number"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dashboard", "Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dashboard", "Payer's Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dashboard", "City"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dashboard", "Province"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dashboard", "Name of Deceased"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dashboard", "Nationality"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dashboard", "Age"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Dashboard", "Sex"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Dashboard", "Date of Death"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Dashboard", "Cause of Death"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Dashboard", "Name of Cemetery"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Dashboard", "Infectious/Not Infectious"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("Dashboard", "Body Embalmed/Not Embalmed"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("Dashboard", "Disposition of Remains"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("Dashboard", "Amount Paid"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("Dashboard", "Collecting Officer"))
        self.menuFile.setTitle(_translate("Dashboard", "File"))
        self.actionPrint.setText(_translate("Dashboard", "Add New"))
        self.actionPrint_2.setText(_translate("Dashboard", "Print "))
        self.actionExport.setText(_translate("Dashboard", "Save"))
        self.actionLogout.setText(_translate("Dashboard", "Logout"))
        self.actionRefresh.setText(_translate("Dashboard", "Refresh"))

    
    def pop_window(self, text):

        msg = QtWidgets.QMessageBox()

        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("{}".format(text))
        msg.setWindowTitle("{}".format(text))

        msg.exec_()
    

    def printDialog(self):
 
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)
    def printpreviewDialog(self):
 
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.printPreview)
        previewDialog.exec_()
 
    def printPreview(self, printer):
        self.tableWidget.print_(printer)

    def saveFile(self):
        option = QFileDialog.DontUseNativeDialog
        file = QFileDialog.getSaveFileName(self.centralwidget,"Save File"," ","All Files(*);; Excel(*.xlsx)", options=option)
        #print (file[0])
    
        workbook = xlsxwriter.Workbook('burialData.xlsx')
        worksheet = workbook.add_worksheet()
        connection = mc.connect(
                host="localhost",
                user="root",
                passwd="123456",
                database="ccro_cdo"
            )
        
        
        with connection:
                cur = connection.cursor()
                row = cur.execute("SELECT * FROM burial_permit_data")
                data = cur.fetchall()

                document = QtGui.QTextDocument()
                cursor = QtGui.QTextCursor(document)
                
                model = self.tableWidget.model()
                for c in range(model.columnCount()):
                    text = model.headerData(c, QtCore.Qt.Horizontal)
                    worksheet.write(0, c+1, text)

                for r in range(model.rowCount()):
                    text = model.headerData(r, QtCore.Qt.Vertical)
                    worksheet.write(r+1, 0, text)

                for c in range(model.columnCount()):
                    for r in range(model.rowCount()):
                        text = model.data(model.index(r, c))
                        worksheet.write(r+1, c+1, text)
                

        workbook.close()
 

 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dashboard = QtWidgets.QMainWindow()
    ui = Ui_Dashboard()
    ui.setupUi(Dashboard)
    Dashboard.show()
    sys.exit(app.exec_())
