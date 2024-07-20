# backend/app/routes/main.py
from flask import Blueprint, jsonify

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return jsonify({"message": "Welcome to the Data Lineage Tracking API"})
