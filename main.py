from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create flask app instance
app = Flask(__name__)
app.debug = True

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jeffkim:kim@localhost:5432/nse_data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


@app.route('/')
def index():
    return '<h1>Learn something interesting</h1>'


if __name__ == '__main__':
    app.run()
