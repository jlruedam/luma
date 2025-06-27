import os
# DB_FILE_PATH = os.path.join(os.path.dirname(__file__), "luma.sqlite")

# from dotenv import dotenv_values

# config = dotenv_values(".env")

USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT', '5432')
DATABASE = os.getenv('DATABASE')

# print(config)
# HOST =config['HOST']
# DATABASE = config['DATABASE']
# USER = config['USER']
# PASSWORD = config['PASSWORD']
# PORT = config.get('PORT', '5432')

class Config:
    # SQLALCHEMY_DATABASE_URI = (
    #     f'mssql+pyodbc://{USER}:{PASSWORD}@{SERVER}/{DATABASE}'
    #     '?driver=ODBC+Driver+17+for+SQL+Server'
    # )
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    SECRET_KEY = "this-is-not-secret" 
