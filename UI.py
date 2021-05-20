
import PyQt5
import PyQt5.QtWidgets
import UI_CentralWindow
import json
import OpenMovie
import ORM
import PyQt5.QtGui
from PyQt5.QtWidgets import QWidget, QShortcut
from PyQt5.QtGui import QKeySequence

class UI(PyQt5.QtWidgets.QMainWindow):
    '''
    Our top level UI widget
    '''
    def __init__(self, parent=None, moviesJSON=None):
        super(UI, self).__init__(parent)
        self.moviesJSON = moviesJSON
        self.setWindowTitle('Python Movie Project')
        self.statusBar().showMessage('Status Bar')

        self.centralWidget = UI_CentralWindow.UI_CentralWindow()
        self.centralWidget.enterMoviePushButton.clicked.connect(self.enterMoviePushButtonClicked)
        
        # shortcut keys added for performing search and closing window
        self.shortcut = QShortcut(QKeySequence("Ctrl+W"), self)
        self.shortcut.activated.connect(self.close)
        self.shortcut = QShortcut(QKeySequence("Ctrl+T"), self)
        self.shortcut.activated.connect(self.enterMoviePushButtonClicked)

        self.setCentralWidget(self.centralWidget)
        self.show()

    def enterMoviePushButtonClicked(self):
        text = self.centralWidget.enterMovieLineEdit.text()
        movie = OpenMovie.OpenMovie(title=text)
        # next query the database for the data based on the title
        try:
            movieTitleQuery = movie.getMovieTitleData()
        # if its not found then do nothing 
        except:
            return
        # next see if you can get the poster, if not display the text "no poster"
        try:
            movie.getPoster()
            fileName = "Posters/"+movie.posterFileName
            self.centralWidget.updatePoster(fileName)
        except:
            self.centralWidget.posterlabel.setText("No Poster")
        # now populate all the info fields
        try:
            creditsQuery, director = movie.getCrew()
        except:
            director = ""
        try:
            lead = movie.getCast()
        except:
            lead = ""
        release_date = movieTitleQuery.release_date
        budget = str(movieTitleQuery.budget)
        revenue = str(movieTitleQuery.revenue)
        runtime = str(round(movieTitleQuery.runtime, 2))
        vote_count = str(round(movieTitleQuery.vote_count, 2))
        vote_average = str(round(movieTitleQuery.vote_average, 2))
        status = movieTitleQuery.status
        self.centralWidget.actorinformation.infoLabel.setText(lead)
        self.centralWidget.directioninformation.infoLabel.setText(director)
        self.centralWidget.releaseDateInformation.infoLabel.setText(release_date)
        self.centralWidget.budgetinformation.infoLabel.setText(budget)
        self.centralWidget.revenueinformation.infoLabel.setText(revenue)
        self.centralWidget.runTimeInformation.infoLabel.setText(runtime)
        self.centralWidget.voteCountInformation.infoLabel.setText(vote_count)
        self.centralWidget.voteAverageInformation.infoLabel.setText(vote_average)
        self.centralWidget.statusinformation.infoLabel.setText(status)
        
        # set the textEdit box with the list of awards
        awardsList = ""
        try:
            awardsList = movie.getAwards()
        except:
            self.centralWidget.awardsDisplay.setText("No awards") 
        self.centralWidget.awardsDisplay.setText(awardsList) 
        year = int(release_date.split("-")[0])
        movie.analyzeMovie(year)
        arm = movie.annualRevenueMean

        self.centralWidget.annualBudgetMeanInformation.infoLabel.setText(str(movie. annualBudgetMean))
        self.centralWidget.annualBudgetMedianInformation .infoLabel.setText(str(movie.annualBudgetMedian))
        self.centralWidget.annualBudgetStdInformation .infoLabel.setText(str(movie.annualBudgetStd))
        self.centralWidget.annualRevenueMeanInformation .infoLabel.setText(str(movie.annualRevenueMean))
        self.centralWidget.annualRevenueMedianInformation.infoLabel.setText(str(movie.annualRevenueMedian))
        self.centralWidget.annualRevenueStdInformation  .infoLabel.setText(str(movie.annualRevenueStd))