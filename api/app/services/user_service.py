from app.models import User, BankAccount, db

class UserService:

    @staticmethod
    def get_all_users():
        """Retrieve all users."""
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        """Retrieve a specific user by ID."""
        return User.query.get(user_id)

    @staticmethod
    def create_user(name, email):
        """Create a new user."""
        # Check if email already exists
        if User.query.filter_by(email=email).first():
            raise ValueError(f"Email {email} is already in use")
        
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def update_user(user_id, name, email):
        """Update an existing user's information."""
        user = User.query.get(user_id)
        if not user:
            return None

        # Check if the new email already exists for another user
        existing_user = User.query.filter_by(email=email).first()
        if existing_user and existing_user.id != user.id:
            raise ValueError(f"Email {email} is already in use by another user")
        
        user.name = name
        user.email = email
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        """Delete a user if they have no associated bank accounts."""
        user = User.query.get(user_id)
        if user:
            # Check if the user has any associated bank accounts
            if BankAccount.query.filter_by(user_id=user.id).count() > 0:
                raise ValueError(f"Cannot delete user {user.name}. User has associated bank accounts.")
            
            db.session.delete(user)
            db.session.commit()
        return user