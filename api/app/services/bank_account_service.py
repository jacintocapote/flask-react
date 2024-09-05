from app.models import BankAccount, User, db

class BankAccountService:

    @staticmethod
    def create_account(account_number, balance, user_id, currency):
        """Create a new bank account and associate it with a user."""
        # Check if the user exists
        user = User.query.get(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found.")

        # Create the bank account if the user is valid
        new_account = BankAccount(
            account_number=account_number,
            balance=balance,
            currency=currency,
            user_id=user_id
        )
        db.session.add(new_account)
        db.session.commit()
        return new_account

    @staticmethod
    def get_account_by_id(account_id):
        """Retrieve a specific bank account by ID."""
        return BankAccount.query.get(account_id)

    @staticmethod
    def get_all_accounts():
        """Retrieve all bank accounts."""
        return BankAccount.query.all()

    @staticmethod
    def update_account(account_id, account_number, balance, currency):
        """Update an existing bank account."""
        account = BankAccount.query.get(account_id)
        if account:
            account.account_number = account_number
            account.balance = balance
            account.currency = currency
            db.session.commit()
        return account

    @staticmethod
    def delete_account(account_id):
        """Delete a bank account."""
        account = BankAccount.query.get(account_id)
        if account:
            db.session.delete(account)
            db.session.commit()
        return account