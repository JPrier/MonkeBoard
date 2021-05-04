import database

class leaderboard:

    def __init__(self):
        self.db = database("leaderboard")

    def add_score(score, username):
        self.db.add_row([username, score])

    def get_scores(username):
        pass

    def get_top_ten():
        pass
