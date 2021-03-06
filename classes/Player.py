import random
from classes.Team import Team
from classes.Constants import * 
from classes.League import League

class Player:
    instances = []
    def __init__(self, name):
        Player.instances.append(self)
        # PERSONAL
        self.name = name
        self.first_name = ""
        self.last_name = ""
        self.nationality = ""
        self.age = 0
        # OTHER
        self.id = 0
        self.team = None
        self.position = ""
        self.skills = 0
        self.value = 0
        # STATS
        self.goals = 0
        self.matches = 0
        

    def __repr__(self):
        return f'{self.name}'

def generate_player(num):
    for player in range(num):
        create_player()
    assign_team()

def create_player():
    player = Player("")
    player.nationality = random.choice(nationalities)
    player.first_name = random.choice(english_first_names) if player.nationality == "English" else random.choice(spanish_first_names)
    player.last_name = random.choice(english_last_names) if player.nationality == "English" else random.choice(spanish_last_names)
    player.name = player.first_name + " " + player.last_name
    player.id = len(Player.instances) - 1
    player.skills = random.randint(40, 99)
    player.value = player.skills * (random.randint(1000, 2000))
    positions = ["GK"] * goalkeepers_percent + ["DF"]* defenders_percent + ["MF"] * midfielders_percent + ["CF"] * forwards_percent
    player.position = random.choice(positions)
    player_age_young = random.randint(16,21)
    player_age_prime = random.randint(22,31)
    player_age_old = random.randint(32,39)
    player.age = random.choices(population = [player_age_young, player_age_prime, player_age_old], weights = [0.2, 0.5, 0.3])[0]
    return player

def assign_team():
    players_by_position = []
    for position in playing_positions_min_max.keys():
        players_by_position.append([x for x in Player.instances if x.position == position]) # creates list that contains 4 nested lists, each has all available players for position
    for team in Team.instances:
        for idx, position in enumerate(playing_positions_min_max.keys()):
            try:
                for i in range(random.randint(playing_positions_min_max[position][0], playing_positions_min_max[position][1])):
                    current_player = players_by_position[idx][0]
                    current_player.team = team
                    team.players_by_position[position].append(current_player)
                    if current_player in players_by_position[idx]:
                        players_by_position[idx].remove(current_player)
            except IndexError:
                continue

                