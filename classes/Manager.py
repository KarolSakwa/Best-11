from classes.Team import Team
from classes.League import League
from classes.Constants import *
import random

class Manager:
    instances = []
    def __init__(self, name):
        Manager.instances.append(self)
        # PERSONAL
        self.name = name
        self.first_name = ""
        self.last_name = ""
        self.nationality = ""
        # OTHER
        self.id = 0
        self.team = None
        self.skills = 0
        self.preferred_formation = 0

    def __repr__(self):
        return f'{self.name}'

    def assign_team(self):
        available_teams = [x for x in Team.instances if x.manager == None and self.nationality == x.nationality and self != me]
        if available_teams:
            self.team = available_teams[0]
            available_teams[0].manager = self

def select_my_team():
    print(select_team_text)
    while True: 
        for league in League.instances:
            print("\n" + league.name.upper() + "\n")
            previous_league_index = League.instances.index(league)-1
            start_enumerate_from = League.instances[previous_league_index].teams_num if previous_league_index >= 0 else 0
            for idx, team in enumerate(league.teams):
                print(f"{team.id}. {team}")
        try:
            my_team_id = int(input())
            me.team = Team.instances[my_team_id]
            Team.instances[my_team_id].manager = me
            break
        except ValueError:
            print("\nYou have to choose the number between 0 and " + str(max(x.id for x in Team.instances)) + "! Try again. ")

def create_me():
    my_name = input(my_name_text)
    global me
    me = Manager(my_name)
    me.skills = 50

def generate_managers(num):
    for i in range(num):
        create_manager(Manager)
    for manager in Manager.instances: manager.assign_team()

def create_manager(role):
    manager = Manager("")
    manager.nationality = random.choice(nationalities)
    manager.first_name = random.choice(english_first_names) if manager.nationality == "English" else random.choice(spanish_first_names)
    manager.last_name = random.choice(english_last_names) if manager.nationality == "English" else random.choice(spanish_last_names)
    manager.name = manager.first_name + " " + manager.last_name
    manager.id = len(Manager.instances) - 1
    manager.skills = random.randint(60, 99)
    manager.preferred_formation = random.choice(available_formations)
    return manager