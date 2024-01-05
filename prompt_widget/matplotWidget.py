import os

from qtpy import QtWidgets

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


## pre-defined matplotlib style
STYLE_FILE = 'plotStyle.style'
filepath = os.path.join(os.path.dirname(__file__), STYLE_FILE)

if os.path.isfile(filepath):
    from matplotlib import pyplot
    pyplot.style.use(filepath)


"""
reference
https://dymaxionkim.blogspot.com/2012/12/pyqt-gui-matplotlib.html
"""

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()

        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
        self.setParent(parent)
        self.ax = self.fig.add_subplot(111)
        
        self.mpl_connect('resize_event', self.resize_figure)

    def resize_figure(self, e):
        self.fig.tight_layout()
        
    def clearAxes(self):
        if len(self.fig.axes) > 1:
            """problem with twinx ylabel location
            """
            ax2 = self.fig.axes[-1]
            self.fig.delaxes(ax2)
        
        self.ax.clear()


class MatplotWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MatplotWidget, self).__init__(parent=parent)
        
        self.mpl_toolbar = None
        
        self.canvas = MplCanvas(self)
        self.ax = self.canvas.ax
        
        self.vbl = QtWidgets.QVBoxLayout()
        self.vbl.setContentsMargins(0,0,0,0)
        self.vbl.setSpacing(0)
        
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
    
    def addToolBar(self, loc=1):
        self.mpl_toolbar = NavigationToolbar(self.canvas, self)
        if loc == 0:
            self.vbl.insertWidget(0, self.mpl_toolbar)
        else:
            self.vbl.addWidget(self.mpl_toolbar)

    def clearAxes(self):
        self.canvas.clearAxes()
    
    def draw(self):
        self.canvas.draw_idle()
        self.canvas.flush_events()
