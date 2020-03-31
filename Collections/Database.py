import mysql.connector
import datetime
import configparser
import ast

class DB():

    def __init__(self):
        pass

    def update(self, list):

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
        today = datetime.datetime.now()
        month = today.month
        year = today.year

        all_players = []

        for i in list:
            licenceNr = int(i['licence_number'])
            elo = int(i['new_elo_wert'])
            this_player = (licenceNr, month, year, elo)
            all_players.append(this_player)

        statement = "INSERT INTO elos (licenceNr, monthID, year, elo) VALUES (%s, %s, %s, %s)"
        mycursor.executemany(statement, all_players)
        db.commit()
