#!/usr/bin/python3
"""starts a Flask web application"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', strict_slashes=False, methods=['GET'])
def status():
    """return status"""
    return (jsonify({"status": "OK"}), 200)


@app_views.route('/stats', strict_slashes=False, methods=['GET'])
def stats():
    """return stats"""
    return (jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")}), 200)