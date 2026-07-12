import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="db",
        user="root",
        password="root123",
        database="movie_db"
    )
    return connection
