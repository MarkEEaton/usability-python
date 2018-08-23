# usability-python

This Flask application was developed to record usability testing data from a series of LibGuides prototypes.

Parameters about each usability test, which were hardcoded into the urls of the LibGuides prototypes, are passed to the Flask application in a GET request. The Flask application parses these arguments and saves them in a CSV file, along with a timestamp and data about the cohort.

The purpose of this is to aggregate data from many usability tests into one dataset that can be handled by Excel.

This repo is part of a larger project undertaken with Prof. Carlos Arguelles. Findings were presented at SUNYLA 2017 at Stony Brook University. A powerpoint from that presentation is included in this repo.  Subsequently, this project was also presented at the CUNY IT Conference 2017 ([slide deck](https://academicworks.cuny.edu/cgi/viewcontent.cgi?article=1217&context=ny_pubs)), and ACRL NEC 2018.

Please also take a look at the related repository, [markeeaton/usability-testing-interface](http://github.com/markeeaton/usability-testing-interface).
