import os
from dotenv import dotenv_values

# config = dotenv_values(".env")

USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
DATABASE = os.getenv('DATABASE')

# print(config)
# HOST =config['HOST']
# DATABASE = config['DATABASE']
# USER = config['USER']
# PASSWORD = config['PASSWORD']


class Config:
    # SQLALCHEMY_DATABASE_URI = (
    #     f'mssql+pyodbc://{USER}:{PASSWORD}@{HOST}/{DATABASE}'
    #     '?driver=ODBC+Driver+17+for+SQL+Server'
    # )
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{USER}:{PASSWORD}@{HOST}/{DATABASE}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    SECRET_KEY = "this-is-not-secret" 
