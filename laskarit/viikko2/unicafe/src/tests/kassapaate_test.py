import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateis_oston_testaus_edulliset(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(20), 20)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)


    def test_kateis_oston_testaus_maukkaat(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(20), 20)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kortilla_oston_testaus_edulliset(self):
        kortti = Maksukortti(300)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(kortti))
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(kortti))
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortilla_oston_testaus_maukkaat(self):
        kortti = Maksukortti(500)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(kortti))
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(kortti))
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_lataus(self):
        kortti = Maksukortti(300)
        self.kassapaate.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(kortti.saldo, 400)
        self.assertFalse(self.kassapaate.lataa_rahaa_kortille(kortti, -1000))
