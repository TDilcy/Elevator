import time
from PyQt4 import QtGui, QtCore
'''
It is the second version:
changelog:
    Make a Elevator owns only one thread rather than two when moveUp and moveDown is called seperately, so that fix the problem that the shadow occurs when an object with two thread running at the same time(duo to redrawing at the same time)
'''


class ElevatorCar(QtGui.QLabel):
    """
    elevatorcar inherited from the Qlabel and add a method to move up and down
    """

    def __init__(self, order, parent=None, direction=None):
        super(ElevatorCar, self).__init__(parent)
        self.order = order
        self.setupUi()
        self.direction = direction
        self.thread = EleMove(self, self.direction)

    def setupUi(self):
        self.setFrameShape(QtGui.QFrame.Box)
        self.setFrameShadow(QtGui.QFrame.Sunken)
        self.setText("EleBox %s" % str(self.order))
        # self.setAlignment()

    def moveUp(self):
        self.thread.setDirection("up")
        # quit before start
        self.thread.terminate()
        self.thread.start()

    def moveDown(self):
        self.thread.setDirection("down")
        self.thread.terminate()
        self.thread.start()

    # def stop(self, cur_thread):
    #     cur_thread.quit()


class EleMove(QtCore.QThread):
    """
    Rewrite the run method of QThread to realize the movement inside a independent thread
    changelog:
        add the method to change the direction
    """
    handle_id_signal = QtCore.pyqtSignal(QtCore.QThread)

    def __init__(self, ele, direction):
        super(EleMove, self).__init__()
        self.ele = ele
        self.direction = direction

    def setDirection(self, direction):
        self.direction = direction

    def run(self):
        # the x, y position of the elebox
        x = self.ele.geometry().x()
        y = self.ele.geometry().y()
        # set the top and buttom bound
        top_margin = 50
        buttom_margin = 450
        if self.direction == "up":
            step = -2
        elif self.direction == "down":
            step = 2
        for i in range(100):
            # limit the movement between the bound
            while (y < buttom_margin) & (y > top_margin):
                self.ele.move(x, y)
                # self.ele.setText("%s %d" % (self.direction, disp))
                y += step
                # use processEvent to redraw the gui
                QtGui.QApplication.processEvents()
                self.handle_id_signal.emit(self.currentThread())
                time.sleep(0.05)
