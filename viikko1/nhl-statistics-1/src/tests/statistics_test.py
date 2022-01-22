import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_valitse_tiimi(self):
        team = self.statistics.team("PIT")
        player = team[0]
        self.assertEqual(len(team), 1)
        self.assertEqual(player.name, "Lemieux")

    def test_etsi_oikea_pelaaja(self):
        player = self.statistics.search("Semenko")
        self.assertEqual(player.name, "Semenko")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 4)
        self.assertEqual(player.assists, 12)
    
    def test_etsi_vaara_pelaaja(self):
        self.assertEqual(self.statistics.search("Laine"), None)

    def test_parhaimmat_maalintekijat(self):
        self.assertEqual(self.statistics.top_scorers(1)[0].name, "Gretzky")