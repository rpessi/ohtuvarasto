import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_saldo_ei_ole_negatiivinen(self):
        self.varasto1 = Varasto(10,-10)
        self.assertGreaterEqual(self.varasto1.saldo, 0)
    
    def test_uudella_varastolla_positiivinen_tilavuus(self):
        self.varasto2 = Varasto(-10)
        self.assertGreaterEqual(self.varasto2.tilavuus, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_negatiivinen_lisays_ei_sallittu(self):
        self.varasto.lisaa_varastoon(-8)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ylisuuri_lisays_ei_sallittu(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_negatiivisen_maaran_ottaminen_ei_sallittu(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_ei_voi_ottaa_enempaa_kuin_varastossa_on(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(8)
        self.assertAlmostEqual(saatu_maara, 5)


    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varastotilanteen_tulostus_toimii(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(3)
        tuloste = self.varasto.__str__()
        self.assertEqual(tuloste, f"saldo = 5, vielä tilaa 5")
