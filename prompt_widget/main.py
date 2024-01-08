import os
import sys
from datetime import datetime

import numpy as np

from qtpy import QtCore, QtGui, QtWidgets
from qtpy.QtCore import Slot, Signal


from main_widget_ui import Ui_Form


class MyForm(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        
        # UI init
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.setMinimumSize(640, 480)
        self.resize(800, 600)
        
        self.ui.sb_refreshTime.wheelEvent = lambda event: None
        
        # UI Style
        self.ui.hbl1.setSpacing(2)
        self.ui.chart1.setStyleSheet("background-color: #FFFFFF;")
        self.ui.chart2.setStyleSheet("background-color: #FFFFFF;")
        
        # add Chart toolbar with location
        self.ui.chart1.addToolBar()
        self.ui.chart2.addToolBar(0)
        
        # UI Default property
        self.ui.btn_stop.setEnabled(False)
        
        # Plot timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.on_btn_plot_clicked)
        
        # Frame rate timer : buffer 5 second
        self.buf = np.zeros(6)
        self.count = 0
        self.timer_fps = QtCore.QTimer(self)
        self.timer_fps.timeout.connect(self.update_fps)
        self.timer_fps.start(1000)
    
    @Slot()
    def on_btn_play_clicked(self):
        self.ui.btn_stop.setEnabled(True)
        self.ui.btn_play.setEnabled(False)
        self.ui.btn_plot.setEnabled(False)
        self.ui.sb_refreshTime.setEnabled(False)
        
        if not self.timer.isActive():
            refresh_time = self.ui.sb_refreshTime.value()
            self.timer.start(int(refresh_time))
    
    @Slot()
    def on_btn_stop_clicked(self):
        self.timer.stop()
        
        self.ui.btn_stop.setEnabled(False)
        self.ui.btn_play.setEnabled(True)
        self.ui.btn_plot.setEnabled(True)
        self.ui.sb_refreshTime.setEnabled(True)
    
    @Slot()
    def on_btn_plot_clicked(self):
        n = 100
        
        x = np.linspace(1, n, n)
        y1 = np.random.rand(n)
        y2 = np.random.rand(n)
        y3 = np.random.rand(n) * 0.5
        
        self.plot1(x, y1)
        self.plot2(x, y2, y3)
        
        self.count += 1
    
    def plot1(self, x, y):
        chart = self.ui.chart1
        chart.clearAxes()
        
        chart.ax.plot(x, y, 'C0')
        chart.ax.grid()
        
        str_title = datetime.now().strftime('%H:%M:%S.%f')[:-3]
        chart.ax.set_title(str_title)
        
        chart.draw()
    
    def plot2(self, x, y1, y2):
        chart = self.ui.chart2
        chart.clearAxes()
        
        # add right axis
        ax2 = chart.ax.twinx()
        
        chart.ax.plot(x, y1, 'C1')
        ax2.plot(x, y2, '+:C2')
        
        chart.ax.grid()
        
        chart.ax.set_ylim(0, 1)
        ax2.set_ylim(0, 1)
        
        chart.ax.set_xlabel('index')
        chart.ax.set_ylabel('left y-label')
        ax2.set_ylabel('right y-label')
        
        str_title = datetime.now().strftime('%H:%M:%S.%f')[:-3]
        chart.ax.set_title(str_title)
        
        chart.draw()
    
    def update_fps(self):
        self.buf = np.roll(self.buf, -1)
        self.buf[-1] = self.count

        delta = float(self.buf[-1] - self.buf[0])
        fps = max(delta, 0) / float(len(self.buf) - 1)
        self.ui.lb_fps.setText(f"{fps:.1f} Hz")


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    
    win = MyForm()
    win.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
