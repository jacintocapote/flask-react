from app.models import Transaction, BankAccount, db

class TransactionService:

    @staticmethod
    def create_transaction(bank_account_id, transaction_type, currency, amount):
        # Fetch the bank account
        bank_account = BankAccount.query.get(bank_account_id)
        if not bank_account:
            raise ValueError(f"Bank account with ID {bank_account_id} not found.")

        # Check if the transaction currency matches the bank account currency
        if bank_account.currency != currency:
            raise ValueError(f"Transaction currency {currency} does not match bank account currency {bank_account.currency}.")

        # Check if the transaction is a transfer and balance is sufficient
        if transaction_type == 'transfer':
            if bank_account.balance < amount:
                raise ValueError("Insufficient balance for transfer.")

        # Create the transaction if the currency is valid
        new_transaction = Transaction(
            bank_account_id=bank_account_id,
            transaction_type=transaction_type,
            currency=currency,
            amount=amount
        )
        db.session.add(new_transaction)

        # Optionally update the bank account balance for deposits and transfers
        if transaction_type == 'deposit':
            bank_account.balance += amount
        elif transaction_type == 'transfer':
            bank_account.balance -= amount

        db.session.commit()
        return new_transaction

    @staticmethod
    def get_all_transactions():
        """Retrieve all transactions across all accounts."""
        return Transaction.query.all()

    @staticmethod
    def get_transactions_by_account(bank_account_id):
        return Transaction.query.filter_by(bank_account_id=bank_account_id).all()

    @staticmethod
    def delete_transaction(transaction_id):
        transaction = Transaction.query.get(transaction_id)
        if transaction:
            db.session.delete(transaction)
            db.session.commit()
        return transaction