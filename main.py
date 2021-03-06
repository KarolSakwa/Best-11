from menu.Menu import Menu
from classes.Constants import *
from events.data_generator import generate_data


def run_game():
  generate_data()
  menu = Menu(title_text)
  menu.show()


if __name__ == '__main__':
  run_game()