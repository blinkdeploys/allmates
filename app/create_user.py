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



def create_user(username, password, is_superuser=False):
    with server.app_context():
        # Check if the username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            print("User with this username already exists.")
            return

        # Create a new user
        roles = ['admin', 'lawyer', 'judge', 'defendant', 'plaintiff']
        role_count = len(roles)
        user_role = roles[random.randint(1, role_count - 1)]
        if is_superuser:
            user_role = "admin" # roles[1]
        new_user = User(username=username,
                        email=faker.email(),
                        first_name=faker.first_name(),
                        last_name=faker.last_name(),
                        other_name=[faker.first_name(), None][random.randint(0, 1)],
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
    if len(sys.argv) < 3:
        print("Usage: python create_user.py <username> <password> [--superuser]")
        sys.exit(1)

    # Get username and password from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    is_superuser = '--superuser' in sys.argv

    create_user(username, password, is_superuser)
