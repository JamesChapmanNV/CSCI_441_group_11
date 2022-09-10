import config
import mysql.connector 
from mysql.connector import errorcode

"""
.......................................................................................
    initialize a connection to the database
.......................................................................................
"""
try:
    cnx = mysql.connector.connect(
            host = config.host,
            user = config.user,
            password = config.passwd)
    print(cnx)
    cursor = cnx.cursor()
except:
    print("connection error")
"""
.......................................................................................
.......................................................................................
"""

#creates db
def create_database(cursor, database):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

""" needed?"""
# try:
#     cursor.execute("USE {}".format(config.db_name))
# except mysql.connector.Error as err:
#     print("Database {} does not exists.".format(config.db_name))
#     if err.errno == errorcode.ER_BAD_DB_ERROR:
#         #create_database(cursor, db_name)
#         print("Database {} created successfully.".format(config.db_name))
#         cnx.database = config.db_name
#     else:
#         print(err)
#         exit(1)

def create_database(cursor, database):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

def create_table(cursor):
    for name, ddl in TABLES.items():
        try:
            cursor.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("TABLE already exists.")
            else:
    	        print(err.msg)

TABLES = {}
TABLES['customers'] = (
    "CREATE TABLE customers ("
    " id int NOT NULL UNIQUE,"
    " name varchar(100) NOT NULL,"
    " address varchar(200),"
    " email varchar(50),"
    " phone varchar(20)"
    ")")

TABLES['masseuses'] = (
    "CREATE TABLE masseuses ("
    " id int NOT NULL UNIQUE,"
    " name varchar(100) NOT NULL,"
    " address varchar(200),"
    " email varchar(50),"
    " phone varchar(20)"
    ")")

TABLES['appointments'] = (
    "CREATE TABLE appointments ("
    " id int NOT NULL UNIQUE,"
    " masseuseId int,"
    " customerId int,"
    " room int NOT NULL,"
    " date date NOT NULL,"
    " time_slot time NOT NULL,"
    " status int,"
    " room int,"
    ")")

TABLES['masseuseavailability'] = (
    "CREATE TABLE masseuseavailability ("
    " id int NOT NULL UNIQUE,"
    " name varchar(200) NOT NULL,"
    ")")

