import database

class leaderboard:

    def __init__(self, game):
        self.db = database("leaderboard")
        self.game = game
        if self.db.check_table_exists(game):
            self.db.create_table(
                self.game,
                "(username VARCHAR(255), score INT(255), score_date DATETIME DEFAULT NOW())"
                )

    def add_score(score, username):
        self.db.add_row(["username", "score"], self.game)

    def get_scores(username):
        scores = self.db.get_filtered(["score"], "username="+str(username), self.game)
        return(scores)

    def get_top_ten():
        pass
