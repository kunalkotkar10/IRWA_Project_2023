from flask import Flask, render_template, request
from websiteSearchCopy import get_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    apts = ()
    if request.method == 'POST':
        text = request.form['text']
        apts = get_data(text)
    return render_template('index.html', apts=apts)

def process_text(text):
    # Replace this with your own processing function
    return text.upper()

if __name__ == '__main__':
    app.run(debug=True)
