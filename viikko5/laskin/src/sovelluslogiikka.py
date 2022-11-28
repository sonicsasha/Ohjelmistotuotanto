class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.aikaisemmat_tulokset = []

    def miinus(self, arvo):
        if arvo!=0:
            self.aikaisemmat_tulokset.append(self.tulos)
        self.tulos = self.tulos - arvo


    def plus(self, arvo):
        if arvo!=0:
            self.aikaisemmat_tulokset.append(self.tulos)
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0
        self.aikaisemmat_tulokset.append(self.tulos)

    def kumoa(self):
        self.tulos = self.aikaisemmat_tulokset.pop()

    def aseta_arvo(self, arvo):
        self.tulos = arvo
