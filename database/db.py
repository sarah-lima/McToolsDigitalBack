import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host='us-cdbr-east-06.cleardb.net',
                                    port=3306,
                                    database='heroku_2bd3fab7e61524c',
                                    user='bf8b2400fe11a4',
                                    password='b479a526')

def connection_db():
    try:
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            return cursor
    except Error as e:
        print("Error while connecting to MySQL", e)
    
    
    

def close_connection():
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")