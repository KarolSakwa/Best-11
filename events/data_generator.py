from classes.Manager import create_me, generate_managers, select_my_team
from classes.League import create_leagues
from classes.Team import Team, set_teams_details
from classes.Constants import *
from classes.Player import generate_player

def generate_data():
    create_me()
    create_leagues()
    select_my_team()
    generate_managers(round(len(Team.instances) + len(Team.instances)/2)) # I need a little bit more managers than teams))
    generate_player(total_players_num)
    set_teams_details()