import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="chintujay",
    database="twofa_app"
)
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    2fa_enabled TINYINT(1) DEFAULT 0,
    2fa_secret VARCHAR(32)
)
""")

db.commit()
cursor.close()
db.close()
print("Database and users table created successfully.")
