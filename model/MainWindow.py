# -*- coding: utf-8 -*-
from model.RedefineUi import RedefineUi


class MainWindow(RedefineUi):
    """docstring for MainWindow"""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui.EleButton1Up.clicked.connect(self.elecars[0].moveUp)
        self.ui.EleButton2Up.clicked.connect(self.elecars[1].moveUp)
        self.ui.EleButton3Up.clicked.connect(self.elecars[2].moveUp)
        self.ui.EleButton4Up.clicked.connect(self.elecars[3].moveUp)
        self.ui.EleButton1Down.clicked.connect(self.elecars[0].moveDown)
        self.ui.EleButton2Down.clicked.connect(self.elecars[1].moveDown)
        self.ui.EleButton3Down.clicked.connect(self.elecars[2].moveDown)
        self.ui.EleButton4Down.clicked.connect(self.elecars[3].moveDown)
