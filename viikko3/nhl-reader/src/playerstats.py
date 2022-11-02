from playerreader import PlayerReader

class PlayerStats:
    def __init__(self, reader: PlayerReader) -> None:
        self.reader = reader
    
    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_player_info()

        return sorted(filter(lambda player: player.nationality == nationality, players), key=lambda player: player.assists + player.goals, reverse=True)
