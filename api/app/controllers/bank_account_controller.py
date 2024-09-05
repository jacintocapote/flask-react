from flask import Blueprint, jsonify, request
from app.services.bank_account_service import BankAccountService

account_blueprint = Blueprint('account_blueprint', __name__)

@account_blueprint.route('/accounts', methods=['GET'])
def get_accounts():
    accounts = BankAccountService.get_all_accounts()
    return jsonify([{"id": acc.id, "account_number": acc.account_number, "balance": acc.balance} for acc in accounts]), 200

@account_blueprint.route('/accounts/<int:account_id>', methods=['GET'])
def get_account(account_id):
    account = BankAccountService.get_account_by_id(account_id)
    if account:
        return jsonify({"id": account.id, "account_number": account.account_number, "balance": account.balance}), 200
    return jsonify({"message": "Account not found"}), 404

@account_blueprint.route('/accounts', methods=['POST'])
def create_account():
    data = request.get_json()
    account = BankAccountService.create_account(data['account_number'], data['balance'], data['user_id'])
    return jsonify({"id": account.id, "account_number": account.account_number, "balance": account.balance}), 201

@account_blueprint.route('/accounts/<int:account_id>', methods=['PUT'])
def update_account(account_id):
    data = request.get_json()
    account = BankAccountService.update_account(account_id, data['account_number'], data['balance'])
    if account:
        return jsonify({"id": account.id, "account_number": account.account_number, "balance": account.balance}), 200
    return jsonify({"message": "Account not found"}), 404

@account_blueprint.route('/accounts/<int:account_id>', methods=['DELETE'])
def delete_account(account_id):
    account = BankAccountService.delete_account(account_id)
    if account:
        return jsonify({"message": "Account deleted"}), 200
    return jsonify({"message": "Account not found"}), 404