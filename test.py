import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = "test"
        self.setWindowTitle(self.title)

        label = QLabel(self)
        pixmap = QPixmap('peakpx.jpg')
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())