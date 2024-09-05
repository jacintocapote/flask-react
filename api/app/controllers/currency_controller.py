from flask import Blueprint, jsonify, request
from app.services.currency_service import CurrencyService

currency_blueprint = Blueprint('currency_blueprint', __name__)

@currency_blueprint.route('/currencies', methods=['GET'])
def get_currencies():
    currencies = CurrencyService.get_all_currencies()
    return jsonify([{"id": c.id, "name": c.name, "representation": c.representation} for c in currencies]), 200

@currency_blueprint.route('/currencies/<string:currency_id>', methods=['GET'])
def get_currency(currency_id):
    currency = CurrencyService.get_currency_by_id(currency_id)
    if currency:
        return jsonify({"id": currency.id, "name": currency.name, "representation": currency.representation}), 200
    return jsonify({"message": "Currency not found"}), 404

@currency_blueprint.route('/currencies', methods=['POST'])
def create_currency():
    data = request.get_json()
    currency = CurrencyService.create_currency(data['id'], data['name'], data['representation'])
    return jsonify({"id": currency.id, "name": currency.name, "representation": currency.representation}), 201

@currency_blueprint.route('/currency/<string:currency_id>', methods=['DELETE'])
def delete_currency(currency_id):
    currency = CurrencyService.delete_currency(currency_id)
    if currency:
        return jsonify({"message": "Currency deleted"}), 200
    return jsonify({"message": "Currency not found"}), 404