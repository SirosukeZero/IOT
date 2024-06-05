import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
import matplotlib

from lab1_ui import *

class Lab1(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.MplWidget = matplotlib.use("Qt5Agg")
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.button_function)
        # window = loadUi("Lab_week1/lab1.ui", self)
        self.setWindowTitle("arduino_sensors")

    def button_function(self):
        print("poep")
    

if __name__ == "__main__":
    app = QApplication([])
    form = Lab1()
    form.show()
    sys.exit(app.exec_())