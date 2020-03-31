class Player():

    def __init__(self, firstname, lastname, licencenr, elo):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__licencenr = licencenr
        self.__elo = elo

    def get_data(self):

        return self.__firstname + ", " + self.__lastname + ", " + self.__licencenr + ", " + self.__elo