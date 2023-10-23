import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QProgressBar

class WorkerThread(QThread):
    update_signal = pyqtSignal(int)
    finished_signal = pyqtSignal()

    def run(self):
        for i in range(101):
            time.sleep(0.1)  # Simulate work
            self.update_signal.emit(i)
        self.finished_signal.emit()

class ProcessStatusIndicator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Process Status Indicator')
        self.setGeometry(100, 100, 400, 100)

        layout = QVBoxLayout()

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMaximum(100)

        self.status_label = QPushButton('I am working', self)
        self.status_label.setDisabled(True)

        self.start_button = QPushButton('Start Process', self)
        self.start_button.clicked.connect(self.start_process)

        layout.addWidget(self.progress_bar)
        layout.addWidget(self.status_label)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def start_process(self):
        self.start_button.setDisabled(True)

        self.worker_thread = WorkerThread()
        self.worker_thread.update_signal.connect(self.update_progress)
        self.worker_thread.finished_signal.connect(self.process_finished)
        self.worker_thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def process_finished(self):
        self.status_label.setText('Process Completed')
        self.start_button.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProcessStatusIndicator()
    window.show()
    sys.exit(app.exec_())
