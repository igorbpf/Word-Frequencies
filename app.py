import os
from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import Result

@app.route('/', methods=['GET','POST'])
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run()


