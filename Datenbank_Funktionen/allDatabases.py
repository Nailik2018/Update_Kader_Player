import mysql.connector
import configparser
import ast

# https://stackoverflow.com/questions/28757902/how-to-install-mysqldb-in-pycharm-windows?rq=1

def print_all_databases():

    db_config = configparser.ConfigParser()
    db_config.read("../configurations/database.ini")

    user = ast.literal_eval(db_config.get("DATABASE", "dbuser"))
    db = ast.literal_eval(db_config.get("DATABASE", "db"))
    password = ast.literal_eval(db_config.get("DATABASE", "password"))

    db = db.split("=")

    localhost = db[1].split(";")
    db = db[2]
    localhost = localhost[0]

    db = mysql.connector.connect(
        host=localhost,
        user=user,
        passwd=password,
        database=db
    )

    mycursor = db.cursor()

    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
        print(x)

print_all_databases()