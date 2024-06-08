import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
import matplotlib
import numpy as np
import serial

matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from lab1_ui import Ui_MainWindow
from mplwidget import MplWidget


ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600)

seconden = 1000


class Lab1(QMainWindow):
    def __init__(self, *args):
        super(Lab1, self).__init__(*args)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.MplWidget = self.ui.widget

        self.begin = 1
        self.end = 6

        self.x = np.arange(self.begin, self.end)
        self.y = np.random.rand(self.end - self.begin)
        self.ui.spinBox.setValue(self.end - self.begin)
        self.ui.spinBox_2.setValue(1)

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(self.x, self.y, "r", linewidth=0.5)
        self.MplWidget.canvas.draw()
        self.x = []
        self.y = []
        self.acc = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.TimerEnable)

        self.ui.pushButton.setText("Enable")
        self.ui.pushButton.clicked.connect(self.timeFunction)

        self.setWindowTitle("arduino_sensors")

    def timeFunction(self):
        if self.ui.pushButton.text() == "Enable":
            self.ui.pushButton.setText("Disable")
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.draw()
            self.end = self.ui.spinBox.value()
            self.timer.start(self.ui.spinBox_2.value() * seconden)
        elif self.ui.pushButton.text() == "Disable":
            self.timer.stop()
            self.ui.pushButton.setText("Enable")
            self.x = []
            self.y = []
            self.acc = 0

    def TimerEnable(self):
        self.update_x()

    def update_x(self):
        self.acc += 1
        self.x.append(self.acc)
        self.y.append(np.random.rand())
        if len(self.x) <= self.end:
            self.MplWidget.canvas.axes.plot(self.x, self.y, "r", linewidth=0.5)
            self.MplWidget.canvas.draw()
        else:
            self.timeFunction()
            self.x = []
            self.y = []
            self.acc = 0


if __name__ == "__main__":
    app = QApplication([])
    form = Lab1()
    form.show()
    sys.exit(app.exec_())
