
import PyQt5
import PyQt5.QtWidgets
import PyQt5.QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from UI_MovieInfo import UI_MovieInfo
# try class UI(PyQt5.QtWidgets.QDialog): if that doesnt work
class UI_CentralWindow(PyQt5.QtWidgets.QDialog):
    def __init__(self, parent=None):
        """
        The class for organizing the central window
        """
        super(UI_CentralWindow, self).__init__(parent)

        # with Qlabels second arg of self may be necessary
        enterMovieLabel = QLabel("Movie to Look Up")
        
        self.enterMovieLineEdit = QLineEdit()
        self.enterMoviePushButton = QPushButton("Look Up Movie")

        self.posterlabel = QLabel("Poster Goes Here")
        # no example of pixmap in src
        self.pixmap = QPixmap()
        # see ui_widget
        self.awardsDisplay = QTextEdit()
        self.awardsDisplay.setReadOnly(True)

        # see simple_layout_example for hbox and vbox creation
        vbox = PyQt5.QtWidgets.QVBoxLayout()
        vboxInfo = PyQt5.QtWidgets.QVBoxLayout()

        hboxSearch = PyQt5.QtWidgets.QHBoxLayout()
        hboxInfoAndPoster = PyQt5.QtWidgets.QHBoxLayout()
        hboxInfo1 = PyQt5.QtWidgets.QHBoxLayout()
        hboxInfo2 = PyQt5.QtWidgets.QHBoxLayout()
        hboxInfo3 = PyQt5.QtWidgets.QHBoxLayout()
        hboxInfo4 = PyQt5.QtWidgets.QHBoxLayout()
        hboxInfo5 = PyQt5.QtWidgets.QHBoxLayout()
        

        self.directioninformation = UI_MovieInfo(title="Director")
        self.actorinformation = UI_MovieInfo(title="Actor")
        self.releaseDateInformation = UI_MovieInfo(title="Release Date")


        self.budgetinformation = UI_MovieInfo(title="Budget")
        self.revenueinformation = UI_MovieInfo(title="Revenue")
        self.runTimeInformation = UI_MovieInfo(title="Run Time")

        self.voteCountInformation = UI_MovieInfo(title="Vote Count")
        self.voteAverageInformation = UI_MovieInfo(title="Vote Average")
        self.statusinformation = UI_MovieInfo(title="Status")

        self.annualBudgetMeanInformation = UI_MovieInfo(title="Annual Budget Mean")
        self.annualBudgetMedianInformation = UI_MovieInfo(title="Annual Budget Median")
        self.annualBudgetStdInformation = UI_MovieInfo(title="Annual Budget STD")

        self.annualRevenueMeanInformation = UI_MovieInfo(title="Annual Revenue Mean")
        self.annualRevenueMedianInformation = UI_MovieInfo(title="Annual Revenue Median")
        self.annualRevenueStdInformation = UI_MovieInfo(title="Annual Revenue STD")

        # see simplelayoutex for adding layout, widget
        hboxSearch.addWidget(enterMovieLabel)
        hboxSearch.addWidget(self.enterMovieLineEdit)
        hboxSearch.addWidget(self.enterMoviePushButton)

        hboxInfo1.addLayout(self.directioninformation.getLayout())  
        hboxInfo1.addLayout(self.actorinformation.getLayout())      
        hboxInfo1.addLayout(self.releaseDateInformation.getLayout())
        
        hboxInfo2.addLayout(self.voteCountInformation.getLayout())
        hboxInfo2.addLayout(self.voteAverageInformation.getLayout())
        hboxInfo2.addLayout(self.statusinformation.getLayout())

        hboxInfo3.addLayout(self.budgetinformation.getLayout())
        hboxInfo3.addLayout(self.revenueinformation.getLayout())
        hboxInfo3.addLayout(self.runTimeInformation.getLayout())

        hboxInfo4.addLayout(self.annualBudgetMeanInformation.getLayout())
        hboxInfo4.addLayout(self.annualBudgetMedianInformation.getLayout())
        hboxInfo4.addLayout(self.annualBudgetStdInformation.getLayout())

        hboxInfo5.addLayout(self.annualRevenueMeanInformation.getLayout())
        hboxInfo5.addLayout(self.annualRevenueMedianInformation.getLayout())
        hboxInfo5.addLayout(self.annualRevenueStdInformation.getLayout())

        hboxInfoAndPoster.addWidget(self.posterlabel)
        hboxInfoAndPoster.addWidget(self.awardsDisplay)

        vboxInfo.addLayout(hboxInfo1)
        vboxInfo.addLayout(hboxInfo2)
        vboxInfo.addLayout(hboxInfo3)
        vboxInfo.addLayout(hboxInfo4)
        vboxInfo.addLayout(hboxInfo5)
        
        hboxInfoAndPoster.addLayout(vboxInfo)

        vbox.addLayout(hboxSearch)
        vbox.addLayout(hboxInfoAndPoster)
        
        # see simpex 
        self.setLayout(vbox)
        return

    def updatePoster(self, posterFileName=None):
        self.pixmap = QPixmap(posterFileName)
        scaled = self.pixmap.scaled(self.posterlabel.size(), PyQt5.QtCore.Qt.KeepAspectRatio)
        self.posterlabel.setPixmap(scaled)
        self.posterlabel.setScaledContents(False)
        return