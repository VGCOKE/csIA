from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///history.db' 
db = SQLAlchemy(app)

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    restaurant_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)

db.create_all() 

@app.route('/api/history', methods=['GET'])
def get_history():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int) 

    history_records = History.query.paginate(page=page, per_page=per_page, error_out=False)
    records = [{'id': record.id, 'date': record.date, 'time': record.time, 'restaurantName': record.restaurant_name, 'address': record.address} for record in history_records.items]
    return jsonify({'data': records, 'total_pages': history_records.pages})

@app.route('/api/history', methods=['POST'])
def add_history():
    new_record = request.get_json()
    history = History(date=new_record['date'], time=new_record['time'], restaurant_name=new_record['restaurantName'], address=new_record['address'])
    db.session.add(history)
    db.session.commit()
    return jsonify({'message': 'History record added!'}), 201

if __name__ == '__main__':
    app.run(debug=True)