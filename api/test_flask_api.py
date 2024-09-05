import pytest
from api import create_app, db
from app.models import User, BankAccount, Transaction

@pytest.fixture
def app():
    # Set up the Flask app for testing
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"  # Use in-memory database for testing
    })

    with app.app_context():
        db.create_all()  # Create tables before running tests
        yield app
        db.session.remove()
        db.drop_all()  # Drop tables after tests

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def init_database(app):
    # Initialize database with test data if necessary
    user = User(name="Test User", email="test@example.com")
    db.session.add(user)
    db.session.commit()
    return user

### User Tests ###

def test_create_user(client):
    """Test creating a new user"""
    response = client.post('/api/users', json={
        "name": "John Doe",
        "email": "john.doe@example.com"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

    # Verify user was added to the DB
    user = User.query.filter_by(email="john.doe@example.com").first()
    assert user is not None
    assert user.name == "John Doe"

def test_create_user_no_bank_account(client):
    """Test creating a user and confirm no bank accounts are associated"""
    response = client.post('/api/users', json={
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    })
    assert response.status_code == 201

    # Verify user was added to the DB
    user = User.query.filter_by(email="jane.doe@example.com").first()
    assert user is not None

    # Verify no bank accounts associated
    assert len(user.accounts) == 0

def test_get_user(client, init_database):
    """Test getting a user from the system"""
    user_id = init_database.id
    response = client.get(f'/api/users/{user_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Test User"
    assert data["email"] == "test@example.com"

def test_update_user(client, init_database):
    """Test updating a user's email"""
    user_id = init_database.id
    response = client.put(f'/api/users/{user_id}', json={
        "name": "Test User",
        "email": "new.email@example.com"
    })
    assert response.status_code == 200

    # Verify updated email in DB
    user = User.query.get(user_id)
    assert user.email == "new.email@example.com"

def test_delete_user(client, init_database):
    """Test deleting a user"""
    user_id = init_database.id
    response = client.delete(f'/api/users/{user_id}')
    assert response.status_code == 200

    # Verify user was deleted from the DB
    user = User.query.get(user_id)
    assert user is None

def test_get_all_users(client):
    """Test getting all users"""
    # Create multiple users
    client.post('/api/users', json={"name": "User1", "email": "user1@example.com"})
    client.post('/api/users', json={"name": "User2", "email": "user2@example.com"})

    response = client.get('/api/users')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2  # We have two users in the system now

### User Error Tests ###

def test_create_duplicate_user_error(client):
    """Test creating a user with an existing email"""
    # Create initial user
    client.post('/api/users', json={
        "name": "John Doe",
        "email": "john.doe@example.com"
    })

    # Attempt to create a user with the same email
    response = client.post('/api/users', json={
        "name": "John Duplicate",
        "email": "john.doe@example.com"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "Email john.doe@example.com is already in use" in data["message"]

def test_delete_non_existent_user_error(client):
    """Test deleting a non-existent user"""
    response = client.delete('/api/users/9999')  # Non-existent user ID
    assert response.status_code == 404
    data = response.get_json()
    assert "User not found" in data["message"]

def test_update_user_duplicate_email_error(client, init_database):
    """Test updating a user's email to an email that already exists"""
    # Create another user
    client.post('/api/users', json={
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    })

    # Attempt to update the first user's email to the existing email
    user_id = init_database.id
    response = client.put(f'/api/users/{user_id}', json={
        "name": "Test User",
        "email": "jane.doe@example.com"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "Email jane.doe@example.com is already in use" in data["message"]

### Bank Account and Transaction Tests ###

def test_create_bank_account(client, init_database):
    """Test creating a bank account and verify it's associated with the user"""
    response = client.post('/api/accounts', json={
        "account_number": "123456",
        "balance": 1000.00,
        "currency": "USD",
        "user_id": init_database.id
    })
    assert response.status_code == 201

    # Verify account was added to the DB
    account = BankAccount.query.filter_by(account_number="123456").first()
    assert account is not None
    assert account.balance == 1000.00
    assert account.currency == "USD"
    assert account.user_id == init_database.id

def test_deposit_to_account(client, init_database):
    """Test depositing money to a bank account"""
    # Create a bank account
    client.post('/api/accounts', json={
        "account_number": "654321",
        "balance": 500.00,
        "currency": "USD",
        "user_id": init_database.id
    })

    # Deposit transaction
    response = client.post('/api/transactions', json={
        "bank_account_id": 1,
        "transaction_type": "deposit",
        "currency": "USD",
        "amount": 200
    })
    assert response.status_code == 201

    # Verify updated balance in DB
    account = BankAccount.query.filter_by(account_number="654321").first()
    assert account.balance == 700.00  # Balance should be updated to 700

def test_transfer_between_accounts(client, init_database):
    """Test transferring money between two accounts"""
    # Create two accounts
    client.post('/api/accounts', json={
        "account_number": "100001",
        "balance": 1000.00,
        "currency": "USD",
        "user_id": init_database.id
    })
    client.post('/api/accounts', json={
        "account_number": "100002",
        "balance": 500.00,
        "currency": "USD",
        "user_id": init_database.id
    })

    # Transfer transaction
    response = client.post('/api/transactions', json={
        "bank_account_id": 1,  # Account 1
        "transaction_type": "transfer",
        "currency": "USD",
        "amount": 300
    })
    assert response.status_code == 201
    
    response = client.post('/api/transactions', json={
        "bank_account_id": 2,  # Account 2
        "transaction_type": "deposit",
        "currency": "USD",
        "amount": 300
    })
    assert response.status_code == 201

    # Verify updated balances in DB
    account1 = BankAccount.query.filter_by(account_number="100001").first()
    account2 = BankAccount.query.filter_by(account_number="100002").first()

    assert account1.balance == 700.00  # 1000 - 300
    assert account2.balance == 800.00  # 500 + 300

### Bank Account Error Tests ###

def test_create_bank_account_invalid_user_error(client):
    """Test creating a bank account with a non-existent user ID"""
    
    response = client.post('/api/accounts', json={
        "account_number": "123456",
        "balance": 1000.00,
        "currency": "USD",
        "user_id": 9999  # Non-existent user ID
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "User with ID 9999 not found" in data["message"]

### Transaction Error Tests ###

def test_transaction_currency_mismatch_error(client, init_database):
    """Test creating a transaction with mismatched currency"""
    # Create a bank account
    client.post('/api/accounts', json={
        "account_number": "987654",
        "balance": 1000.00,
        "currency": "USD",
        "user_id": init_database.id
    })

    # Attempt to create a transaction with a different currency
    response = client.post('/api/transactions', json={
        "bank_account_id": 1,
        "transaction_type": "deposit",
        "currency": "EUR",  # Mismatched currency
        "amount": 200
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "Transaction currency EUR does not match bank account currency USD" in data["message"]

def test_delete_non_existent_transaction_error(client):
    """Test deleting a non-existent transaction"""
    response = client.delete('/api/transactions/9999')  # Non-existent transaction ID
    assert response.status_code == 404
    data = response.get_json()
    assert "Transaction not found" in data["message"]

def test_transfer_insufficient_balance_error(client, init_database):
    """Test transferring money from an account with insufficient balance"""
    # Create two accounts
    client.post('/api/accounts', json={
        "account_number": "100001",
        "balance": 100.00,  # Low balance
        "currency": "USD",
        "user_id": init_database.id
    })
    client.post('/api/accounts', json={
        "account_number": "100002",
        "balance": 500.00,
        "currency": "USD",
        "user_id": init_database.id
    })

    # Attempt to transfer more than the available balance
    response = client.post('/api/transactions', json={
        "bank_account_id": 1,  # Account 1 with low balance
        "transaction_type": "transfer",
        "currency": "USD",
        "amount": 200  # Exceeds available balance
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "Insufficient balance" in data["message"]