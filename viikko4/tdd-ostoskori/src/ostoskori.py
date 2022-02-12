from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.korissa = []
        self.lkm_korissa = 0
        self.hinta_korissa = 0
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return self.lkm_korissa
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return self.hinta_korissa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        self.lkm_korissa += 1
        self.hinta_korissa += lisattava.hinta()
        for ostos in self.korissa:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return
        self.korissa.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        self.lkm_korissa -= 1
        self.hinta_korissa -= poistettava.hinta()
        for ostos in self.korissa:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.korissa
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
