import os
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileDialog, QPushButton, QDialog
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QLabel
from output_window import Ui_Output
from PyQt5.QtGui import QPixmap

class Ui_HashCatWindow(object):
    wordlist_filename = ""
    hashfile = ""
    def __init__(self):
        self.textBrowser_wordlist = None
        self.windows = [self]
        self.im = "./peakpx_other.jpg"


    def futtatas(self, parancslista):  # a parancs meghívása
        #print(parancslista)
        process = subprocess.Popen(["hashcat", parancslista], stdout=subprocess.PIPE)
        output = process.communicate()
        print(output)
        output = str(output)
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

    def open_file_dialog_hashfile(self): #hashfile kitallózása
        dialog = QFileDialog()
        dialog.setDirectory(r'/home/kali')
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Text files (*.txt)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec_() == QDialog.Accepted:
            hash_file = dialog.selectedFiles()[0]
            # Split the filename and path
            hash_path, hash_filename = os.path.split(hash_file)
            if hash_file is None:
                print("Nem választottál")
            self.textBrowser_hashfile.setPlainText(hash_file)
            hs = open(hash_file, "r")
            print(hs.read())
            #pl.close()
            return hash_path, hash_filename
        else:
            return None, None


    def open_file_dialog_wordlist(self): #wordlist file kitallózása
        dialog = QFileDialog()
        dialog.setDirectory(r'/home/kali')
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Text files (*.txt)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec_() == QDialog.Accepted:
            wordlist_file = dialog.selectedFiles()[0]
            # Split the filename and path
            wordlist_file_path, wordlist_file_name = os.path.split(wordlist_file)
            if wordlist_file is None:
                print("Nem választottál")
            self.textBrowser_wordlist.setPlainText(wordlist_file)
            wl = open(wordlist_file, "r")
            print(wl.read())
            #tf.close()
            return wordlist_file_path, wordlist_file_name
        else:
            return None, None
    def setupUi(self, HashCatWindow):
        wordlist_filename = ""
        HashCatWindow.setObjectName("HashCatWindow")
        HashCatWindow.resize(551, 538)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        HashCatWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(HashCatWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_hashcat = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_hashcat.setGeometry(QtCore.QRect(140, 40, 221, 51))
        self.pushButton_hashcat.setObjectName("pushButton_hashcat")
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit.setGeometry(QtCore.QRect(170, 400, 131, 51))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.textEdit_options = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_options.setGeometry(QtCore.QRect(60, 140, 441, 41))
        self.textEdit_options.setToolTip("")
        self.textEdit_options.setStatusTip("")
        self.textEdit_options.setObjectName("textEdit_options")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 110, 151, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 190, 251, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 270, 151, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton_browse_hashfile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_browse_hashfile.setGeometry(QtCore.QRect(60, 220, 111, 51))
        self.pushButton_browse_hashfile.setObjectName("pushButton_browse_hashfile")
        self.pushButton_browse_wordlist = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_browse_wordlist.setGeometry(QtCore.QRect(60, 300, 111, 51))
        self.pushButton_browse_wordlist.setObjectName("pushButton_browse_wordlist")
        self.textBrowser_hashfile = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_hashfile.setGeometry(QtCore.QRect(180, 220, 321, 51))
        self.textBrowser_hashfile.setObjectName("textBrowser_hashfile")
        self.textBrowser_wordlist = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_wordlist.setGeometry(QtCore.QRect(180, 300, 321, 51))
        self.textBrowser_wordlist.setObjectName("textBrowser_wordlist")
        HashCatWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HashCatWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 551, 29))
        self.menubar.setObjectName("menubar")
        HashCatWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HashCatWindow)
        self.statusbar.setObjectName("statusbar")
        HashCatWindow.setStatusBar(self.statusbar)

        self.background_label = QLabel(HashCatWindow)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 551, 538))  # Adjust the dimensions as needed
        self.background_label.setPixmap(QPixmap(self.im))
        self.background_label.setScaledContents(True)
        self.background_label.lower()

        self.pushButton_browse_hashfile.clicked.connect(self.open_file_dialog_hashfile) #hashfile tallózás megnyitása
        self.pushButton_browse_wordlist.clicked.connect(self.open_file_dialog_wordlist) #wordlist tallózás megnyitása

        self.pushButton_hashcat.clicked.connect(
            lambda: self.futtatas(wordlist_filename)) #parancs futtatás metódus meghívása

        self.retranslateUi(HashCatWindow)
        self.pushButton_quit.clicked.connect(HashCatWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(HashCatWindow)

    def retranslateUi(self, HashCatWindow):
        _translate = QtCore.QCoreApplication.translate
        HashCatWindow.setWindowTitle(_translate("HashCatWindow", "MainWindow"))
        self.pushButton_hashcat.setText(_translate("HashCatWindow", "Run HashCat"))
        self.pushButton_quit.setText(_translate("HashCatWindow", "quit"))
        self.label.setText(_translate("HashCatWindow", "options:"))
        self.label_2.setText(_translate("HashCatWindow", "hash file (txt):"))
        self.label_3.setText(_translate("HashCatWindow", "wordlist (txt):"))
        self.pushButton_browse_hashfile.setText(_translate("HashCatWindow", "Browse"))
        self.pushButton_browse_wordlist.setText(_translate("HashCatWindow", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HashCatWindow = QtWidgets.QMainWindow()
    ui = Ui_HashCatWindow()
    ui.setupUi(HashCatWindow)
    HashCatWindow.show()
    sys.exit(app.exec_())
