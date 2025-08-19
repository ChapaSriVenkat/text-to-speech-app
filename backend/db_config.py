import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="Your_password",
        database="Your_database"
    )

def create_user_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
