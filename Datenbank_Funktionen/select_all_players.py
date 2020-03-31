import mysql.connector
import configparser
import ast

def select_all_players():

    db_config = configparser.ConfigParser()
    db_config.read("configurations/database.ini")

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
    mycursor.execute("SELECT licenceNr FROM players")
    list_of_players = mycursor.fetchall()

    return list_of_players

