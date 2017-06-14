# usability-python

This Flask application was developed to record usability testing data from a series of LibGuides prototypes.

Parameters about each usability test, which were hardcoded into the urls of the LiibGuides prototypes, are passed to the Flask application in a GET request. The Flask application parses these arguments and saves them in a CSV file, along with a timestamp and data about the cohort.

The purpose of this is to aggregate data from many usability tests into one dataset that can be handled by Excel.
