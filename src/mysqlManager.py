from src import config
import mysql.connector 
from mysql.connector import errorcode

"""
.......................................................................................
    initialize a connection to the database
.......................................................................................
"""
try:
    connection = mysql.connector.connect(
            host = config.host,
            user = config.user,
            password = config.passwd,
            database = config.db_name
            )
    cursor = connection.cursor()
except:
    print("connection error")

    
#creates db and tables, only need to run once
"""
try:
    cursor.execute("USE {}".format(config.db_name))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(config.db_name))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor, config.db_name)
        print("Database {} created successfully.".format(config.db_name))
        cnx.database = config.db_name
    else:
        print(err)
        exit(1)
create_tables(cursor)
.......................................................................................
.......................................................................................
"""


def create_database(cursor, database):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def create_tables(cursor):
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
    " customerId int NOT NULL UNIQUE,"
    " name varchar(100) NOT NULL,"
    " address varchar(200),"
    " email varchar(50),"
    " phone varchar(20)"
    ")")

TABLES['masseuses'] = (
    "CREATE TABLE masseuses ("
    " masseuseId int NOT NULL UNIQUE,"
    " name varchar(100) NOT NULL,"
    " address varchar(200),"
    " email varchar(50),"
    " phone varchar(20)"
    ")")

TABLES['appointments'] = (
    "CREATE TABLE appointments ("
    " appointmentId int AUTO_INCREMENT PRIMARY KEY ,"
    " start_time datetime NOT NULL,"
    " room int NOT NULL,"
    " status varchar(20) NOT NULL,"
    " masseuseId int,"
    " customerId int"
    ")")

# Note: 1=Sunday, 2=Monday, 3=Tuesday, 4=Wednesday, 5=Thursday, 6=Friday, 7=Saturday.
TABLES['masseuseavailability'] = (
    "CREATE TABLE masseuseavailability ("
    " id int AUTO_INCREMENT PRIMARY KEY ,"
    " masseuseId int NOT NULL,"
    " dow int NOT NULL,"
    " start int NOT NULL,"
    " end int NOT NULL"
    ")")


