
"""
Database a place where we store, retrieve and manage data.
Database management system (DBMS) is a digital system that manages database. 
Types of DBMS
1. Relational DBMS (SQL -> Structured Query Language) e.g mySQL, PostgreSQL, MSSQL, ORACLE, MariaDB, e.t.c
2. Non Relational DBMS (NoSQL) e.g MongoDB, fireStore

Types of table Relationships
1. one to one -> user table(id, fullname, email, password) and  profile table(id, picture_url, bio, user_id)
2. one to many -> user table(id, fullname, email, password) and  post table(id, title, content, user_id)
3. many to many -> user table, product_table(id, name, price, user_id) and order_table(id, product_id, user_id)

catagories of queries
1. DDL (Data Definition Language) -> CREATE, ALTER, DROP, TRUNCATE
2. DML (Data Manipulation Language) -> INSERT, UPDATE, DELETE 
3. DQL (Data Query Language) -> SELECT
"""
import mysql.connector as sql 

mycon = sql.connect(
    host = "127.0.0.1",
    port = "3306",
    user = "root",
    password = "password",
    database = "junebank_db"
)
mycon.autocommit = True
mycursor = mycon.cursor()

# bank app
# -> functionalities; create account, transfer, deposit, withdraw, check balance, login e.t.c
# -> database tables; user table(id, fullname, email, password, address, account_number, account balance), transaction table(id, sender_id, receiver_id, amount, type, transaction_date)

# query = "CREATE DATABASE junebank_db"
# query = "SHOW DATABASES"
# mycursor.execute(query)
# for db in mycursor:
#     print(db)

# result = mycursor.fetchall()
# print(result)


query = """CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(50),
    email VARCHAR(50) UNIQUE,
    password VARCHAR(50),
    address VARCHAR(100),
    account_no VARCHAR(10),
    account_balance FLOAT DEFAULT 0.0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
"""

# query = "ALTER TABLE users CHANGE fullname name VARCHAR(50)"
query = "ALTER TABLE users CHANGE account_balance account_balance FLOAT(10, 2) DEFAULT 0.0"
# query = "ALTER TABLE users DROP COLUMN fullname"
# query = "ALTER TABLE users ADD COLUMN fullname VARCHAR(50) AFTER id"

# query = "TRUNCATE TABLE users"
# query = "DROP TABLE users"

# mycursor.execute(query)

import random

# random.seed(100)
# num = random.randint(1000000000, 1099999999)
# print(num)

def register():
    fullname = input("Enter your fullname: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    address = input("Enter your address: ")
    account_no = random.randint(1000000000, 1099999999)
    
    query = "INSERT INTO users(fullname, email, password, address, account_no) VALUES(%s, %s, %s, %s, %s)"
    values = (fullname, email, password, address, account_no)
    mycursor.execute(query, values)
    
    print('Registration successfull')

register()