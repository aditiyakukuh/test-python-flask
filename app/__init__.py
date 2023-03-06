from flask import Flask #Memanggil library Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

app = Flask(__name__) #Untuk menjelaskan nama modul yang digunakan, sehingga ketika folder lain memanggil folder app akan otomatis teridentifikasi.

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
db = SQLAlchemy(app)

from app import routes #Memanggil file routes (akan segera dibuat)