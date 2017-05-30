from flask import Flask, request, render_template
from openpyxl import load_workbook
from openpyxl.utils.datetime import datetime_to_W3CDTF
import cohort
import re
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

workbook = load_workbook(filename='/home/b7jl/usability/data.xlsx')
worksheet = workbook.active

logging.basicConfig(filename='/home/b7jl/usability/debuglog.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info('instantiated')

@app.route('/', methods=['GET'])
def submit():
    try:
        logging.info('in the route')
        prototype = request.args.get('prototype')
        element = request.args.get('element')
        logging.debug('type of variable prototype: %s', type(prototype))
        logging.debug('type of variable element: %s', type(element))
        if re.compile(r'[^_a-zA-Z]').search(str(element)):
            return 
        if re.compile(r'[^0-9]').search(str(prototype)):
            return
        else:
            worksheet.append([date_to_string(), cohort.cohort, prototype, element])
            workbook.save('/home/b7jl/usability/data.xlsx')
    except Exception as e:
        logging.warning('threw an exception')
        logging.exception('message')
    return render_template('completed.html')

if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1', debug=True)
