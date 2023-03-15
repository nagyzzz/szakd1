
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JohnWindow(object):
    def setupUi(self, JohnWindow):
        JohnWindow.setObjectName("JWindow")
        JohnWindow.resize(551, 538)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        JohnWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(JohnWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_nmap = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_nmap.setGeometry(QtCore.QRect(140, 40, 221, 51))
        self.pushButton_nmap.setObjectName("pushButton_nmap")
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit.setGeometry(QtCore.QRect(170, 400, 131, 51))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.textEdit_password = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_password.setGeometry(QtCore.QRect(60, 140, 441, 41))
        self.textEdit_password.setToolTip("")
        self.textEdit_password.setStatusTip("")
        self.textEdit_password.setObjectName("textEdit_password")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 110, 151, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 190, 251, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 270, 151, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton_quit_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit_2.setGeometry(QtCore.QRect(60, 220, 111, 51))
        self.pushButton_quit_2.setObjectName("pushButton_quit_2")
        self.pushButton_quit_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit_3.setGeometry(QtCore.QRect(60, 300, 111, 51))
        self.pushButton_quit_3.setObjectName("pushButton_quit_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(180, 220, 321, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(180, 300, 321, 51))
        self.textBrowser_2.setObjectName("textBrowser_2")
        JohnWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JohnWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 551, 29))
        self.menubar.setObjectName("menubar")
        JohnWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(JohnWindow)
        self.statusbar.setObjectName("statusbar")
        JohnWindow.setStatusBar(self.statusbar)

        self.retranslateUi(JohnWindow)
        self.pushButton_quit.clicked.connect(JohnWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(JohnWindow)

    def retranslateUi(self, JWindow):
        _translate = QtCore.QCoreApplication.translate
        JWindow.setWindowTitle(_translate("JWindow", "MainWindow"))
        self.pushButton_nmap.setText(_translate("JWindow", "Run John"))
        self.pushButton_quit.setText(_translate("JWindow", "quit"))
        self.label.setText(_translate("JWindow", "options:"))
        self.label_2.setText(_translate("JWindow", "jelszó lista (pl: rockyou.txt):"))
        self.label_3.setText(_translate("JWindow", "cél fájl (txt):"))
        self.pushButton_quit_2.setText(_translate("JWindow", "Browse"))
        self.pushButton_quit_3.setText(_translate("JWindow", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JWindow = QtWidgets.QMainWindow()
    ui = Ui_JWindow()
    ui.setupUi(JWindow)
    JWindow.show()
    sys.exit(app.exec_())
