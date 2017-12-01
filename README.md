# usability-python

This Flask application was developed to record usability testing data from a series of LibGuides prototypes.

Parameters about each usability test, which were hardcoded into the urls of the LibGuides prototypes, are passed to the Flask application in a GET request. The Flask application parses these arguments and saves them in a CSV file, along with a timestamp and data about the cohort.

The purpose of this is to aggregate data from many usability tests into one dataset that can be handled by Excel.

This repo is part of a larger project that was presented at SUNYLA 2017 at Stony Brook University. A powerpoint from that presentation is included in this repo. Please also take a look at the related repository, [markeeaton/usability-testing-interface](http://github.com/markeeaton/usability-testing-interface). 

This project was also presented at the CUNY IT Conference 2017. The slide deck for that conference will be added soon.
