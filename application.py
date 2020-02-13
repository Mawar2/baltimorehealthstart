import os, flask
from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
@app.route('/')

def index():
    return flask.render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        client = request.form['client']
        education = request.form['education']
        firstTime = request.form['BHS']
        comments = request.form['comments']
        
        # validation
        if client == '' or comments == '':
            return render_template('index.html', message="Please fill out all required information.")
        #print(client, education, firstTime, comments)
        return render_template('success.html')


app.run(
    port=int(os.getenv('PORT', 8089)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)

if __name__ == '__main__':
    app.run(debug=True)