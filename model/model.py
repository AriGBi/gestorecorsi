from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getCodins(self):
        return DAO.getCodins() #questo metodo del modello prende l'elenco dei corsi dal DAO

    def getAllCorsi(self):
        return DAO.getAllCorsi()

    def getCorisPD(self, pd):
        return DAO.getCorsiPD(pd)
