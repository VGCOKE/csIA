from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///./restaurant.db'

CORS(app, resources={r"/*": {"origins": "http://localhost:5173", "allow_headers": "Content-Type"}}) 
db.init_app(app)

from routes import register_routes
register_routes(app, db)

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)