import classes.Manager as manager
from helpers.team_helpers import display_player_info, get_all_players_list, remove_player_from_team, add_player_to_team, display_team_profile, display_team_profile_transfer_mode, print_formatted_calendar, select_player, get_next_game, print_game_squads
from helpers.general_helpers import get_input, print_list_elements_no_brackets
from classes.Constants import * 
from classes.Player import Player
from classes.Match import Match

def show_my_team_func():
    display_team_profile(manager.me.team)

def set_formation_func(separator_on=True):
    if separator_on: print(menu_separator)
    while True:
        print(enter_formation_header)
        try:
            selected_formation = int(input(""))
            if selected_formation not in available_formations: 
                print(wrong_input_error)
                continue
            break
        except ValueError: print(wrong_input_error)
    manager.me.preferred_formation = selected_formation

def sell_player_func():
    if len(manager.me.team.players) > min_players_num:
        print(sell_player_header.upper())
        display_team_profile_transfer_mode(manager.me.team)
        print(f"{len(manager.me.team.players)}. {menu_option_back_text}")
        to_sell = get_input("", "")
        if to_sell == len(manager.me.team.players):
            return
        else:
            sold_player = manager.me.team.players[to_sell]
            remove_player_from_team(sold_player, manager.me.team)
            manager.me.team.budget += sold_player.value
            print(f"{menu_separator}{sold_player.name} has been sold! You've earned ${sold_player.value}.")
    else: print(too_few_players)

def buy_player_func():
    all_players_except_mine = [x for x in Player.instances if x.team != manager.me.team]
    if len(manager.me.team.players) < max_players_num:
        print(buy_player_header.upper())
        for idx, player in enumerate(all_players_except_mine): 
            print(f"{idx}. {player.name} | {player.position} | Skills: {player.skills}, Age: {player.age}, Value: ${player.value}, Team: {player.team}")
        print(f"{len(all_players_except_mine)}. {menu_option_back_text}")
        to_buy = get_input("", "")
        if to_buy == len(all_players_except_mine):
            return
        else:
            bought_player = all_players_except_mine[to_buy]
            add_player_to_team(bought_player, manager.me.team)
            manager.me.team.budget -= bought_player.value
            print(f"{menu_separator}You've bought {bought_player.name}! You've spent ${bought_player.value}.")
    else: print(too_many_players + str(len(manager.me.team.players)))

def show_calendar_func():
    print(menu_separator)
    print_formatted_calendar(manager.me.team.league.calendar, manager.me.team)

def show_current_fixture_func():
    print(menu_separator + "\n")
    for game in manager.me.team.league.calendar[manager.me.team.league.current_fixture - 1]:
        team_1 = game.home if game.home != manager.me.team else "*" + game.home.name + "*" # for easier identification of my team
        team_2 = game.away if game.away != manager.me.team else "*" + game.away.name + "*"
        print(f"\t{team_1} vs. {team_2}")

def show_league_table_func():
    # searching for the longest team name - for formatting purposes
    t_name_maxlen = 0
    for team in manager.me.team.league.teams:
        if len(team.name) > t_name_maxlen:
            t_name_maxlen = len(team.name)
    # empty space before headers
    print(f"\n{(t_name_maxlen - 1) * ' '} ", end="")
    # table headers
    for idx, header in enumerate(table_headers):
        if idx != len(table_headers) - 1:
            print(header + " | ", end="")
        else: print(header + " | ")
    # table body
    for idx, team in enumerate(sorted(manager.me.team.league.teams, key=lambda t: (t.points, (t.goals_scored-t.goals_conceded)), reverse=True)):
        print(f'{idx+1}. {team.name + ((t_name_maxlen-len(team.name)) * " " + (" " if idx < 9 else ""))} | {" " * (len(table_headers[1])-1) + str(team.games_played)} | {" " * (len(table_headers[2])-1) + str(team.wins)} | {" " * (len(table_headers[3])-1) + str(team.draws)} | {" " * (len(table_headers[4])-1) + str(team.losses)} | {" " * (len(table_headers[5])-1) + str(team.goals_scored)} | {" " * (len(table_headers[6])-1) + str(team.goals_conceded)} | {" " * (len(table_headers[7])-1) + str(team.goals_scored-team.goals_conceded)} | {" " * (len(table_headers[8])-1) + str(team.points)} | ')

