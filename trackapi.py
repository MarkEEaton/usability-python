from flask import Flask, request, render_template
from openpyxl import load_workbook
import cohort
from datetime import datetime as dt

app = Flask(__name__)

workbook = load_workbook(filename='data.xlsx')
worksheet = workbook.active

@app.route('/', methods=['GET'])
def submit():
    try:
        prototype = request.args.get('prototype')
        element = request.args.get('element')
        worksheet.append([dt.now(), cohort.cohort, prototype, element])
        workbook.save('data.xlsx')
    except e:
        print('There\'s been an error')
        print(e)
    return 'hello world'

if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1', debug=True)
