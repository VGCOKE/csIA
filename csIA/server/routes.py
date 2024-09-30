from flask import render_template, request, jsonify
from fastapi.encoders import jsonable_encoder
from models import Restaurant, History
import googlemaps
import time

def register_routes(app, db):
    
    @app.route('/history', methods=['GET'])
    def all_history():
        history = History.query.all()
        return jsonable_encoder({
            'history': history
        })
    
    @app.route('/history/<place_id>', methods=['GET'])
    def history_detail(place_id):
        #record = History.query.get(placeid)
        record = History.query().filter_by(History.placeid == place_id).first()
        for record in History:
            if History['placeid'] == place_id:
                return jsonable_encoder({'record': record})
    
    @app.route('/', methods=['GET'])
    def all_restaurants():
        restaurants = Restaurant.query.all()
        return jsonable_encoder({
            'restaurant': restaurants
        })
    
    