def select_squad_next_game_func():
    if manager.me.preferred_formation == 0:
        print(no_formation_set_error)
        set_formation_func()
    else: 
        change_formation = input("Do you want to change formation? y/n \n")
        if change_formation.lower() == "y": set_formation_func()
    selected_gk = manager.me.team.players_by_position["GK"][get_input("Select a goalkeeper: \n", display_player_info(manager.me.team.players_by_position["GK"], 1, False, True, False))]
    all_dfs = select_player("DF", int(str(manager.me.preferred_formation)[0]), manager.me)
    all_mfs = select_player("MF", int(str(manager.me.preferred_formation)[1]), manager.me)
    all_cfs = select_player("CF", int(str(manager.me.preferred_formation)[2]), manager.me)
    first_11 = all_dfs + all_mfs + all_cfs
    first_11.insert(0, selected_gk)
    manager.me.team.set_first_11(first_11)
    manager.me.team.first_11_skills = sum(x.skills for x in first_11)
    print(f"Your squad: {selected_gk} - {print_list_elements_no_brackets([x.name for x in all_dfs], ', ')} - {print_list_elements_no_brackets([x.name for x in all_mfs], ', ')} - {print_list_elements_no_brackets([x.name for x in all_cfs], ', ')}")
    print(f"Total squad skills: {manager.me.team.first_11_skills}")

def play_next_game_func():
    my_league = manager.me.team.league
    if manager.me.preferred_formation == 0:
        print(menu_separator)
        print(no_formation_set_error)
        set_formation_func(False)
    if not manager.me.team.first_11:
        print(no_squad_set)
        select_squad_next_game_func()
    if my_league.current_fixture <= len(my_league.calendar):
        print(f"\n {my_league.name.upper()} - FIXTURE {str(my_league.current_fixture).upper()}\n")
        print_game_squads(get_next_game(manager.me.team).home, get_next_game(manager.me.team).away)
        for match in my_league.calendar[my_league.current_fixture - 1]:
            match.play_match()
            if match.home == manager.me.team or match.away == manager.me.team: 
                print(f"{match.home.name.upper()}\t{match.score[0]} : {match.score[1]}\t{match.away.name.upper()} ")
                for scorers_num in range(max(len(match.goal_scorers[0]), len(match.goal_scorers[1]))):
                    try:
                        home_goal_scorer = match.goal_scorers[0][scorers_num].name
                    except IndexError:
                        home_goal_scorer = ""
                    try:
                        away_goal_scorer = match.goal_scorers[1][scorers_num].name
                    except IndexError:
                        away_goal_scorer = ""
                    print(f"{home_goal_scorer} \t\t\t {away_goal_scorer}")
        my_league.current_fixture += 1
    else: print(menu_separator + "Season finished. No more matches to play. ")
    

def show_best_scorers_func():
    print(menu_separator)
    print(best_scorers_header)
    for idx, scorer in enumerate(sorted(manager.me.team.league.goalscorers, key=lambda s: (s.goals), reverse=True)):
        print(f"{idx+1}. {scorer.name} ({scorer.team.name}) - {scorer.goals}")
      
def show_last_fixture_stats_func():
    print(menu_separator)
    print(last_fixture_stats_header)
    if manager.me.team.league.current_fixture < 2: print(too_few_fixtures_error)
    else:
        for match in manager.me.team.league.calendar[manager.me.team.league.current_fixture - 2]:
            print(f"{match.home.name.upper()}\t{match.score[0]} : {match.score[1]}\t{match.away.name.upper()} ")
            for scorers_num in range(max(len(match.goal_scorers[0]), len(match.goal_scorers[1]))):
                try:
                    home_goal_scorer = match.goal_scorers[0][scorers_num].name
                except IndexError:
                    home_goal_scorer = ""
                try:
                    away_goal_scorer = match.goal_scorers[1][scorers_num].name
                except IndexError:
                    away_goal_scorer = ""
                print(f"{home_goal_scorer} \t\t\t {away_goal_scorer}")
            print("\n")

def show_team_profile_func():
    print(menu_separator)
    while True:
        for idx, team in enumerate(manager.me.team.league.teams):
            print(f"{idx}. {team.name}")
        try:
            selected_team_num = int(input(""))
            break
        except ValueError: print(wrong_input_error)
    display_team_profile(manager.me.team.league.teams[selected_team_num])