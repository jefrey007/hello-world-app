from flask import Flask
from flask_cors import CORS  # Importing CORS
import psycopg2
import os

# Initialize Flask app and CORS
app = Flask(__name__)
CORS(app)  # Enabling CORS for all routes by default

def get_db_connection():
    connection = psycopg2.connect(
        host=os.getenv('DB_HOST', 'postgres'),  # Update default to 'postgres'
        database=os.getenv('DB_NAME', 'mydatabase'),
        user=os.getenv('DB_USER', 'user'),
        password=os.getenv('DB_PASSWORD', 'password')
