from flask import Blueprint, jsonify, request
from app.services.user_service import UserService

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/users', methods=['GET'])
def get_users():
    users = UserService.get_all_users()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users]), 200

@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200
    return jsonify({"message": "User not found"}), 404

@user_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = UserService.create_user(data['name'], data['email'])
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201

@user_blueprint.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = UserService.update_user(user_id, data['name'], data['email'])
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200
    return jsonify({"message": "User not found"}), 404

@user_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = UserService.delete_user(user_id)
    if user:
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"message": "User not found"}), 404