import sys
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
import matplotlib
import numpy as np
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from lab1_ui import Ui_MainWindow
from mplwidget import MplWidget


class Lab1(QMainWindow):
    def __init__(self, *args):
        super(Lab1, self).__init__(*args)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.MplWidget = self.ui.widget

        self.x = np.arange(1, 6)
        self.y = np.random.rand(5)
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(self.x, self.y, 'r', linewidth=0.5)
        self.MplWidget.canvas.draw()

        self.timer = QTimer()
        # self.timer.timeout.connect(self.showTime)
        self.ui.pushButton.setText("Enable")
        self.ui.pushButton.clicked.connect(self.timeFunction)
        
        self.setWindowTitle("arduino_sensors")

    def timeFunction(self):
        if self.ui.pushButton.text() == "Enable":
            self.timer.start(1000)
            self.ui.pushButton.setText("Disable")
        elif self.ui.pushButton.text() == "Disable":
            self.timer.stop()
            self.ui.pushButton.setText("Enable")


if __name__ == "__main__":
    app = QApplication([])
    form = Lab1()
    form.show()
    sys.exit(app.exec_())
