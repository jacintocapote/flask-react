from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    accounts = db.relationship('BankAccount', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.name}>"


class BankAccount(db.Model):
    __tablename__ = 'bank_accounts'

    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(20), unique=True, nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)
    currency = db.Column(db.String(3), nullable=False)  # Add currency field
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    transactions = db.relationship('Transaction', backref='bank_account', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<BankAccount {self.account_number} ({self.currency})>"
 
class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    transaction_type = db.Column(db.String(50), nullable=False)  # Can be 'transfer' or 'deposit'
    currency = db.Column(db.String(3), nullable=False)           # Currency code, e.g., 'USD'
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    bank_account_id = db.Column(db.Integer, db.ForeignKey('bank_accounts.id'), nullable=False)

    def __repr__(self):
        return f"<Transaction {self.transaction_type} {self.amount} {self.currency}>"       