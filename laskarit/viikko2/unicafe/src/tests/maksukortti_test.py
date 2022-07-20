import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikein_alussa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.10 euroa")

    def test_rahan_lataaminen_kasvattaa_saldo_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.20 euroa")

#    Saldo vähenee oikein, jos rahaa on tarpeeksi
    def test_ota_rahaa_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.05 euroa")

#    Saldo ei muutu, jos rahaa ei ole tarpeeksi
    def test_saldo_ei_muutu(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.10 euroa")

#    Metodi palauttaa True, jos rahat riittivät ja muuten False
    def test_riittaako_raha(self):
        x = self.maksukortti.ota_rahaa(2)
        print(x)
        self.assertTrue(x)
        y = self.maksukortti.ota_rahaa(100)
        print(y)
        self.assertFalse(y)