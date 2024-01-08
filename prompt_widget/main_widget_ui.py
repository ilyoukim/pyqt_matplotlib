# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hbl_top = QtWidgets.QHBoxLayout()
        self.hbl_top.setObjectName("hbl_top")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hbl_top.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.hbl_top.addWidget(self.label)
        self.sb_refreshTime = QtWidgets.QSpinBox(Form)
        self.sb_refreshTime.setMinimumSize(QtCore.QSize(60, 0))
        self.sb_refreshTime.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.sb_refreshTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sb_refreshTime.setMinimum(100)
        self.sb_refreshTime.setMaximum(2000)
        self.sb_refreshTime.setSingleStep(100)
        self.sb_refreshTime.setDisplayIntegerBase(10)
        self.sb_refreshTime.setObjectName("sb_refreshTime")
        self.hbl_top.addWidget(self.sb_refreshTime)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.hbl_top.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.hbl_top)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_Plot = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Plot.sizePolicy().hasHeightForWidth())
        self.btn_Plot.setSizePolicy(sizePolicy)
        self.btn_Plot.setObjectName("btn_Plot")
        self.gridLayout.addWidget(self.btn_Plot, 0, 0, 2, 1)
        self.btn_Play = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Play.sizePolicy().hasHeightForWidth())
        self.btn_Play.setSizePolicy(sizePolicy)
        self.btn_Play.setObjectName("btn_Play")
        self.gridLayout.addWidget(self.btn_Play, 0, 2, 1, 1)
        self.btn_Stop = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Stop.sizePolicy().hasHeightForWidth())
        self.btn_Stop.setSizePolicy(sizePolicy)
        self.btn_Stop.setObjectName("btn_Stop")
        self.gridLayout.addWidget(self.btn_Stop, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.hbl1 = QtWidgets.QHBoxLayout()
        self.hbl1.setObjectName("hbl1")
        self.chart1 = MatplotWidget(Form)
        self.chart1.setObjectName("chart1")
        self.hbl1.addWidget(self.chart1)
        self.chart2 = MatplotWidget(Form)
        self.chart2.setObjectName("chart2")
        self.hbl1.addWidget(self.chart2)
        self.verticalLayout.addLayout(self.hbl1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lb_fps = QtWidgets.QLabel(Form)
        self.lb_fps.setMinimumSize(QtCore.QSize(40, 0))
        self.lb_fps.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_fps.setObjectName("lb_fps")
        self.horizontalLayout.addWidget(self.lb_fps)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Refresh time:"))
        self.label_2.setText(_translate("Form", " ms "))
        self.btn_Plot.setText(_translate("Form", "Plot"))
        self.btn_Play.setText(_translate("Form", "Play"))
        self.btn_Stop.setText(_translate("Form", "Stop"))
        self.label_3.setText(_translate("Form", "Frame rate:"))
        self.lb_fps.setText(_translate("Form", "0.0 Hz"))
from matplotWidget import MatplotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
