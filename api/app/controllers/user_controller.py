from flask import Blueprint, jsonify, request
from app.services.user_service import UserService

user_blueprint = Blueprint('user_blueprint', __name__)

# Get all users
@user_blueprint.route('/users', methods=['GET'])
def get_users():
    """Retrieve all users."""
    users = UserService.get_all_users()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users]), 200

# Get a specific user by ID
@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieve a specific user by ID."""
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200
    return jsonify({"message": "User not found"}), 404

# Create a new user
@user_blueprint.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""
    data = request.get_json()
    try:
        user = UserService.create_user(data['name'], data['email'])
        return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

# Update an existing user
@user_blueprint.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update an existing user."""
    data = request.get_json()
    try:
        user = UserService.update_user(user_id, data['name'], data['email'])
        if user:
            return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200
        return jsonify({"message": "User not found"}), 404
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

# Delete a user
@user_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user if they have no associated bank accounts."""
    try:
        user = UserService.delete_user(user_id)
        if user:
            return jsonify({"message": "User deleted"}), 200
        return jsonify({"message": "User not found"}), 404
    except ValueError as e:
        return jsonify({"message": str(e)}), 400