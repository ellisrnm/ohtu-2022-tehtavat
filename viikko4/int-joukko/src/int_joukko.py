KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Syötetyn kapasiteetin arvo ei ole kelvollinen")
        self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Syötetyn kasvatuskoon arvo ei ole kelvollinen")
        self.kasvatuskoko = kasvatuskoko

        self.joukko = []
        self.alkioiden_lkm = 0

    def kuuluu(self, alkio):
        if alkio in self.joukko:
            return True
        return False

    def lisaa(self, alkio):
        if self.kuuluu(alkio):
            return False

        if self.alkioiden_lkm == self.kapasiteetti:
            self.kapasiteetti += self.kasvatuskoko

        self.joukko.append(alkio)
        self.alkioiden_lkm = self.alkioiden_lkm + 1
        return True

    def poista(self, alkio):
        try:
            self.joukko.remove(alkio)
            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True
        except:
            return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = []
        for alkio in self.joukko:
            taulu.append(alkio)

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()

        for a_alkio in a.joukko:
            x.lisaa(a_alkio)

        for b_alkio in b.joukko:
            x.lisaa(b_alkio)

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()

        for a_alkio in a.joukko:
            for b_alkio in b.joukko:
                if a_alkio == b_alkio:
                    y.lisaa(b_alkio)

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()

        for a_alkio in a.joukko:
            z.lisaa(a_alkio)

        for b_alkio in b.joukko:
            z.poista(b_alkio)

        return z

    def __str__(self):
        arvot = [str(arvo) for arvo in self.joukko[:self.alkioiden_lkm]]
        return "{" + ", ".join(arvot) + "}"
