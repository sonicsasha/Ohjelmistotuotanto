import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_tuotteen_hinta(self):
        self.kori.lisaa_tuote(Tuote("testi1", 5))
        self.assertEqual(self.kori.hinta(), 5)
    
    def test_kahden_tuotteen_lisaamisen_jalkeen_ostoskorissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        piima = Tuote("Piimä", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(piima)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_tuotteiden_summa(self):
        maito = Tuote("Maito", 3)
        piima = Tuote("Piimä", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(piima)
        self.assertEqual(self.kori.hinta(), maito.hinta() + piima.hinta())
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_kaksi_kertaa_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 2*maito.hinta())

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        # testaa että metodin palauttaman listan pituus 1
        self.assertEqual(len(ostokset), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        # testaa täällä, että palautetun listan ensimmäinen ostos on halutunkaltainen.
        self.assertEqual(ostos.tuote.nimi(), maito.nimi())
        self.assertEqual(ostos.lukumaara(), 1)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        piima = Tuote("Piimä", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(piima)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_yksi_ostos(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_ostoksen_jolla_sama_nimi_kuin_tuotteella_ja_kaksi_kappaletta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuote.nimi(), maito.nimi())
        self.assertEqual(ostos.lukumaara(), 2)
    
    def test_korissa_kaksi_samaa_tuotetta_yksi_poistetaan_ostoskorissa_yksi_tuote(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    def test_korissa_yksi_tuote_ja_se_poistetaan_niin_kori_tyhja(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)
    
    def test_metodi_tyhjenna_tyhjentaa_korin(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.kori.tyhjenna()

        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)