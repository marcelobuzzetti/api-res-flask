from credenciais import secrets
import string
import random

random_str = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(random_str) for i in range(12))
DEBUG = True
SQLALCHEMY_DATABASE_URI = f"mysql://{secrets['mysql-user']}:{secrets['mysql-password']}@{secrets['mysql-host']}:{secrets['mysql-port']}/{secrets['mysql-database']}"
SQLALQUEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = key