import sys

import self as self
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.uic.properties import QtWidgets

import main

Ui_MainWindow, baseClass = uic.loadUiType('main.ui')
Ui_NmapWindow, baseClass = uic.loadUiType('nmap_window_old.ui')
#from nmap_window import Ui_NmapWindow
#from main_window_2 import Ui_MainWindow

class MainWindow(baseClass):

    def openNmap(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_NmapWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #main_window_2.pushButton_nmap = QtWidgets.QPushButton(main_window_2.centralwidget, clicked = lambda: self.openNmap())
        #self.pushButton_quit.clicked.connect(self.closeEvent())
        # Your code ends here
        self.show()






if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())