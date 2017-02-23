# -*- utf-8 -*-
from PyQt4 import QtGui
from model.elev import Ui_MainWindow
from model.ElevatorCar import ElevatorCar


class RedefineUi(QtGui.QMainWindow):
    """docstring for RedefineUi"""

    def __init__(self):
        super(RedefineUi, self).__init__()
        # the UI created by the Qtdesigner
        self.ui = Ui_MainWindow()
        # use the QtGui.QMainWindow to initiate the UI
        self.ui.setupUi(self)
        self.setGeometry(500, 100, 800, 800)
        self.elecars = self.initBox()

    def initBox(self):
        '''
        initiate the ele_box in the gui, return a list contains all of them
        '''
        HEIGHT = self.ui.EleButton1Up.height()
        WIDTH = self.ui.EleButton1Up.width()
        EleBox1 = ElevatorCar(1, self)
        EleBox1.setGeometry(100, 275, WIDTH, HEIGHT)
        EleBox2 = ElevatorCar(2, self)
        EleBox2.setGeometry(270, 275, WIDTH, HEIGHT)
        EleBox3 = ElevatorCar(3, self)
        EleBox3.setGeometry(440, 275, WIDTH, HEIGHT)
        EleBox4 = ElevatorCar(4, self)
        EleBox4.setGeometry(600, 275, WIDTH, HEIGHT)
        return [EleBox1, EleBox2, EleBox3, EleBox4]
