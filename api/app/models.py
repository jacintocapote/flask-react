from flask_sqlalchemy import SQLAlchemy

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
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"<BankAccount {self.account_number}>"
    
class Currency(db.Model):
    __tablename__ = 'currencies'

    id = db.Column(db.String(20), unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    representation = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"<Curreny {self.name}>"    