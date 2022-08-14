from app_operations import app_functions, opening_phrase


class App:
    def __init__(self, user_action):
        self.action = user_action
        app_functions.get(self.action)()


while True:
    action = input(opening_phrase)
    if action.lower() == "e":
        break
    if action in app_functions:
        a = App(action)
    else:
        print("Invalid option. Please try it again")

