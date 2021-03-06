from classes.Constants import *


def get_input(header, to_print):
    while True: 
        print(header)
        print(to_print)
        try: 
            int_input = int(input(""))
            break
        except ValueError: print(wrong_input_error)
    return int_input

def print_list_elements_no_brackets(list, connector):
    return connector.join(list)
