from flask import Flask, request, render_template
from openpyxl.utils.datetime import datetime_to_W3CDTF
import cohort
import logging
from pytz import timezone
from datetime import datetime as dt

app = Flask(__name__)


def date_to_string():
    eastern = timezone('US/Eastern')
    date_str = datetime_to_W3CDTF(dt.now(eastern))
    date_str = date_str.replace('T', ' ')
    date_str = date_str.replace('Z', '')
    return date_str


logging.basicConfig(filename='/home/b7jl/usability/debuglog.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info('instantiated')


@app.route('/', methods=['GET'])
def submit():
    try:
        logging.info('in the route')
        prototype = str(request.args.get('prototype'))
        element = str(request.args.get('element'))
        data = date_to_string() + ',' + cohort.cohort\
                                + ',' + prototype\
                                + ',' + element\
                                + '\n'
        with open('./usability/data.csv', 'a') as f:
            f.write(data)
    except Exception as e:
        logging.warning('threw an exception')
        logging.exception('message')
    return render_template('completed.html')


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1', debug=True)
