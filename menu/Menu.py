from menu.Menu_Item import Menu_Item
from classes.Constants import *
from menu.menu_functions import *
import classes.Manager as manager
import os

class Menu:
  def __init__(self, title, show_exit=True, children_menu=False):
    self.title = title
    self.item_list = []
    self.show_exit = show_exit
    self.children_menu = children_menu

  def show(self):
    # Create all menu items
    self.create_main_menu_items()

    # Display
    while True:

      print(menu_separator)
      # Title
      print("\n\t\t" + self.title + "\n")

      # Name of manager and his club
      if manager.me != None:
        print(("\t" + manager.me.name + " - manager of " + manager.me.team.name + "\n").upper())

      # Items
      for idx, item in enumerate (self.item_list):
        print(f"{idx}. {item.name}")

      print(menu_separator)
      try:
        menu_choice = int(input("\n"))
        os.system('cls')
        self.item_list[menu_choice].function_name()
      except IndexError: print(menu_separator + "\n" + wrong_input_error)
      except ValueError: print(menu_separator + "\n" + wrong_input_error)


  def create_main_menu_items(self):
    # CREATING MENU ITEMS 
    show_my_team = Menu_Item(show_my_team_text, show_my_team_func)
    set_formation = Menu_Item(set_formation_text, set_formation_func)
    sell_player = Menu_Item(sell_player_text, sell_player_func)
    buy_player = Menu_Item(buy_player_text, buy_player_func)
    show_calendar = Menu_Item(show_calendar_text, show_calendar_func)
    show_current_fixture = Menu_Item(show_current_fixture_text, show_current_fixture_func)
    show_league_table = Menu_Item(show_league_table_text, show_league_table_func)
    select_squad_next_game = Menu_Item(select_squad_next_game_text, select_squad_next_game_func)
    play_next_game = Menu_Item(play_next_game_text, play_next_game_func)
    show_best_scorers = Menu_Item(show_best_scorers_text, show_best_scorers_func)
    show_last_fixture_stats = Menu_Item(show_last_fixture_stats_text, show_last_fixture_stats_func)
    show_team_profile = Menu_Item(show_team_profile_text, show_team_profile_func)

    # PACKING MENU ITEMS INTO MENU LIST
    self.item_list.append(show_my_team)
    self.item_list.append(set_formation)
    self.item_list.append(sell_player)
    self.item_list.append(buy_player)
    self.item_list.append(show_calendar)
    self.item_list.append(show_current_fixture)
    self.item_list.append(show_league_table)
    self.item_list.append(select_squad_next_game)
    self.item_list.append(play_next_game)
    self.item_list.append(show_best_scorers)
    self.item_list.append(show_last_fixture_stats)
    self.item_list.append(show_team_profile)

    # exit option 
    exit_item = Menu_Item(exit_text, exit)
    if self.show_exit: self.item_list.append(exit_item)
