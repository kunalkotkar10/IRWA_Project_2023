from flask import Flask, render_template, request, make_response
# from websiteSearchCopy import get_data
from housing_search import get_data, get_sortedData
import pandas as pd

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    apts = pd.DataFrame({'Name': [], 'Link': [], 'Price': [], 'Beds': [], 'Bath': []})
    if request.method == 'POST':
        text = request.form['text']
        apts = get_data(text)
        # print(apts)
    return render_template('index.html', apts=apts)

@app.route('/sort', methods=['GET','POST'])
def sort():
    apts = pd.DataFrame({'Name': [], 'Link': [], 'Price': [], 'Beds': [], 'Bath': []})
    sort_type = request.form['value']
    print(sort_type)
    apts = get_sortedData(sort_type)
    print(f'In Python: {apts}')
    # response = make_response(render_template('index.html', apts=get_sortedData(sort_type)))
    # response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    # return response
    return render_template('index.html', apts = get_sortedData(sort_type))
    # return render_template('index.html', apts=apts)
    # return render_template('index.html', apts=apts)
    # return '<html><body><h1>Hello, World!</h1></body></html>'

if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
