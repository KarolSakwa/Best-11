# menu 
title_text = "BEST 11 - GAME MENU"
exit_text = "EXIT"
menu_option_back_text = "BACK"
my_name_text = "Enter the name of the manager: "
too_few_players = "There's too few players in your team to sell someone else!"
too_many_players = "You've got too many players in your team! If you want to buy a player, try to sell someone first."
show_my_team_text = "Show my team"
set_formation_text = "Set formation"
sell_player_text = "Sell player"
buy_player_text = "Buy player"
show_calendar_text = "Show full calendar"
show_current_fixture_text = "Show current fixture"
show_league_table_text = "Show league table"
play_next_game_text = "Play next game"
select_squad_next_game_text = "Select squad for the next game"
show_best_scorers_text = "Show best scorers in the league"
show_last_fixture_stats_text = "Show last fixture statistics"
show_team_profile_text = "Show team profile"
enter_formation_header = "Enter the formation you would like your team to play (e.g. 442 - 4 defenders, 4 midfielders, 2 forwards)"
sell_player_header = "Sell player:\n"
buy_player_header = "Buy player:\n"
best_scorers_header = "\tBest scorers:\n"
last_fixture_stats_header = "\tLast fixture statistics: \n"
table_headers = ["Team", "Games", "Won", "Drawn", "Lost", "Goals scored", "Goals conceded", "Goal difference", "Points"]
menu_separator = "\n_____________________________________________________\n"
wrong_input_error = "You have to enter a correct number! \n"
no_formation_set_error = "You have to choose formation you want to play! \n"
no_squad_set = "You have to select squad for the next game! \n"
too_few_fixtures_error = menu_separator + "You have to play a game before you will be able to check statistics!"
#general
total_players_num = 1000
leagues_num = 2
leagues_names = ["Premier League", "LaLiga"]
select_team_text = "Select your team: "
nationalities = ["English", "Spanish"]
playing_positions_min_max = {"GK": [2, 3], "DF": [5, 8], "MF": [6, 9], "CF": [3, 4]} # contains names, minimum and maximum number of players for position
min_players_num = 18
max_players_num = 30
goalkeepers_percent = 15
defenders_percent = 33
midfielders_percent = 32
forwards_percent = 20
junior_age_until = 23
available_formations = [361, 352, 343, 442, 451, 433, 541, 532, 523]
english_first_names = ["Oliver", "Jack", "Harry", "Alfie", "Charlie", "Thomas", "William", "Joshua", "George", "James", "Daniel", "Jacob", "Samuel", "Ethan", "Joseph", "Mohammed", "Alexander", "Noah", "Oscar", "Lucas", "Dylan", "Benjamin", "Archie", "Max", "Riley", "Lewis", "Muhammad", "Jake", "Jayden", "Ryan", "Logan", "Henry", "Tyler", "Liam", "Finley", "Adam", "Isaac", "Leo", "Luke", "Callum", "Matthew", "Edward", "Harrison", "Freddie", "Connor", "Harvey", "Mason", "Nathan", "Jamie", "Theo", "Zachary", "Michael", "Toby", "Alex", "Aaron", "Harley", "Kai", "Sebastian", "Owen", "Leon", "Charles", "Cameron", "David", "Ollie", "Mohammad", "Aiden", "Finlay", "Louis", "Luca", "Louie", "Reuben", "Ben", "Kyle", "Rhys", "Gabriel", "Kian", "Ashton", "Bailey", "Hayden", "Reece", "Arthur", "Joel", "Bobby", "Jude", "Stanley", "Elliot", "Evan", "Caleb", "Kieran", "Aidan", "Frederick", "Robert", "John", "Sam", "Brandon", "Billy", "Dexter", "Taylor", "Bradley", "Jenson"]
english_last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey", "Rivera", "Cooper", "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long", "Patterson", "Hughes", "Flores", "Washington", "Butler", "Simmons", "Foster", "Gonzales", "Bryant ", "Alexander", "Russell", "Griffin ", "Diaz", "Hayes"]
spanish_first_names = ["Santiago", "Sebastián", "Matías", "Nicolás", "Samuel", "Alejandro", "Mateo", "Diego", "Benjamín", "Daniel", "Joaquín", "Tomás", "Gabriel", "Lucas", "Martín", "Emmanuel", "Alexander", "David", "Emiliano", "Carlos", "Juan José", "Andrés", "Felipe", "Ignacio", "Leonardo", "Adrián", "Francisco", "Rodrigo", "Ángel", "Miguel Ángel", "Fernando", "Santino", "Bautista", "Agustín", "Juan Pablo", "Vicente", "Thiago", "Maximiliano", "Pablo", "Eduardo", "Christopher", "Kevin", "Isaac", "Juan Diego", "Aarón", "Dylan", "Jesús", "Esteban", "Manuel", "Juan Sebastián", "Franco", "Lautaro", "Miguel", "Juan David", "Ricardo", "Bruno", "Luciano", "Juan", "Emilio", "Juan Esteban", "Julián", "Valentino", "Javier", "Joshua", "Rafael", "Jorge", "José", "Luis", "Diego Alejandro", "Gael", "Óscar", "Juan Manuel", "Máximo", "Axel", "Facundo", "Jonathan", "Ian", "Josué", "Camilo", "Sergio", "Jerónimo", "Álex", "Mauricio", "Juan Camilo", "Alonso", "Anthony", "Dante", "Christian", "Simón", "Patricio", "Héctor", "Iván", "Marcos", "Ramiro", "Alberto", "Matthew", "Pedro", "Mario", "Alan", "Arturo"]
spanish_last_names = ["García", "González", "Rodríguez", "Fernández", "López", "Martínez", "Sánchez", "Pérez", "Gómez", "Martin", "Jiménez", "Ruiz", "Hernández", "Diaz", "Moreno", "Muñoz", "Álvarez", "Romero", "Alonso", "Gutiérrez", "Navarro", "Torres", "Domínguez", "Vázquez", "Ramos", "Gil", "Ramírez", "Serrano", "Blanco", "Molina", "Morales", "Suarez", "Ortega", "Delgado", "Castro", "Ortiz", "Rubio", "Marín", "Sanz", "Núñez", "Iglesias", "Medina", "Garrido", "Cortes", "Castillo", "Santos", "Lozano", "Guerrero", "Cano", "Prieto", "Méndez", "Cruz", "Calvo", "Gallego", "Vidal", "León", "Márquez", "Herrera", "Peña", "Flores", "Cabrera", "Campos", "Vega", "Fuentes", "Carrasco", "Diez", "Caballero", "Reyes", "Nieto", "Aguilar", "Pascual", "Santana", "Herrero", "Lorenzo", "Montero", "Hidalgo", "Giménez", "Ibáñez", "Ferrer", "Duran", "Santiago", "Benítez", "Mora", "Vicente", "Vargas", "Arias", "Carmona", "Crespo", "Román", "Pastor", "Soto", "Sáez", "Velasco", "Moya", "Soler", "Parra", "Esteban", "Bravo", "Gallardo", "Rojas"]

teams_names = {
    "Premier League": [
        "Arsenal",
        "Aston Villa",
        "Brighton & Hove Albion",
        "Burnley",
        "Chelsea",
        "Crystal Palace",
        "Everton",
        "Fulham",
        "Leeds United",
        "Leicester City",
        "Liverpool",
        "Manchester City",
        "Manchester United",
        "Newcastle United",
        "Sheffield United",
        "Southampton",
        "Tottenham Hotspur",
        "West Bromwich Albion",
        "West Ham United",
        "Wolverhampton Wanderers"
    ], 
    "LaLiga": [
        "Athletic Bilbao",
        "Atlético Madryt",
        "FC Barcelona",
        "Cádiz CF",
        "Celta Vigo",
        "Deportivo Alavés",
        "SD Eibar",
        "Elche CF",
        "Getafe CF",
        "Granada CF",
        "SD Huesca",
        "Levante UD",
        "CA Osasuna",
        "Real Betis",
        "Real Madryt",
        "Real Sociedad",
        "Real Valladolid",
        "Sevilla FC",
        "Valencia CF",
        "Villarreal CF"
    ]

    }   