# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1102, 612)
        MainWindow.setStyleSheet("background-color: rgb(30, 31, 28);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_serial = QtWidgets.QLabel(self.centralwidget)
        self.label_serial.setGeometry(QtCore.QRect(20, 19, 1061, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        font.setPointSize(16)
        self.label_serial.setFont(font)
        self.label_serial.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_serial.setAlignment(QtCore.Qt.AlignCenter)
        self.label_serial.setObjectName("label_serial")
        self.textBrowser_serial = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_serial.setGeometry(QtCore.QRect(20, 75, 1061, 51))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(14)
        self.textBrowser_serial.setFont(font)
        self.textBrowser_serial.setStyleSheet("color: rgb(255, 255, 255);")
        self.textBrowser_serial.setObjectName("textBrowser_serial")
        self.pushButto_granted = QtWidgets.QPushButton(self.centralwidget)
        self.pushButto_granted.setGeometry(QtCore.QRect(20, 210, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButto_granted.setFont(font)
        self.pushButto_granted.setStyleSheet("background-color: rgb(189, 255, 148);\n"
"border-radius: 10px;")
        self.pushButto_granted.setObjectName("pushButto_granted")
        self.pushButto_denied = QtWidgets.QPushButton(self.centralwidget)
        self.pushButto_denied.setGeometry(QtCore.QRect(920, 210, 160, 51))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButto_denied.setFont(font)
        self.pushButto_denied.setStyleSheet("background-color: rgb(189, 255, 148);\n"
"border-radius: 10px;")
        self.pushButto_denied.setObjectName("pushButto_denied")
        self.pushButto_register = QtWidgets.QPushButton(self.centralwidget)
        self.pushButto_register.setGeometry(QtCore.QRect(480, 210, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButto_register.setFont(font)
        self.pushButto_register.setObjectName("pushButto_register")
        self.textBrowser_output = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_output.setGeometry(QtCore.QRect(252, 143, 691, 51))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(14)
        self.textBrowser_output.setFont(font)
        self.textBrowser_output.setStyleSheet("color: rgb(255, 255, 255);")
        self.textBrowser_output.setObjectName("textBrowser_output")
        self.label_output = QtWidgets.QLabel(self.centralwidget)
        self.label_output.setGeometry(QtCore.QRect(20, 150, 211, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        font.setPointSize(12)
        self.label_output.setFont(font)
        self.label_output.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_output.setAlignment(QtCore.Qt.AlignCenter)
        self.label_output.setObjectName("label_output")
        self.pushButton_upload = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_upload.setGeometry(QtCore.QRect(958, 143, 121, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.pushButton_upload.setFont(font)
        self.pushButton_upload.setStyleSheet("background-color: rgb(180, 251, 255);\n"
"border-radius: 10px;")
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.label_detail = QtWidgets.QLabel(self.centralwidget)
        self.label_detail.setGeometry(QtCore.QRect(20, 290, 1061, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        font.setPointSize(16)
        self.label_detail.setFont(font)
        self.label_detail.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_detail.setAlignment(QtCore.Qt.AlignCenter)
        self.label_detail.setObjectName("label_detail")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(20, 350, 211, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        font.setPointSize(12)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.textBrowser_name = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_name.setGeometry(QtCore.QRect(252, 343, 831, 51))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(14)
        self.textBrowser_name.setFont(font)
        self.textBrowser_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.textBrowser_name.setObjectName("textBrowser_name")
        self.label_id = QtWidgets.QLabel(self.centralwidget)
        self.label_id.setGeometry(QtCore.QRect(18, 427, 211, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        font.setPointSize(12)
        self.label_id.setFont(font)
        self.label_id.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_id.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id.setObjectName("label_id")
        self.textBrowser_id = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_id.setGeometry(QtCore.QRect(250, 420, 831, 51))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(14)
        self.textBrowser_id.setFont(font)
        self.textBrowser_id.setStyleSheet("color: rgb(255, 255, 255);")
        self.textBrowser_id.setObjectName("textBrowser_id")
        self.label_gender = QtWidgets.QLabel(self.centralwidget)
        self.label_gender.setGeometry(QtCore.QRect(18, 507, 211, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        font.setPointSize(12)
        self.label_gender.setFont(font)
        self.label_gender.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_gender.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gender.setObjectName("label_gender")
        self.textBrowser_gender = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_gender.setGeometry(QtCore.QRect(250, 500, 831, 51))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(14)
        self.textBrowser_gender.setFont(font)
        self.textBrowser_gender.setStyleSheet("color: rgb(255, 255, 255);")
        self.textBrowser_gender.setObjectName("textBrowser_gender")
        self.pushButto_edit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButto_edit.setGeometry(QtCore.QRect(480, 210, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButto_edit.setFont(font)
        self.pushButto_edit.setStyleSheet("background-color: rgb(189, 255, 148);\n"
"border-radius: 10px;")
        self.pushButto_edit.setObjectName("pushButto_edit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1102, 26))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.menuUser = QtWidgets.QMenu(self.menubar)
        self.menuUser.setObjectName("menuUser")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuUser.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_serial.setText(_translate("MainWindow", "Serial Number"))
        self.pushButto_granted.setText(_translate("MainWindow", "Granted"))
        self.pushButto_denied.setText(_translate("MainWindow", "Denied"))
        self.pushButto_register.setText(_translate("MainWindow", "Register"))
        self.label_output.setText(_translate("MainWindow", "Output Folder :"))
        self.pushButton_upload.setText(_translate("MainWindow", "Upload"))
        self.label_detail.setText(_translate("MainWindow", "Details"))
        self.label_name.setText(_translate("MainWindow", "Employee Name :"))
        self.label_id.setText(_translate("MainWindow", "Employee ID :"))
        self.label_gender.setText(_translate("MainWindow", "Gender :"))
        self.pushButto_edit.setText(_translate("MainWindow", "Edit"))
        self.menuMain.setTitle(_translate("MainWindow", "Main"))
        self.menuUser.setTitle(_translate("MainWindow", "User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())