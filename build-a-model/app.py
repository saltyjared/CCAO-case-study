from flask import Flask, render_template
import pandas as pd
from data import df

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', data=df.columns)

if __name__ == '__main__':
    app.run(debug=True)