import os
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileDialog, QPushButton, QDialog
from pathlib import Path
from PyQt5.QtWidgets import QApplication

from output_window import Ui_Output


class Ui_JohnWindow(object):
    password_list_filename = None
    target_filename = None
    def __init__(self):
        self.windows = [self]
        self.textBrowser_target_file = None


    def futtatas(self, parancslista):  # a parancs meghívása
        #print(parancslista)
        process = subprocess.Popen(["john", parancslista], stdout=subprocess.PIPE)
        output = process.communicate()
        print(output)
        output = str(output)
        self.openOutput(output)

    def openOutput(self, szoveg=None):
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

    def open_file_dialog_password_list(self):
        dialog = QFileDialog()
        dialog.setDirectory(r'/home/kali')
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Text files (*.txt)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec_() == QDialog.Accepted:
            password_list_filename = dialog.selectedFiles()[0]
            # Split the filename and path
            password_list_path, password_list_file = os.path.split(password_list_filename)
            if password_list_path is None:
                print("Nem választottál")
            self.textBrowser_password_list.setPlainText(password_list_filename)
            pl = open(password_list_filename, "r")
            print(pl.read())
            #pl.close()
            return password_list_path, password_list_file
        else:
            return None, None


    def open_file_dialog_target_file(self):
        dialog = QFileDialog()
        dialog.setDirectory(r'/home/kali')
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Text files (*.txt)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec_() == QDialog.Accepted:
            target_file = dialog.selectedFiles()[0]
            # Split the filename and path
            target_file_path, target_file_name = os.path.split(target_file)
            if target_file is None:
                print("Nem választottál")
            self.textBrowser_target_file.setPlainText(target_file)
            tf = open(target_file, "r")
            print(tf.read())
            #tf.close()
            return target_file_path, target_file_name
        else:
            return None, None
    def setupUi(self, JohnWindow):
        JohnWindow.setObjectName("JohnWindow")
        JohnWindow.resize(551, 538)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        JohnWindow.setFont(font)
        password_list_filename = ""
        target_filename = ""
        self.centralwidget = QtWidgets.QWidget(JohnWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_john = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_john.setGeometry(QtCore.QRect(140, 40, 221, 51))
        self.pushButton_john.setObjectName("pushButton_nmap")
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit.setGeometry(QtCore.QRect(170, 400, 131, 51))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.textEdit_options = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_options.setGeometry(QtCore.QRect(60, 140, 441, 41))
        self.textEdit_options.setToolTip("")
        self.textEdit_options.setStatusTip("")
        self.textEdit_options.setObjectName("textEdit_password")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 110, 151, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 190, 251, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 270, 151, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton_password_list = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_password_list.setGeometry(QtCore.QRect(60, 220, 111, 51))
        self.pushButton_password_list.setObjectName("pushButton_password_list")
        self.pushButton_target_file = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_target_file.setGeometry(QtCore.QRect(60, 300, 111, 51))
        self.pushButton_target_file.setObjectName("pushButton_target_file")
        self.textBrowser_password_list = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_password_list.setGeometry(QtCore.QRect(180, 220, 321, 51))
        self.textBrowser_password_list.setObjectName("textBrowser_password_list")
        #self.textBrowser_password_list.setPlainText(password_list_filename)
        self.textBrowser_target_file = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_target_file.setGeometry(QtCore.QRect(180, 300, 321, 51))
        self.textBrowser_target_file.setObjectName("textBrowser_target_file")
        self.textBrowser_target_file.setPlainText(target_filename)
        JohnWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JohnWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 551, 29))
        self.menubar.setObjectName("menubar")
        JohnWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(JohnWindow)
        self.statusbar.setObjectName("statusbar")
        JohnWindow.setStatusBar(self.statusbar)

        self.pushButton_password_list.clicked.connect(self.open_file_dialog_password_list)
        self.pushButton_target_file.clicked.connect(self.open_file_dialog_target_file)
        self.retranslateUi(JohnWindow)
        self.pushButton_quit.clicked.connect(JohnWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(JohnWindow)

        self.pushButton_john.clicked.connect(
            lambda: self.futtatas(password_list_filename))

    def retranslateUi(self, JohnWindow):
        _translate = QtCore.QCoreApplication.translate
        JohnWindow.setWindowTitle(_translate("JohnWindow", "MainWindow"))
        self.pushButton_john.setText(_translate("JohnWindow", "Run John"))
        self.pushButton_quit.setText(_translate("JohnWindow", "quit"))
        self.label.setText(_translate("JohnWindow", "options:"))
        self.label_2.setText(_translate("JohnWindow", "jelszó lista (pl: rockyou.txt):"))
        self.label_3.setText(_translate("JohnWindow", "cél fájl (txt):"))
        self.pushButton_password_list.setText(_translate("JohnWindow", "Browse"))
        self.pushButton_target_file.setText(_translate("JohnWindow", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JWindow = QtWidgets.QMainWindow()
    ui = Ui_JohnWindow()
    ui.setupUi(JWindow)
    JWindow.show()
    sys.exit(app.exec_())
