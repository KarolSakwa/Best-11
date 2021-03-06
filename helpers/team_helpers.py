from classes.Constants import *
from operator import attrgetter
import random
from helpers.general_helpers import get_input

def display_player_info(player_list, tabs_num=4, display_position=False, enumerated=False, display_value=True):
    players_info = ""
    for idx, player in enumerate(player_list):
        position = f"Position: {player.position}, " if display_position else ""
        player_idx = str(idx) + ". " if enumerated else ""
        player_value = f", Value: {player.value} " if display_value else ""
        players_info += f"{tabs_num * '    '} {player_idx}{player.name}, {position}Age: {player.age}, Skills: {player.skills}{player_value}\n"
    return players_info

def get_all_players_list(team):
    all_players = []
    for player_list in team.players_by_position.values():
        for player in player_list:
            all_players.append(player)
    return all_players
        
def remove_player_from_team(player, team):
    player.team = None
    team.players.remove(player)
    team.players_by_position[player.position].remove(player)
    if player == team.team_star: team.team_star = max([x for x in team.players], key=attrgetter('skills'))
    if player == team.young_prospect: team.young_prospect = [x for x in team.players if x.age < junior_age_until]

def add_player_to_team(player, team):
    player.team = team
    team.players.append(player)
    team.players_by_position[player.position].append(player)
    if player.skills > team.team_star.skills: team.team_star = player
    if player.age < junior_age_until and player.skills > team.young_prospect.skills: set_young_prospect(team)

def set_young_prospect(team):
    if team.young_players: 
        try:
            team.young_prospect = max([x for x in team.young_players if x != team.team_star], key=attrgetter('skills'))
        except ValueError:  team.young_prospect = min([x for x in team.players], key=attrgetter('age')) # young prospect is the best of all young players and 


def display_team_profile_transfer_mode(team):
    for idx, player in enumerate(team.players):
        print(f"{idx}. {player.name} | {player.position} | Skills: {player.skills}, Age: {player.age}, Value: ${player.value}")

def display_team_profile(team):
    best_scorer = max([x for x in team.players], key=attrgetter('goals'))
    most_matches = max([x for x in team.players], key=attrgetter('matches'))
    print(f"""              ____________________________

                {team.name.upper()}

        Manager: {team.manager}
        Preferred formation: {str(team.manager.preferred_formation) if team.manager.preferred_formation != 0 else "Unknown"}
        Team star: {team.team_star.name} | {team.team_star.position} | Skills: {team.team_star.skills}, Age: {team.team_star.age}
        Young prospect: {team.young_prospect.name} | {team.young_prospect.position} | Skills: {team.young_prospect.skills}, Age: {team.young_prospect.age}
        Average player age: {team.average_age}
        Average player skills: {team.average_player_skill}
        Budget: ${team.budget}
        Statistics:
            Points: {team.points}
            Goals scored: {team.goals_scored} 
            Goals conceded: {team.goals_conceded}
            Best scorer: {best_scorer} ({best_scorer.goals})
            Most matches played: {most_matches} ({most_matches.matches})
        Players: 
            Goalkeepers: 
{display_player_info(team.players_by_position["GK"])}
            Defenders: 
{display_player_info(team.players_by_position["DF"])}
            Midfielders: 
{display_player_info(team.players_by_position["MF"])}
            Forwards: 
{display_player_info(team.players_by_position["CF"])}
            ____________________________
        """)

def select_player(position_name, position_len, manager):
    selected_players = [None for x in range (position_len)]
    all_players = manager.team.players_by_position[position_name].copy()
    if position_name == "DF": position_full_name = "defender"
    elif position_name == "MF": position_full_name = "midfielder"
    else: position_full_name = "forward"
    for player_num in range (position_len):
        selected_players[player_num] = all_players[get_input(f"Select a {position_full_name} ({player_num+1} of {str(position_len)}): \n", display_player_info(all_players, 1, False, True, False))]
        all_players.remove(selected_players[player_num])
    return selected_players

def print_formatted_calendar(calendar, my_team):
    print(menu_separator)
    for idx, fixture in enumerate(calendar):
        print(f"\nFIXTURE {idx+1}:\n")
        for game in fixture:
            team_1 = game.home if game.home != my_team else "*" + game.home.name + "*" # for easier identification of my team
            team_2 = game.away if game.away != my_team else "*" + game.away.name + "*"
            print(f"\t{team_1} vs. {team_2}")

def get_next_game(team):
    my_team_game = None
    for game in team.league.calendar[team.league.current_fixture - 1]:
        if game.home == team or game.away == team: my_team_game = game
    return my_team_game
    

def print_game_squads(team1, team2):
    print(f"{team1.name.upper()}\t\t\t\t{team2.name.upper()}\n")
    for player_num in range(len(team1.first_11)):
        print(f"{team1.first_11[player_num].name} | {team1.first_11[player_num].skills} |\t\t{team2.first_11[player_num].name} | {team2.first_11[player_num].skills} |")
    print("\n")

def get_best_players(position, team):
    available_players = [x for x in team.players_by_position[position]]
    best_players = []
    position_id = 0
    if position == "MF": position_id = 1 
    elif position == "CF": position_id = 2
    for i in range (int(str(team.manager.preferred_formation)[position_id])):
        if available_players:
            best_player = max(available_players, key=attrgetter('skills'))
            best_players.append(best_player)
            available_players.remove(best_player)
    return best_players