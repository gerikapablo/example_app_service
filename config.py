import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'helloworld1234g.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'prueba'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'giuliana'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Jueves459.'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'giulianasa'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'Wx27Lq+mqdRKg1emIoSHBJ5wJTjXkem9wRbvSPhKoPKdwZ0sKa2gAGxHxuRErY3FyNKflGE9fsFZWmtsgIgS3g=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
