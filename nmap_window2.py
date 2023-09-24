import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QLabel
from output_window import Ui_Output
from PyQt5.QtGui import QPixmap

class Ui_NmapWindow(object):
    pushButton_nmap: QPushButton

    def __init__(self):
        self.ui = None
        self.windows = [self]
        self.im = "./peakpx_other.jpg"

    def futtatas(self, jelszo, parancslista):  #a parancs meghívása
        #print(jelszo)
        #print(parancslista)
        sudoPasswd = subprocess.Popen(["echo", jelszo], stdout=subprocess.PIPE)
        parancslista = parancslista.split()
        output = subprocess.check_output(["sudo", "-S", "-k"] + parancslista, stdin=sudoPasswd.stdout)
        print(output)
        #szoveg = print(output)
        output = str(output)
        #output = output.splitlines()
        self.openOutput(output)

    def openOutput(self, szoveg=None): #output ablak megnyitása
        szoveg = szoveg.splitlines()
        szoveg = '\n'.join(szoveg)
        window = QtWidgets.QMainWindow()
        self.ui = Ui_Output()
        self.ui.setupUi(window)
        self.ui.textBrowser.setText(szoveg)
        #self.ui.textBrowser.setText(szoveg.encode('utf-8').decode('utf-8'))
        #self.ui.textBrowser.setText(str(szoveg.encode("utf-8")))
        window.show()
        self.windows.append(window)


    def command(self) -> object: #a parancs összeállítása
        sC = ""
        sS = ""
        if self.checkBox_sC.isChecked():
            sC = "-sC "
        if self.checkBox_sS.isChecked():
            sS = "-sS "
        return "nmap " + sC + sS + self.textEdit_options.toPlainText() + " " + self.textEdit_target_ip.toPlainText()
        #return "nmap " + self.textEdit_target_ip.toPlainText()
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
        self.pushButton_quit.setGeometry(QtCore.QRect(180, 480, 131, 51))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.textEdit_password = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_password.setGeometry(QtCore.QRect(60, 140, 411, 41))
        self.textEdit_password.setToolTip("")
        self.textEdit_password.setStatusTip("")
        self.textEdit_password.setObjectName("textEdit_password")
        self.textEdit_options = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_options.setGeometry(QtCore.QRect(60, 220, 411, 41))
        self.textEdit_options.setToolTip("")
        self.textEdit_options.setStatusTip("")
        self.textEdit_options.setObjectName("textEdit_options")
        self.checkBox_sC = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_sC.setGeometry(QtCore.QRect(220, 360, 61, 41))
        self.checkBox_sC.setObjectName("checkBox_sC")
        self.checkBox_sS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_sS.setGeometry(QtCore.QRect(220, 420, 61, 41))
        self.checkBox_sS.setObjectName("checkBox_sS")
        self.textEdit_target_ip = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_target_ip.setGeometry(QtCore.QRect(60, 300, 411, 41))
        self.textEdit_target_ip.setToolTip("")
        self.textEdit_target_ip.setStatusTip("")
        self.textEdit_target_ip.setObjectName("textEdit_target_ip")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 110, 151, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 190, 151, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 270, 151, 31))
        self.label_3.setObjectName("label_3")
        NmapWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NmapWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 29))
        self.menubar.setObjectName("menubar")
        NmapWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NmapWindow)
        self.statusbar.setObjectName("statusbar")
        NmapWindow.setStatusBar(self.statusbar)

        self.background_label = QLabel(NmapWindow)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 551, 538))  # Adjust the dimensions as needed
        self.background_label.setPixmap(QPixmap(self.im))
        self.background_label.setScaledContents(True)
        self.background_label.lower()

        self.retranslateUi(NmapWindow)
        self.pushButton_quit.clicked.connect(NmapWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(NmapWindow)

        self.pushButton_nmap.clicked.connect(
            lambda: self.futtatas(self.textEdit_password.toPlainText(), self.command())) #a parancs meghívása

    def retranslateUi(self, NmapWindow):
        _translate = QtCore.QCoreApplication.translate
        NmapWindow.setWindowTitle(_translate("NmapWindow", "MainWindow"))
        self.pushButton_nmap.setText(_translate("NmapWindow", "Run Nmap"))
        self.pushButton_quit.setText(_translate("NmapWindow", "quit"))
        self.checkBox_sC.setText(_translate("NmapWindow", "-sC"))
        self.checkBox_sS.setText(_translate("NmapWindow", "-sS"))
        self.label.setText(_translate("NmapWindow", "sudo password:"))
        self.label_2.setText(_translate("NmapWindow", "options:"))
        self.label_3.setText(_translate("NmapWindow", "target IP:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NmapWindow = QtWidgets.QMainWindow()
    ui = Ui_NmapWindow()
    ui.setupUi(NmapWindow)
    NmapWindow.show()
    sys.exit(app.exec_())
