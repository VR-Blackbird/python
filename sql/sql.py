import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Helloworld@123",
    database="bab"
)

cursor = db.cursor()

# cursor.execute("CREATE DATABASE Stupid")

# cursor.execute("SHOW DATABASES;")
#
# for d in cursor:
#     print(d)

# cursor.execute("CREATE TABLE BURGER (burger_id INT PRIMARY KEY AUTO INCREMENT, name VARCHAR(255), size VARCHAR(255));")


cursor.execute("ALTER TABLE BURGER MODIFY burger_id INT AUTO_INCREMENT;")
db.commit()