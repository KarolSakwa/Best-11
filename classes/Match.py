from events.match_events import get_goals_scored, give_match_stats

class Match:
    instances = []
    def __init__(self, home, away, league):
        Match.instances.append(self)
        self.id = 0
        self.score = []
        self.home = home
        self.away = away
        self.league = league
        self.winner = None
        self.loser = None
        # match events
        self.goal_scorers = []

    def __repr__(self):
        return f'{self.home} vs. {self.away}'

    def play_match(self):
        goals = get_goals_scored(self)
        self.score = [goals[0], goals[1]]
        self.goal_scorers = [goals[2], goals[3]]
        give_match_stats(self)
