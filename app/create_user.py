import sys
import os
import random
from werkzeug.security import generate_password_hash


# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from app.models import User
from app import db, server
from faker import Faker


faker = Faker()
USER_ROLES = ['admin', 'lawyer', 'judge', 'defendant', 'plaintiff']


def create_user(*args, **kwargs):
    with server.app_context():
        # Create a new user
        email = kwargs.get("email", faker.email())
        first_name = kwargs.get("first_name", faker.first_name())
        last_name = kwargs.get("last_name", faker.last_name())
        username = kwargs.get("username", None)
        password = kwargs.get("password", None)
        is_superuser = kwargs.get("is_superuser", False)
        role_count = len(USER_ROLES)
        user_role = kwargs.get("user_role", None)
        if not user_role:
            if is_superuser:
                user_role = "admin" # roles[1]
            else:
                user_role = USER_ROLES[random.randint(1, role_count - 1)]

        if not (username and password and user_role):
            print("Username, password or role was not provided")
            return

        # Check if the username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            print("User with this username already exists.")
            return

        new_user = User(username=username,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        other_name=None, #[faker.first_name(), None][random.randint(0, 1)],
                        role=user_role,
                        is_superuser=is_superuser,
                        )
        new_user.set_password(password)
        # persist to the db
        db.session.add(new_user)
        db.session.commit()
        print(f"User '{username}' created successfully{' as superuser' if is_superuser else ''}.")


if __name__ == "__main__":
    # Check if enough arguments were provided
    if len(sys.argv) < 1:
        print("Usage: python create_user.py <username> <password> [--superuser]")
        sys.exit(1)

    # Get username and password from command-line arguments
    username = None
    password = None
    is_superuser = '--superuser' in sys.argv
    email = None
    first_name = None
    last_name = None
    user_role = None
    if len(sys.argv) > 1:
        username = sys.argv[1] or None
        if username == "--superuser":
            username = None
    if len(sys.argv) > 2:
        password = sys.argv[2] or None
        if password == "--superuser":
            password = None
    if not username:
        username = input("Username: ")
    if not password:
        password = input("Password: ")
    if not email:
        email = input("Email Address: ")
    if not first_name:
        first_name = input("First Name: ")
    if not last_name:
        last_name = input("Last Name: ")
    if is_superuser:
        user_role = "admin" # or roles[1]
    else:
        roles_joined = ", ".join(USER_ROLES[1:])
        user_role = input(f"Select User Role ({roles_joined}): ")

    create_users_kwargs = dict(username=username,
                               email=email,
                               password=password,
                               first_name=first_name,
                               last_name=last_name,
                               is_superuser=is_superuser,
                               user_role=user_role,
                               )
    from pprint import pprint
    pprint(create_users_kwargs)
    if not (username and password and user_role):
        print("Username, password or role was not provided")
        sys.exit(1)

    create_user(**create_users_kwargs)
