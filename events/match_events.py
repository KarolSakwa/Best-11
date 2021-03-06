import random

def get_goals_scored(match):
    home_off_def_strength_proportions = match.home.get_offensive_strength() / match.away.get_defensive_strength()
    away_off_def_strength_proportions = match.away.get_offensive_strength() / match.home.get_defensive_strength()

    def get_goals_num(proportions):
        if proportions < 0.9: return 0
        elif proportions < 1.3: return 1
        elif proportions < 1.6: return 2
        elif proportions < 1.9: return 3
        elif proportions < 2.1: return 4
        else: return 5
    
    home_goals_scored = get_goals_num(home_off_def_strength_proportions)
    away_goals_scored = get_goals_num(away_off_def_strength_proportions)

    goalscorers_home = set_goalscorers(match.home, home_goals_scored)
    goalscorers_away = set_goalscorers(match.away, away_goals_scored)
    
    return [home_goals_scored, away_goals_scored, goalscorers_home, goalscorers_away]

def give_match_stats(match):
    if match.score[0] > match.score[1]: 
        match.winner = match.home
        match.loser = match.away
    elif match.score[0] < match.score[1]: 
        match.winner = match.away
        match.loser = match.home
    if match.winner == None:
        match.home.points += 1
        match.away.points += 1
        match.home.budget += 1000
        match.away.budget += 1000    
        match.home.draws += 1
        match.away.draws += 1
    else:
        match.winner.points += 3
        match.winner.wins += 1
        match.winner.budget += 5000
        match.loser.losses += 1
    match.home.games_played += 1
    match.away.games_played += 1
    match.home.goals_scored += match.score[0]
    match.home.goals_conceded += match.score[1]
    match.away.goals_scored += match.score[1]
    match.away.goals_conceded += match.score[0]
    for player in match.home.first_11: player.matches += 1
    for player in match.away.first_11: player.matches += 1

def set_goalscorers(team, goals_num):
    goalscorers = []
    for i in range(goals_num):
        goalscorer = random.choices(population = [random.choice([x for x in team.first_11 if x.position == "CF"]),   random.choice([x for x in team.first_11 if x.position == "MF"]), random.choice([x for x in team.first_11 if x.position == "DF"]), team.first_11[0] ], weights =   [0.5, 0.36, 0.1299, 0.0001])
        goalscorer[0].goals += 1
        goalscorers.append(goalscorer[0])
        if goalscorer[0] not in team.league.goalscorers: team.league.goalscorers.append(goalscorer[0])
    return goalscorers
        