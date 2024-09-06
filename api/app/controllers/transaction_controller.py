from flask import Blueprint, jsonify, request
from app.services.transaction_service import TransactionService

transaction_blueprint = Blueprint('transaction_blueprint', __name__)

# Create a transaction (deposit or transfer)
@transaction_blueprint.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    try:
        # Validate and create the transaction
        transaction = TransactionService.create_transaction(
            bank_account_id=data['bank_account_id'],
            transaction_type=data['transaction_type'],
            currency=data['currency'],
            amount=data['amount']
        )
        return jsonify({
            'id': transaction.id,
            'transaction_type': transaction.transaction_type,
            'currency': transaction.currency,
            'amount': transaction.amount,
            'timestamp': transaction.timestamp.isoformat()
        }), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400  # Handle validation errors

# Get all transactions for a specific bank account
@transaction_blueprint.route('/transactions/account/<int:bank_account_id>', methods=['GET'])
def get_transactions(bank_account_id):
    transactions = TransactionService.get_transactions_by_account(bank_account_id)
    if transactions:
        return jsonify([{
            'id': t.id,
            'transaction_type': t.transaction_type,
            'currency': t.currency,
            'amount': t.amount,
            'timestamp': t.timestamp.isoformat()
        } for t in transactions]), 200
    return jsonify({"message": "No transactions found for this account."}), 404

# Get all transactions across all accounts
@transaction_blueprint.route('/transactions/all', methods=['GET'])
def get_all_transactions():
    transactions = TransactionService.get_all_transactions()
    return jsonify([{
        'id': t.id,
        'transaction_type': t.transaction_type,
        'amount': t.amount,
        'currency': t.currency,
        'bank_account_id': t.bank_account_id,  # Include bank account ID for clarity
        'timestamp': t.timestamp.isoformat()
    } for t in transactions]), 200

# Get a specific transaction by its ID
@transaction_blueprint.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    transaction = TransactionService.get_transaction_by_id(transaction_id)
    if transaction:
        return jsonify({
            'id': transaction.id,
            'transaction_type': transaction.transaction_type,
            'currency': transaction.currency,
            'amount': transaction.amount,
            'timestamp': transaction.timestamp.isoformat()
        }), 200
    return jsonify({"message": "Transaction not found"}), 404

# Delete a transaction by its ID
@transaction_blueprint.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    try:
        transaction = TransactionService.delete_transaction(transaction_id)
        if transaction:
            return jsonify({"message": "Transaction deleted"}), 200
        return jsonify({"message": "Transaction not found"}), 404
    except ValueError as e:
        return jsonify({"message": str(e)}), 400