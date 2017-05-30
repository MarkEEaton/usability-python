from flask import Flask, request, render_template
from openpyxl import load_workbook
from openpyxl.utils.datetime import datetime_to_W3CDTF
import cohort
import re
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

@app.route('/', methods=['GET'])
def submit():
    try:
        prototype = request.args.get('prototype')
        element = request.args.get('element')
        if re.compile(r'[^_a-zA-Z]').search(element):
            return render_template("failed regex on element")
        if re.compile(r'[^0-9]').search(prototype):
            return render_template("failed regex on prototype")
        else:
            worksheet.append([date_to_string(), cohort.cohort, prototype, element])
            workbook.save('/home/b7jl/usability/data.xlsx')
    except Exception as e:
        print('There\'s been an error')
        print(e)
    return render_template('completed.html')

if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1', debug=True)
