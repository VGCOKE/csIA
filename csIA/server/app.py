from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///history.db' 
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)