import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'Eeneetaaghaequaengoshai4jahChe4h'
    SQLALCHEMY_DATABASE_URI = os.getenv('POSTGRES_URL') or 'postgresql://postgres:password@localhost:5432/court_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

