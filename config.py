from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

db_user = os.getenv('DB_USER')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_password = os.getenv('DB_PASSWORD')
db_port = os.getenv('DB_PORT')

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

app.app_context().push()