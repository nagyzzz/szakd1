import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NmapWindow(object):

    def futtatas(jelszo, parancslista): #a parancs meghívása
        sudoPasswd = subprocess.Popen(["echo", jelszo], stdout=subprocess.PIPE)
        output = subprocess.check_output(["sudo", "-S", "-k"] + parancslista, stdin=sudoPasswd.stdout)
        return output
    def setupUi(self, NmapWindow):
        NmapWindow.setObjectName("NmapWindow")
        NmapWindow.resize(550, 600)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        NmapWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(NmapWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_nmap = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_nmap.setGeometry(QtCore.QRect(140, 40, 221, 51))
        self.pushButton_nmap.setObjectName("pushButton_nmap")
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit.setGeometry(QtCore.QRect(180, 450, 131, 51))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.textEdit_password = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_password.setGeometry(QtCore.QRect(60, 120, 411, 41))
        self.textEdit_password.setToolTip("")
        self.textEdit_password.setStatusTip("")
        self.textEdit_password.setObjectName("textEdit_password")
        self.textEdit_options = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_options.setGeometry(QtCore.QRect(60, 190, 411, 41))
        self.textEdit_options.setToolTip("")
        self.textEdit_options.setStatusTip("")
        self.textEdit_options.setObjectName("textEdit_options")
        self.checkBox_sC = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_sC.setGeometry(QtCore.QRect(220, 340, 61, 41))
        self.checkBox_sC.setObjectName("checkBox_sC")
        self.checkBox_sS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_sS.setGeometry(QtCore.QRect(220, 390, 61, 41))
        self.checkBox_sS.setObjectName("checkBox_sS")
        self.textEdit_target_ip = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_target_ip.setGeometry(QtCore.QRect(60, 260, 411, 41))
        self.textEdit_target_ip.setToolTip("")
        self.textEdit_target_ip.setStatusTip("")
        self.textEdit_target_ip.setObjectName("textEdit_target_ip")
        NmapWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NmapWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 29))
        self.menubar.setObjectName("menubar")
        NmapWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NmapWindow)
        self.statusbar.setObjectName("statusbar")
        NmapWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NmapWindow)
        self.pushButton_quit.clicked.connect(NmapWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(NmapWindow)

        command = "nmap" + str(self.textEdit_options) + str(self.textEdit_target_ip)
        command = command.split()
        self.pushButton_nmap.clicked.connect(lambda: self.futtatas(self.textEdit_password.toPlainText(), command))
    def retranslateUi(self, NmapWindow):
        _translate = QtCore.QCoreApplication.translate
        NmapWindow.setWindowTitle(_translate("NmapWindow", "MainWindow"))
        self.pushButton_nmap.setText(_translate("NmapWindow", "Run Nmap"))
        self.pushButton_quit.setText(_translate("NmapWindow", "quit"))
        self.checkBox_sC.setText(_translate("NmapWindow", "-sC"))
        self.checkBox_sS.setText(_translate("NmapWindow", "-sS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NmapWindow = QtWidgets.QMainWindow()
    ui = Ui_NmapWindow()
    ui.setupUi(NmapWindow)
    NmapWindow.show()
    sys.exit(app.exec_())
