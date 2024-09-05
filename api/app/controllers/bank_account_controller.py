from flask import Blueprint, jsonify, request
from app.services.bank_account_service import BankAccountService

account_blueprint = Blueprint('account_blueprint', __name__)

# Create a new bank account
@account_blueprint.route('/accounts', methods=['POST'])
def create_account():
    data = request.get_json()
    try:
        account = BankAccountService.create_account(
            account_number=data['account_number'],
            balance=data['balance'],
            user_id=data['user_id'],
            currency=data['currency']
        )
        return jsonify({
            'id': account.id,
            'account_number': account.account_number,
            'balance': account.balance,
            'currency': account.currency,
            'user_id': account.user_id
        }), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

# Get a specific bank account by ID
@account_blueprint.route('/accounts/<int:account_id>', methods=['GET'])
def get_account(account_id):
    account = BankAccountService.get_account_by_id(account_id)
    if account:
        return jsonify({
            'id': account.id,
            'account_number': account.account_number,
            'balance': account.balance,
            'currency': account.currency,
            'user_id': account.user_id
        }), 200
    return jsonify({"message": "Account not found"}), 404

# Get all bank accounts
@account_blueprint.route('/accounts', methods=['GET'])
def get_accounts():
    accounts = BankAccountService.get_all_accounts()
    return jsonify([{
        'id': acc.id,
        'account_number': acc.account_number,
        'balance': acc.balance,
        'currency': acc.currency,
        'user_id': acc.user_id
    } for acc in accounts]), 200

# Update an existing bank account
@account_blueprint.route('/accounts/<int:account_id>', methods=['PUT'])
def update_account(account_id):
    data = request.get_json()
    account = BankAccountService.update_account(
        account_id=account_id,
        account_number=data['account_number'],
        balance=data['balance'],
        currency=data['currency']
    )
    if account:
        return jsonify({
            'id': account.id,
            'account_number': account.account_number,
            'balance': account.balance,
            'currency': account.currency,
            'user_id': account.user_id
        }), 200
    return jsonify({"message": "Account not found"}), 404

# Delete a bank account
@account_blueprint.route('/accounts/<int:account_id>', methods=['DELETE'])
def delete_account(account_id):
    account = BankAccountService.delete_account(account_id)
    if account:
        return jsonify({"message": "Account deleted"}), 200
    return jsonify({"message": "Account not found"}), 404