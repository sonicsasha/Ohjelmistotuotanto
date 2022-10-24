import unittest
from statistics import Statistics, SortBy
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
    def setUp(self) -> None:
        self.stats = Statistics(PlayerReaderStub())
    
    def test_search_player(self):
        self.assertEqual(str(self.stats.search("Semenko")), str(PlayerReaderStub().get_players()[0]))
        self.assertEqual(self.stats.search("Shrek"), None)
    
    def test_search_team(self):
        players = PlayerReaderStub().get_players()
        self.assertEqual(str(self.stats.team("EDM")[0]), str(players[0]))
        self.assertEqual(str(self.stats.team("EDM")[1]), str(players[2]))
        self.assertEqual(str(self.stats.team("EDM")[2]), str(players[4]))
    
    def test_top_player_points(self):
        players = PlayerReaderStub().get_players()
        self.assertEqual(str(self.stats.top(2, SortBy.POINTS)[0]), str(players[4]))
        self.assertEqual(str(self.stats.top(2, SortBy.POINTS)[1]), str(players[1]))
    
    def test_top_player_goals(self):
        players = PlayerReaderStub().get_players()
        self.assertEqual(str(self.stats.top(2, SortBy.GOALS)[0]), str(players[1]))
        self.assertEqual(str(self.stats.top(2, SortBy.GOALS)[1]), str(players[3]))
    
    def test_top_player_assists(self):
        players = PlayerReaderStub().get_players()
        self.assertEqual(str(self.stats.top(2, SortBy.ASSISTS)[0]), str(players[4]))
        self.assertEqual(str(self.stats.top(2, SortBy.ASSISTS)[1]), str(players[3]))
