import os
# Initiate and setup the env vars
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'  # os.environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')

