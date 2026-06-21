import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    # Azure Blob Storage (modern SDK)
    BLOB_CONNECTION_STRING = os.environ.get('BLOB_CONNECTION_STRING') or "DefaultEndpointsProtocol=https;AccountName=ENTER_STORAGE_ACCOUNT_NAME;AccountKey=ENTER_STORAGE_KEY;EndpointSuffix=core.windows.net"
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or "ENTER_IMAGES_CONTAINER_NAME"

    # Azure SQL Database
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'ENTER_SQL_SERVER_NAME.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'ENTER_SQL_DB_NAME'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'ENTER_SQL_SERVER_USERNAME'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'ENTER_SQL_SERVER_PASSWORD'
    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://'
        + SQL_USER_NAME + '@' + SQL_SERVER
        + ':' + SQL_PASSWORD + '@' + SQL_SERVER
        + ':1433/' + SQL_DATABASE
        + '?driver=ODBC+Driver+17+for+SQL+Server'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Microsoft Authentication
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET") or "ENTER_CLIENT_SECRET_HERE"
    AUTHORITY = "https://login.microsoftonline.com/common"
    CLIENT_ID = "ENTER_CLIENT_ID_HERE"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"
