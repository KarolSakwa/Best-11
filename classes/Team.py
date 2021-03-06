from helpers.team_helpers import get_all_players_list, set_young_prospect, get_best_players
import classes.Manager as manager
from operator import attrgetter
import random
from classes.Constants import *

class Team:
    instances = []
    def __init__(self, name):
        Team.instances.append(self)
        self.id = 0
        self.name = name
        self.players_by_position = {"GK": [], "DF": [], "MF": [], "CF": []}
        self.manager = None
        self.league = None
        self.nationality = ""
        self.players = []
        self.young_players = []
        self.team_star = None
        self.young_prospect = None
        self.average_age = 0
        self.average_player_skill = 0
        self.budget = 0 
        self.selected_11 = []
        self.first_11 = []
        self.first_11_skills = 0
        # competitions
        self.games_played = 0
        self.points = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_scored = 0
        self.goals_conceded = 0
        self.next_opponent = None
        

    def __repr__(self):
        return f'{self.name}'

    def get_first_11(self):
        best_gk = max([x for x in self.players_by_position["GK"]], key=attrgetter('skills'))
        best_dfs = get_best_players("DF", self)
        best_mfs = get_best_players("MF", self)
        best_cfs = get_best_players("CF", self)
        first_11 = best_dfs + best_mfs + best_cfs
        first_11.insert(0, best_gk)
        return first_11

    def get_defensive_strength(self):
        return sum(x.skills for x in self.first_11 if x.position == "GK" or x.position == "DF")

    def get_offensive_strength(self):
        return sum(x.skills for x in self.first_11 if x.position == "MF" or x.position == "CF")

    def set_first_11(self, first_11):
        self.first_11 = first_11


def set_teams_details():
    for team in Team.instances:
        team.players = get_all_players_list(team)
        team.young_players = [x for x in team.players if x.age < junior_age_until]
        team.team_star = max([x for x in team.players], key=attrgetter('skills'))
        set_young_prospect(team)
        team.average_age = round(sum([x.age for x in team.players])/len(team.players))
        team.average_player_skill = round(sum([x.skills for x in team.players])/len(team.players))
        team.budget = sum([x.value for x in team.players]) + random.randint(5000, 20000)
        if team != manager.me.team: team.first_11 = team.get_first_11()