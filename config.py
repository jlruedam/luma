# import os
# DB_FILE_PATH = os.path.join(os.path.dirname(__file__), "luma.sqlite")

from dotenv import dotenv_values

config = dotenv_values(".env")

print(config)

SERVER =str(config['SERVER'])
DATABASE = str(config['DATABASE'])
USER = str(config['USER'])
PASSWORD = str(config['PASSWORD'])

class Config:
    SQLALCHEMY_DATABASE_URI = (
        f'mssql+pyodbc://{USER}:{PASSWORD}@{SERVER}/{DATABASE}'
        '?driver=ODBC+Driver+17+for+SQL+Server'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    SECRET_KEY = "this-is-not-secret" 
