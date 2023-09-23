from credenciais import secrets

DEBUG = True
SQLALCHEMY_DATABASE_URI = f"mysql://{secrets['mysql-user']}:{secrets['mysql-password']}@{secrets['mysql-host']}:{secrets['mysql-port']}/{secrets['mysql-database']}"
SQLALQUEMY_TRACK_MODIFICATIONS = False