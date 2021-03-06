from classes.Constants import *
from classes.Team import Team
from classes.Match import Match

class League:
    instances = []
    def __init__(self, name, teams_num=20):
        League.instances.append(self)
        self.name = name
        self.teams_num = teams_num
        self.teams = []
        self.id = 0
        self.calendar = []
        self.current_fixture = 1
        self.goalscorers = []


    def __repr__(self):
        return f'{self.name}'

    def create_teams(self):
        for team_name in teams_names[self.name]:
          team = Team(team_name)
          self.teams.append(team)
        for idx, team in enumerate(Team.instances): team.id = idx
        for team in self.teams: team.league = self

    def create_calendar(self):
      calendar = []
      if len(self.teams) % 2 == 1: self.teams = self.teams + [None]
      # manipulate map (array of indexes for list) instead of list itself
      # this takes advantage of even/odd indexes to determine home vs. away
      teams_num = len(self.teams)
      all_teams_indexes = list(range(teams_num))
      mid = teams_num // 2
      # creating first round
      for i in range(teams_num-1):
        first_half = all_teams_indexes[:mid]
        second_half = all_teams_indexes[mid:]
        second_half.reverse()
        first_round = []
        for j in range(mid):
          t1 = self.teams[first_half[j]]
          t2 = self.teams[second_half[j]]
          if j == 0 and i % 2 == 1:
            first_round.append(Match(t2, t1, self))
          else:
            first_round.append(Match(t1, t2, self))
        calendar.append(first_round)
          # rotate list by teams_num/2, leaving last element at the end
        all_teams_indexes = all_teams_indexes[mid:-1] + all_teams_indexes[:mid] + all_teams_indexes[-1:]
      #creating second round
      for i in range(teams_num-1):
        first_half = all_teams_indexes[:mid]
        second_half = all_teams_indexes[mid:]
        second_half.reverse()
        second_round = []
        for j in range(mid):
          t1 = self.teams[first_half[j]]
          t2 = self.teams[second_half[j]]
          if j == 0 and i % 2 == 1:
            second_round.append(Match(t1, t2, self))
          else:
            second_round.append(Match(t2, t1, self))
        calendar.append(second_round)
          # rotate list by teams_num/2, leaving last element at the end
        all_teams_indexes = all_teams_indexes[mid:-1] + all_teams_indexes[:mid] + all_teams_indexes[-1:]
      return calendar

def create_leagues():
    premier_league = League(leagues_names[0])
    laliga = League(leagues_names[1])
    premier_league.create_teams()
    premier_league.calendar = premier_league.create_calendar()
    laliga.create_teams()
    laliga.calendar = laliga.create_calendar()
    for idx, league in enumerate(League.instances): 
        league.id = idx # give leagues an id
        for team in league.teams: team.nationality = "English" if league.id == 0 else "Spanish"

