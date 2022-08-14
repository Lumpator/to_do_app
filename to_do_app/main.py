from app_operations import app_functions, opening_phrase


def app(user_action):
    app_functions.get(user_action)()


while True:
    action = input(opening_phrase)
    if action.lower() == "e":
        break
    if action in app_functions:
        app(action)
    else:
        print("Invalid option. Please try it again")
