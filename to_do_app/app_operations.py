from db_table_creation import Tasks
from db_utils import cr_session

opening_phrase = "________________________\n1: Show open tasks \n2: Mark task as done\n3: Add new task\n4: Show " \
                 "all tasks(unfinished and done)\nOr press E for exit\n" \
                 "________________________\nPlease choose your action: "


def show_open_tasks():
    print("Your open tasks:")
    s = cr_session()
    tasks = s.query(Tasks).filter(Tasks.done == None).order_by(Tasks.id).all()
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("There are no open tasks.")
        return -1


def mark_task_as_done():
    try:
        if show_open_tasks() == -1:
            return -1
        else:
            task_id = input("Please select, which task you want to mark as done: ")
            s = cr_session()
            task_to_mark = s.query(Tasks).filter(Tasks.id == task_id).first()
            task_to_mark.done = True
            s.commit()
            print(f"Your task with ID {task_to_mark.id} was successfully set as done.")
    except:
        print("Something were wrong")


def add_new_task():
    try:
        new_task = input("Add new task: ")
        s = cr_session()
        s.add(Tasks(tasks=new_task))
        s.commit()
        print(f"Your task was successfully added into database.")
    except:
        print("Something were wrong")


def show_all_tasks():
    print("All your tasks:")
    s = cr_session()
    tasks = s.query(Tasks).order_by(Tasks.done).all()
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("There are no tasks yet.")


app_functions = {"1": show_open_tasks, "2": mark_task_as_done, "3": add_new_task, "4": show_all_tasks}
