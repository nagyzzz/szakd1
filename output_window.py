
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTextBrowser, QLabel
from PyQt5.QtGui import QPixmap, QColor

class Ui_Output(object):
    textBrowser: QTextBrowser

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit.setGeometry(QtCore.QRect(190, 540, 181, 81))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 40, 800, 480))
        self.textBrowser.setObjectName("textBrowser")
        #self.textBrowser.setText("output.setText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        """
        self.background_label = QLabel(MainWindow)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 900, 700))  # Adjust the dimensions as needed
        self.background_label.setPixmap(QPixmap(self.im))
        self.background_label.setScaledContents(True)
        self.background_label.lower()
        """
        self.retranslateUi(MainWindow)
        self.pushButton_quit.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_quit.setText(_translate("MainWindow", "quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Output()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


def textBrowser():
    return None