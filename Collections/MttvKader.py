# -*- coding: utf-8 -*-
from Collections.CSVDownloadOfWebsite import CSVDownloadOFWebsite
from Datenbank_Funktionen.select_all_players import select_all_players
from helpfunctions.tuple_to_list import tuple_to_list
from Collections.Database import DB

class MttvKader():

    def __init__(self, male_url, female_url):
        self.male_url = male_url
        self.female_url = female_url

    @staticmethod
    def get_row_data(url):
        print("Die URL " + str(url) + " wird aufgerufen.")
        csv_download = CSVDownloadOFWebsite(url)
        raw_data = str(csv_download.download())
        all_data = raw_data.split("\\r\\")

        player = []

        for line in all_data:
            data_set = line.split(";")

            current_player = {}

            if line == "n\'" or data_set[1] == "VORNAME":
                #print(line)
                continue
            else:
                firstname = ''
                for i in range(0, len(data_set[0])):
                    if i != 0:
                        firstname += data_set[0][i]
                        i += 1
                current_player['firstname'] = firstname
                current_player['lastname'] = data_set[1]
                current_player['licence_number'] = data_set[2]
                current_player['club'] = data_set[3]
                current_player['new_elo_wert'] = data_set[4]
                current_player['elo_wert_delta'] = data_set[5]
                current_player['placement'] = data_set[6]
                current_player['classment'] = data_set[7]
                current_player['classment_men'] = data_set[8]

                player.append(current_player)

        return player

    def update_execute(self):

        kader_player_tuple = select_all_players()
        kader_player_list = tuple_to_list(kader_player_tuple)

        male = MttvKader.get_row_data(self.male_url)
        female = MttvKader.get_row_data(self.female_url)

        print("Update der Männer wird gestartet!")
        print("Es hat total " + str(len(male)) + " männliche Spieler.")
        print("-" * 100)
        print("Update der Frauen wird gestartet!")
        print("Es hat total " + str(len(female)) + " weibliche Spieler.")

        i = 0

        filtered_male = []
        filtered_female = []

        # loop license nr of male player from csv list and compare with male player license nr in db
        # if license nr from csv list matches license nr from db
        # = kader player
        for single_player in male:
            for license in kader_player_list:
                if int(license) == int(single_player['licence_number']):
                    filtered_male.append(single_player)
                i += 1

        i = 0

        # loop license nr of male player from csv list and compare with female player license nr in db
        # if license nr from csv list matches license nr from db
        # = kader player
        for single_player in female:
            for license in kader_player_list:
                if int(license) == int(single_player['licence_number']):
                    filtered_female.append(single_player)
                i += 1

        # Update DB
        db = DB()
        db.update(filtered_male)
        db.update(filtered_female)
