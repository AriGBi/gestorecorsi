from database.DB_connect import DBConnect
from model.corso import Corso


class DAO():


    @staticmethod
    def getCodins():
        """ Chiama DBconnect, si fa imprestare la connessione e esegue la query"""
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)
        query="""SELECT c.codins FROM corso c """
        cursor.execute(query)
        res=[]
        for row in cursor:
            res.append(row["codins"])


        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllCorsi():
        """ Chiama DBconnect, si fa imprestare la connessione e esegue la query"""
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)
        query="""SELECT * FROM corso c """
        cursor.execute(query)
        res=[]
        for row in cursor:
            #res.append(Corso(codins=row["codins"],crediti=row["crediti"],nome=row["nome"],pd=row["pd"])) #creo degli oggetti Corso a partire dai dati del database
            res.append(Corso(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorsiPD(pd):
        """ Chiama DBconnect, si fa imprestare la connessione e esegue la query"""
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM corso c where c.pd=%s"""
        cursor.execute(query,(pd,))
        res = []
        for row in cursor:
            # res.append(Corso(codins=row["codins"],crediti=row["crediti"],nome=row["nome"],pd=row["pd"])) #creo degli oggetti Corso a partire dai dati del database
            res.append(Corso(**row))

        cursor.close()
        cnx.close()
        return res

if __name__=="__main__":
    print(DAO.getCodins())

    for c in (DAO.getAllCorsi()):
        print(c)
