from flask import Blueprint, jsonify, request
from app.models import Item # Import the Item model

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return jsonify({'message': 'Welcome to the API'})


@bp.route('/api/items', methods=['GET'])
def get_items():
    items = [item.to_dict() for item in Item.get_all_items()]
    return jsonify({'items': items})


@bp.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.get_item_by_id(item_id)
    if item:
        return jsonify(item.to_dict())
    return jsonify({'message': 'Item not found'}), 404


@bp.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'message': 'Missing name in request body'}), 400

    name = data['name']
    description = data.get('description') # Description is optional

    new_item = Item.add_item(name, description)
    return jsonify(new_item.to_dict()), 201
