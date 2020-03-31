# -*- coding: utf-8 -*-
from Collections.CSVDownloadOfWebsite import CSVDownloadOFWebsite
from Datenbank_Funktionen.select_all_players import select_all_players
from helpfunctions.tuple_to_list import tuple_to_list

class MttvKaderData():

    def __init__(self, url):
        self.url = url

    def get_row_data(self):
        print("Die URL " + str(self.url) + " wird aufgerufen.")
        csv_download = CSVDownloadOFWebsite(self.url)
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

    def select_players(self):
        kader_player_tuple = select_all_players.select_all_players()
        kader_player_list = tuple_to_list(kader_player_tuple)
        return kader_player_list
