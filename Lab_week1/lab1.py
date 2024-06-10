#   Students: Ryoma Nonaka & Jonas Skolnik
#   UvAnetID: 14932431 & 14932423
#   Studie: BSc Informatica
#   File: lab1.py
#   Goal: This file implements a PyQt5 application that interacts with
#   accelerometer data to visualize the data in real-time. The application
#   generates random data for initial plotting and allows the user to start
#   and stop the data process with a button click. After enabling the button
#   It uses the x y z data given by the arduino.

import sys
import matplotlib
import numpy as np
from lab1_ui import Ui_MainWindow
# from mplwidget import MplWidget
from lab1_accel import get_accelarator
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as
# FigureCanvas
# from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as
# NavigationToolbar
# from matplotlib.figure import Figure

matplotlib.use("Qt5Agg")

# 1000 = 1 seconde
seconden = 1000
max_x = 6


class Lab1(QMainWindow):
    def __init__(self, *args):
        super(Lab1, self).__init__(*args)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.MplWidget = self.ui.widget

        self.begin = 1
        self.end = 6
        self.init_random_data()

        self.ui.spinBox.setValue(self.end - self.begin)
        self.ui.spinBox_2.setValue(1)

        self.plot_random()
        self.reset()

        self.timer = QTimer()
        self.timer.timeout.connect(self.TimerEnable)

        self.ui.pushButton.setText("Enable")
        self.ui.pushButton.clicked.connect(self.timeFunction)

        self.setWindowTitle("arduino_sensors")

    #   Function initializing the data when starting the program
    #   and the lists for the data from the arduino accelerator
    def init_random_data(self):
        self.x = np.arange(self.begin, self.end)
        self.y = np.random.rand(self.end - self.begin)
        self.yX = []
        self.yY = []
        self.yZ = []

    #   This Function plots the initial random data
    def plot_random(self):
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(self.x, self.y, "r", linewidth=0.4)
        self.MplWidget.canvas.draw()

    #   This Function handles the enable/disable
    #   button click to start or stop the timer
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
            self.reset()

    #   This Function enables the timer to update the plot
    def TimerEnable(self):
        self.update_x()

    #   This Function updates the x-axis and accelerometer data,
    #   then updates the plot
    def update_x(self):
        self.acc += 1
        x, y, z = get_accelarator()
        self.x.append(self.acc)
        self.yX.append(x)
        self.yY.append(y)
        self.yZ.append(z)
        print(self.yX, self.yY, self.yZ)
        if self.acc >= max_x:
            self.yX.pop(0)
            self.yY.pop(0)
            self.yZ.pop(0)
            self.x.pop(0)
        if self.acc <= self.end:
            self.update_plot()
        else:
            self.timeFunction()
            self.reset()

    #   This Function Updates the plot with the latest data
    def update_plot(self):
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(self.x, self.yX, "r",
                                        linewidth=0.4)
        self.MplWidget.canvas.axes.plot(self.x, self.yY, "g",
                                        linewidth=0.4)
        self.MplWidget.canvas.axes.plot(self.x, self.yZ, "b",
                                        linewidth=0.4)
        self.MplWidget.canvas.draw()

    #   This Function Resets the data lists and accumulator
    def reset(self):
        self.x = []
        self.yX = []
        self.yY = []
        self.yZ = []
        self.acc = 0


if __name__ == "__main__":
    app = QApplication([])
    form = Lab1()
    form.show()
    sys.exit(app.exec_())
