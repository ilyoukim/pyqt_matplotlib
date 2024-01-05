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
        
        ## UI init
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.sb_refreshTime.wheelEvent = lambda event: None
        
        ## UI Style
        self.ui.hbl1.setSpacing(2)
        self.ui.chart1.setStyleSheet("background-color: #FFFFFF;")
        self.ui.chart2.setStyleSheet("background-color: #FFFFFF;")
        
        ## add Chart toolbar with location
        self.ui.chart1.addToolBar()
        self.ui.chart2.addToolBar(0)
        
        ## UI Default property
        self.ui.btn_Stop.setEnabled(False)
        
        ## Plot timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.on_btn_Plot_clicked)
        
        ## Frame rate timer : buffer 5 second
        self.buf = np.zeros(6)
        self.count = 0
        self.timerfps = QtCore.QTimer()
        self.timerfps.timeout.connect(self.updateFPS)
        self.timerfps.start(1000)
    
    @Slot()
    def on_btn_Play_clicked(self):
        self.ui.btn_Stop.setEnabled(True)
        self.ui.btn_Play.setEnabled(False)
        self.ui.btn_Plot.setEnabled(False)
        self.ui.sb_refreshTime.setEnabled(False)
        
        if not self.timer.isActive():
            refreshTime = self.ui.sb_refreshTime.value()
            self.timer.start(int(refreshTime))
    
    @Slot()
    def on_btn_Stop_clicked(self):
        self.timer.stop()
        
        self.ui.btn_Stop.setEnabled(False)
        self.ui.btn_Play.setEnabled(True)
        self.ui.btn_Plot.setEnabled(True)
        self.ui.sb_refreshTime.setEnabled(True)
    
    @Slot()
    def on_btn_Plot_clicked(self):
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
        
        strTitle = datetime.now().strftime('%H:%M:%S.%f')[:-3]
        chart.ax.set_title(strTitle)
        
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
        
        strTitle = datetime.now().strftime('%H:%M:%S.%f')[:-3]
        chart.ax.set_title(strTitle)
        
        chart.draw()
    
    def updateFPS(self):
        self.buf = np.roll(self.buf, -1)
        self.buf[-1] = self.count
        
        fps = max(self.buf[-1] - self.buf[0], 0) / float(len(self.buf) - 1)
        self.ui.lb_fps.setText(f"{fps:.1f} Hz")


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    
    win = MyForm()
    win.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
