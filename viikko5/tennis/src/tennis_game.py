class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0
    def won_point(self):
        self.score+=1
        

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if self.player1.name == player_name:
            self.player1.won_point()
        else:
            self.player2.won_point()
    
    def _get_tied_score_text(self):
        score_texts = ["Love-All", "Fifteen-All", "Thirty-All", "Forty-All", "Deuce"]

        index = min(self.player1.score, len(score_texts)-1)
        return score_texts[index]
    
    def _get_endgame_score_text(self):
        score_difference = self.player2.score - self.player1.score

        if score_difference <= -2:
            return "Win for player1"
        elif score_difference >= 2:
            return "Win for player2"

        difference_texts = {-1: "Advantage player1", 1: "Advantage player2"}

        return difference_texts[score_difference]
    
    def _get_score_text(self):
        score_texts = ["Love", "Fifteen", "Thirty", "Forty"]

        return f"{score_texts[self.player1.score]}-{score_texts[self.player2.score]}"

    def get_score(self):
        if self.player1.score == self.player2.score:
            return self._get_tied_score_text()
        elif self.player1.score >= 4 or self.player2.score >= 4:
            return self._get_endgame_score_text()
        else:
            return self._get_score_text()
