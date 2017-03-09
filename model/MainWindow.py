# -*- coding: utf-8 -*-
from model.RedefineUi import RedefineUi


class MainWindow(RedefineUi):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui.EleButton1Up.clicked.connect(lambda: self.up(0))
        self.ui.EleButton2Up.clicked.connect(lambda: self.up(1))
        self.ui.EleButton3Up.clicked.connect(lambda: self.up(2))
        self.ui.EleButton4Up.clicked.connect(lambda: self.up(3))
        self.ui.EleButton5Up.clicked.connect(lambda: self.up(4))
        self.ui.EleButton6Up.clicked.connect(lambda: self.up(5))
        self.ui.EleButton7Up.clicked.connect(lambda: self.up(6))
        self.ui.EleButton1Down.clicked.connect(lambda: self.down(0))
        self.ui.EleButton2Down.clicked.connect(lambda: self.down(1))
        self.ui.EleButton3Down.clicked.connect(lambda: self.down(2))
        self.ui.EleButton4Down.clicked.connect(lambda: self.down(3))
        self.ui.EleButton5Down.clicked.connect(lambda: self.down(4))
        self.ui.EleButton6Down.clicked.connect(lambda: self.down(5))
        self.ui.EleButton7Down.clicked.connect(lambda: self.down(6))

        # show the floor of the elevator
        self.elecars[0].thread.obj_signal.connect(self.showFloor)
        self.elecars[1].thread.obj_signal.connect(self.showFloor)
        self.elecars[2].thread.obj_signal.connect(self.showFloor)
        self.elecars[3].thread.obj_signal.connect(self.showFloor)
        self.elecars[4].thread.obj_signal.connect(self.showFloor)
        self.elecars[5].thread.obj_signal.connect(self.showFloor)
        self.elecars[6].thread.obj_signal.connect(self.showFloor)
