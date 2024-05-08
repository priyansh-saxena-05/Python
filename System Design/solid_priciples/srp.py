"""
Single Responsibility Principle (SRP):
The Single Responsibility Principle states that a class should have only one reason to change, meaning it should have only one responsibility. This principle helps to keep classes focused, maintainable, and easier to understand.Example: Consider a class that handles both user authentication and user data persistence.
This violates SRP because it has two responsibilities:
authentication and data persistence.
"""

class UserManager:
    def authenticate_user(self, username, password):
        # Authenticate user
        pass
    
    def save_user(self, user):
        # Save user to database
        pass
"""    
To adhere to SRP, we can split this class into two separate classes: one for user authentication and another for user data persistence.
"""

class Authenticator:
    def authenticate_user(self, username, password):
        # Authenticate user
        pass

class UserRepository:
    def save_user(self, user):
        # Save user to database
        pass