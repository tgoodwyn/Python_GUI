
import PyQt5
import PyQt5.QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
# try class UI(PyQt5.QtWidgets.QDialog): if that doesnt work
class UI_MovieInfo(PyQt5.QtWidgets.QDialog):
    def __init__(self, parent=None, title=None):
        """
        The class for the movie info boxes
        """
        super(UI_MovieInfo, self).__init__(parent)
        # self.parent = parent
        # self.title = title
        self.titleLabel = QLabel(title)
        self.infoLabel = QLabel("Info")
        self.hbox= QHBoxLayout()        
        titleLabelFont = QFont()
        titleLabelFont.setBold(True)
        self.titleLabel.setFont(titleLabelFont)
        self.hbox.addWidget(self.titleLabel)
        self.hbox.addWidget(self.infoLabel)
        return

    def getLayout(self):
        return self.hbox
