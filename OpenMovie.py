"""
The class file for instantiating movies so that their posters and other data may be accessed. 
"""
import os
import urllib.request
import sys
import logging
import re
import traceback
import json
import ORM
import bs4
import requests
import omdb
import datetime
import numpy as np
import pandas as pd

class OpenMovie:
    def __init__(self, title=""):
        """
        The constructor initializes the three fields and also creates the directory that the poster files will be stored in.
        """
        self.posterFileName = ""
        self.title = title
        # connect to omdb
        self.client = omdb.OMDBClient(apikey=os.environ['OMDB_API_KEY'])
        # get data
        try:
            self.movie = self.client.get(title=title)
        except:
            return
        # the directory is created in a try catch block since after first being created it will throw an exception when mkdir is called again.
        try:
            os.mkdir("Posters")
        except:
            pass
        return

    def getPoster(self):
        """
        This method gets the poster from the URL stored in the posterURL field.  
        """
        self.posterURL = self.movie['poster']
        # log that the method has been called, and on what movie
        logging.info("OpenMovie.getPoster called. Movie title: "+self.title+", Poster URL: "+self.posterURL)
        # strip the movie title of disallowed characters for file names
        dic = {"/": "_", "?": "_", ":":"_", " ":"_"}
        for i, j in dic.items():
            self.title = self.title.replace(i, j)
        self.posterFileName = self.title
        # use urlretrieve to get the file and put it in the posters directory
        try:
            fileName = self.posterFileName
            url = self.posterURL
            localFile, header = urllib.request.urlretrieve(url, "Posters/"+fileName+".jpg")
            return True
        # if urlretrieve does not work, use the traceback library to log error information
        except:
            return false         

    def getAwards(self):
    
        title = self.title
        client = omdb.OMDBClient(apikey=os.environ['OMDB_API_KEY'])
        movieData = client.get(title=title)
        imdbID = movieData['imdb_id']
        imdbAwardsURL = "https://www.imdb.com/title/{}/awards?ref_=tt_awd".format(
            movieData['imdb_id'])
        r = requests.get(imdbAwardsURL)
        soup = bs4.BeautifulSoup(r.text, 'lxml')
        table = soup.find('table', attrs={'class': 'awards'})

        rows = table.find_all('tr')

        winline = table.find('td',attrs={'class': 'title_award_outcome'} )
        numWins = 0
        if "Winner" in winline.text:
            numWins = int(winline['rowspan'])
        else:
            return False
        data = []
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])  # Get rid of empty

        temp = []
        temp.append(data[0][1])
        for i in range(1,numWins):
            temp.append(data[i][0]) 
        awardsList = "\n\n".join(temp)
        return awardsList

    def getMovieTitleData(self):
        movieQuery = ORM.session.query(ORM.Movies).filter_by(title=self.title).first()
        if (movieQuery != None):
            logging.info("movie found in database")

            return movieQuery
        else:
            logging.info("movie not found in database")
            raise exception 

    def getCrew(self):
        creditsQuery = ORM.session.query(ORM.Credits).filter_by(title=self.title).first()
        if (creditsQuery == None):
            logging.info("no director found")
            raise exception 
        director = None
        crew = eval(creditsQuery.crew)
        for c in crew:
            for k, v in c.items():
                if k == "job":
                    if c[k] == "Director":
                        director = c["name"]
        return creditsQuery, director            
    
    def getCast(self):
        castQuery = ORM.session.query(ORM.Credits).filter_by(title=self.title).first()
        if (castQuery == None):
            logging.info("no lead found")
            raise exception 
        cast = eval(castQuery.cast)
        lead = cast[0]["name"]
        return lead

    def analyzeMovie(self, year=None):

        startDate = "{}-01-01".format(year)
        endDate = "{}-01-01".format(year+1)

        yearSQL = """select * from public."movies" where release_date>'{}' and release_date <'{}';""".format(
            startDate, endDate)
        yearDataFrame = pd.read_sql(yearSQL, ORM.db.raw_connection())
        self.annualRevenueMean =np.nanmean(yearDataFrame['revenue'])
        self.annualRevenueMedian =np.nanmedian(yearDataFrame['revenue'])
        self.annualRevenueStd =np.nanstd(yearDataFrame['revenue'])
        self.annualBudgetMean =np.nanmean(yearDataFrame['budget'])
        self.annualBudgetMedian =np.nanmedian(yearDataFrame['budget'])
        self.annualBudgetStd =np.nanstd(yearDataFrame['budget'])