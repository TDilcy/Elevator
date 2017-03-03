# -*- utf-8 -*-
from PyQt4 import QtGui
# from PyQt4 import QtCore
# from model.elev import Ui_MainWindow
from model.elev_bak import Ui_MainWindow
from model.ElevatorCar import ElevatorCar


class RedefineUi(QtGui.QMainWindow):
    """docstring for RedefineUi"""

    def __init__(self):
        super(RedefineUi, self).__init__()
        # the UI created by the Qtdesigner
        self.ui = Ui_MainWindow()
        # use the QtGui.QMainWindow to initiate the UI
        self.ui.setupUi(self)
        self.WIDTH = self.ui.frame_1.geometry().width()
        self.HEIGHT = self.ui.frame_1.geometry().height()
        self.Y = self.ui.frame_1.geometry().y()
        self.X = self.ui.frame_1.geometry().x()
        self.setGeometry(500, 100, 700, 850)
        self.initFrames()
        self.init_splitters()
        self.elecars = self.initEleCars()

    def initFrames(self):
        self.ui.frame_2.setGeometry(self.frame_X(2), self.Y, self.WIDTH, self.HEIGHT)
        self.ui.frame_3.setGeometry(self.frame_X(3), self.Y, self.WIDTH, self.HEIGHT)
        self.ui.frame_4.setGeometry(self.frame_X(4), self.Y, self.WIDTH, self.HEIGHT)
        self.ui.frame_5.setGeometry(self.frame_X(5), self.Y, self.WIDTH, self.HEIGHT)
        self.ui.frame_6.setGeometry(self.frame_X(6), self.Y, self.WIDTH, self.HEIGHT)
        self.ui.frame_7.setGeometry(self.frame_X(7), self.Y, self.WIDTH, self.HEIGHT)

    def init_splitters(self):
        S_WIDTH = self.WIDTH * 0.8
        S_HEIGHT = S_WIDTH
        S_Y = self.Y + self.HEIGHT + 30
        self.ui.splitter_1.setGeometry(self.splitter_X(1), S_Y, S_WIDTH, S_HEIGHT)
        self.ui.splitter_2.setGeometry(self.splitter_X(2), S_Y, S_WIDTH, S_HEIGHT)
        self.ui.splitter_3.setGeometry(self.splitter_X(3), S_Y, S_WIDTH, S_HEIGHT)
        self.ui.splitter_4.setGeometry(self.splitter_X(4), S_Y, S_WIDTH, S_HEIGHT)
        self.ui.splitter_5.setGeometry(self.splitter_X(5), S_Y, S_WIDTH, S_HEIGHT)
        self.ui.splitter_6.setGeometry(self.splitter_X(6), S_Y, S_WIDTH, S_HEIGHT)
        self.ui.splitter_7.setGeometry(self.splitter_X(7), S_Y, S_WIDTH, S_HEIGHT)

    def splitter_X(self, n):
        return self.X + (2 * n - 1) * self.WIDTH * 0.1 + (n - 1) * self.WIDTH * 0.8

    def frame_X(self, n):
        return self.X + (n - 1) * self.WIDTH

    def initEleCars(self):
        '''
        initiate the ele_box in the gui, return a list contains all of them
        '''
        # margin = self.ui.frame_1.geometry().x() # self.ui.frame_1.height()
        HEIGHT = 30
        WIDTH = self.ui.frame_1.width()
        elecar1 = ElevatorCar(1, self)
        # thread1 = QtCore.QThread()
        # elecar1.moveToThread(thread1)
        # thread1.started.connect(elecar1.moveUp)
        elecar1.setGeometry(self.ui.frame_1.geometry().x(), 275, WIDTH, HEIGHT)
        elecar2 = ElevatorCar(2, self)
        elecar2.setGeometry(self.ui.frame_2.geometry().x(), 275, WIDTH, HEIGHT)
        elecar3 = ElevatorCar(3, self)
        elecar3.setGeometry(self.ui.frame_3.geometry().x(), 275, WIDTH, HEIGHT)
        elecar4 = ElevatorCar(4, self)
        elecar4.setGeometry(self.ui.frame_4.geometry().x(), 275, WIDTH, HEIGHT)
        elecar5 = ElevatorCar(5, self)
        elecar5.setGeometry(self.ui.frame_5.geometry().x(), 275, WIDTH, HEIGHT)
        elecar6 = ElevatorCar(6, self)
        elecar6.setGeometry(self.ui.frame_6.geometry().x(), 275, WIDTH, HEIGHT)
        elecar7 = ElevatorCar(7, self)
        elecar7.setGeometry(self.ui.frame_7.geometry().x(), 275, WIDTH, HEIGHT)
        return [elecar1, elecar2, elecar3, elecar4, elecar5, elecar6, elecar7]

    def up(self, order):
        self.elecars[order].moveUp()
        self.elecars[order].thread.obj_signal.connect(self.move)

    def down(self, order):
        self.elecars[order].moveDown()
        self.elecars[order].thread.obj_signal.connect(self.move)

    def move(self, ele):
        '''
        important issue: the refresh operation should be put at the main thread rather than the sub-thread, otherwise, it will crash.
        '''
        # # the x, y position of the elebox
        x = ele.geometry().x()
        y = ele.geometry().y()
        top_margin = 50
        buttom_margin = 650
        if ele.direction == "up":
            step = -2
        elif ele.direction == "down":
            step = 2
        y += step
        QtGui.QApplication.processEvents()
        while (y <= buttom_margin) & (y >= top_margin):
            ele.move(x, y)
            break

    def showFloor(self, ele):
        '''
        show which flow does the elecar locate in the correspondant lcd
        '''
        y = ele.geometry().y()
        # top_margin = 50
        lcds = [self.ui.lcd1, self.ui.lcd2, self.ui.lcd3, self.ui.lcd4, self.ui.lcd5, self.ui.lcd6, self.ui.lcd7]
        lcd_selected = lcds[self.elecars.index(ele)]
        # calculate the floor
        lcd_selected.display(sum(map(lambda j: (10 - j) if (50 + 65 * j) <= y < (50 + 65 * (j + 1)) else 0, range(10))))
