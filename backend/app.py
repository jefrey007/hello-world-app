from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    connection = psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        database=os.getenv('DB_NAME', 'mydatabase'),
        user=os.getenv('DB_USER', 'user'),
        password=os.getenv('DB_PASSWORD', 'password')
    )
    return connection

@app.route('/')
def hello():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT message FROM greetings LIMIT 1;')
    greeting = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return greeting

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
