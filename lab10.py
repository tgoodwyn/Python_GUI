#! /usr/bin/env python3
import configparser
import json
import logging
import sys
import OpenMovie

import PyQt5
import UI
import os
import pandas as pd
import sqlalchemy
import sqlalchemy.ext.declarative
import ORM
import bs4
import requests
import omdb

if __name__ == "__main__":
    # config and log
    # instantiate a configparser and read in the associated config file
    try:
        config = configparser.RawConfigParser()
        config.read("movies.cfg")
    except OSError:
        print("Config fail")
        sys.exit(-1)
    # currently the config file just has the name of the log file that will be used for the program
    log_file_name = ""
    if config.has_section('LOGGING'):
        log_file_name = config['LOGGING']['LOG_FILE']
    else:
        log_file_name = "default.log"
    # set up the log file
    try:
        logging.basicConfig(filename=log_file_name,
                            level=logging.DEBUG,
                            format=
                            '%(asctime)s,%(levelname)s,%(message)s',
                            datefmt=
                            '%m/%d/%Y %I:%M:%S %p')
    except:
        print ("Failed to open log file %s" % (log_file_name))
        sys.exit(-1)
    logging.info("Program Started...")

    # starting gui
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    gui = UI.UI()
    gui.show()
    app.exec_()

