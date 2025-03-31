from dataclasses import dataclass




@dataclass
class Corso:
    codins:int
    crediti:int
    nome:str
    pd:int
    #studenti: list[Student]=None #lazy initialization
    #matricole:list[str] =None

    def __eq__(self, other):
        return self.codins == other.codins #due elementi si distinguono per la loro chiave primaria

    def __hash__(self):
        return hash(self.codins) #delega alla funzione di hash della CHIAVE PRIMARIA

    def __str__(self):
        return f"{self.nome} ({self.codins}) - {self.crediti} CFU"
