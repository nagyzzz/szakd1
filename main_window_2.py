
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

from nmap_window import Ui_NmapWindow #masodik ablak megnyitasa

class Ui_MainWindow(object):

    def __init__(self):
        self.windows = [self]

    def openNmap(self):
        window = QtWidgets.QMainWindow()
        self.ui = Ui_NmapWindow()
        self.ui.setupUi(window)
        window.show()
        self.windows.append(window)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 700)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_nmap = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openNmap()) #masodik ablak megnyitasa
        self.pushButton_nmap.setGeometry(QtCore.QRect(200, 150, 171, 61))
        self.pushButton_nmap.setObjectName("pushButton_nmap")
        self.pushButton_hashcat = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_hashcat.setGeometry(QtCore.QRect(200, 360, 181, 81))
        self.pushButton_hashcat.setObjectName("pushButton_hashcat")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(140, 40, 291, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_johntheripper = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_johntheripper.setGeometry(QtCore.QRect(180, 250, 221, 71))
        self.pushButton_johntheripper.setObjectName("pushButton_johntheripper")
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit.setGeometry(QtCore.QRect(200, 480, 181, 81))
        self.pushButton_quit.setObjectName("pushButton_quit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #self.pushButton_quit.clicked.connect(MainWindow.closeEvent) # type: ignore
        self.pushButton_quit.clicked.connect(QApplication.closeAllWindows)
        #self.pushButton_nmap.clicked.connect(MainWindow.openNmap)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_nmap.setText(_translate("MainWindow", "nmap"))
        self.pushButton_hashcat.setText(_translate("MainWindow", "hashcat"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Verdana\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">V??lassz egy opci??t:</p></body></html>"))
        self.pushButton_johntheripper.setText(_translate("MainWindow", "john the ripper"))
        self.pushButton_quit.setText(_translate("MainWindow", "quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
