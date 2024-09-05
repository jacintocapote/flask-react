from app.models import BankAccount, db

class BankAccountService:

    @staticmethod
    def get_all_accounts():
        return BankAccount.query.all()

    @staticmethod
    def get_account_by_id(account_id):
        return BankAccount.query.get(account_id)

    @staticmethod
    def create_account(account_number, balance, user_id):
        new_account = BankAccount(account_number=account_number, balance=balance, user_id=user_id)
        db.session.add(new_account)
        db.session.commit()
        return new_account

    @staticmethod
    def update_account(account_id, account_number, balance):
        account = BankAccount.query.get(account_id)
        if account:
            account.account_number = account_number
            account.balance = balance
            db.session.commit()
        return account

    @staticmethod
    def delete_account(account_id):
        account = BankAccount.query.get(account_id)
        if account:
            db.session.delete(account)
            db.session.commit()
        return account