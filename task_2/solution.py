import sys
import sqlite3 as sq
from datetime import date


PATH_TO_DB = "data.db"


def create_connection(db: str) -> sq.Connection:
    """This function creates connection with db and returns if"""

    con = sq.connect(db)
    return con


def close_connection(con: sq.Connection) -> None:
    """This function closes given connection with db"""
    
    con.commit()
    con.close()


def create_table(con: sq.Connection) -> None:
    """This function creates table into db"""

    flag = check_if_connection(con)
    if flag:
        cur = con.cursor()
        query = """CREATE TABLE IF NOT EXISTS tasks(task_id INTEGER PRIMARY KEY,
                   task_name VARCHAR(50), task_isactive VARCHAR(1), task_closing_date DATE)"""
        cur.execute(query)






def add_task(con: sq.Connection, *task_names: tuple[str]) -> None:
    """This function adds one of several tasks into db"""
    
    flag = check_if_connection(con) and check_if_not_empty(task_names)
    if flag:
        cur = con.cursor()
        for task_name in task_names:
            cur.execute("INSERT INTO tasks (task_name, task_isactive)VALUES (?, 1)", (task_name, ))
        print("The tasks have been added")


def remove_task(con: sq.Connection, *task_ids: tuple[str]) -> None:
    """This function removes one of several tasks from db"""
    
    flag = check_if_connection(con) and check_if_not_empty(task_ids) and check_if_all_tasks_exist(con, task_ids)
    if flag:
        cur = con.cursor()
        for task_id in task_ids:
            cur.execute("DELETE FROM tasks WHERE task_id == ?", (task_id, ))
        print("The tasks with", *task_ids, "ids have been removed")


def mark_task(con: sq.Connection, task_id: str) -> None:
    """This function marks the task with given id as done into db and
       sets current closing date for this task"""
    
    flag = check_if_connection(con) and check_if_task_exist_and_isactive(con, task_id)
    if flag:
        cur = con.cursor()
        query = "UPDATE tasks SET task_isactive = 0, task_closing_date = ? WHERE task_id == ?"
        cur.execute(query, (date.today(), task_id))
        print(f"The tasks with {task_id} id has been marked")


def list_active_task(con: sq.Connection) -> None:
    """This function show the active tasks if they exist"""
        
    flag = check_if_connection(con)
    if flag:
        cur = con.cursor()
        cur.execute("SELECT COUNT(task_name) FROM tasks WHERE task_isactive == 1")
        active_task_numbers = cur.fetchone()[0]
        if active_task_numbers == 0:
            print("There are not active tasks")
        else:
            cur.execute("SELECT task_id, task_name FROM tasks WHERE task_isactive == 1")
            print("Your active tasks:\nid  task")
            for task in cur:
                print(str(task[0]).ljust(3), task[1])


def list_statistic(con: sq.Connection) -> None:
    """This function show the statistic about completed tasks if they exist"""
    
    flag = check_if_connection(con)
    if flag:
        cur = con.cursor()
        cur.execute("SELECT COUNT(task_name) FROM tasks WHERE task_isactive == 0")
        not_active_task_numbers = cur.fetchone()[0]
        if not_active_task_numbers == 0:
            print("There are not completed tasks")
        else:
            cur.execute("SELECT task_closing_date, COUNT(task_name) FROM tasks WHERE task_isactive == 0 GROUP BY task_closing_date")
            for task in cur:
                print(f"{task[0]}: you've completed {task[1]} tasks!")




def check_if_connection(con: sq.Connection) -> bool:
    """This function checks if given argument if Connection object.
       Returns True if it is or returns False and throws Exception otherwise"""

    if type(con) != sq.Connection:
        raise ValueError("The first argument of function must be Connection object")
        return False
    return True


def check_if_not_empty(tpl: tuple[str]) -> bool:
    """This function checks if given tuple is empty.
       Returns False and throws Exception if it is or returns True otherwise"""
    
    if len(tpl) == 0:
        raise ValueError("Command didn't get any arguments")
        return False
    return True


def check_if_all_tasks_exist(con: sq.Connection, task_ids: tuple[str]) -> bool:
    """This function checks if all the tasks with given ids exist.
       Returns True if it is or returns False and throws Exception otherwise"""
        
    cur = con.cursor()
    for task_id in task_ids:
        cur.execute("SELECT COUNT(task_name) FROM tasks WHERE task_id == ?", (task_id, ))
        task_numbers = cur.fetchone()[0]
        if task_numbers == 0:
            raise ValueError("Command got the wrong ids")
            return False
    return True


def check_if_task_exist_and_isactive(con: sq.Connection, task_id: str) -> bool:
    """This function checks if the task with given id exists and it is active.
       Returns True if it is or returns False and throws Exception otherwise"""
        
    cur = con.cursor()
    cur.execute("SELECT COUNT(task_name) FROM tasks WHERE task_id == ? AND task_isactive == 1", (task_id, ))
    task_numbers = cur.fetchone()[0]
    if task_numbers == 0:
        raise ValueError(f"Task with {task_id} doesn't exist or this task is not active")
        return False
    return True





def main() -> None:
    """This function runs the main loop, reads and calls the necessary functions,
       catches the exception and print text of caught exception"""
    
    print("Hello! This is TODO app. Enter 'help' to get information about using this app.")
    while True:
        entered_data = input("Select command: ")
        if entered_data == "":
            continue
        
        command, *args_list = entered_data.split(maxsplit=1)
        if args_list != []:
            args_list = [i.strip() for i in args_list[0].strip(",").split(",")]

        if command == "exit":
            break
        elif command == "help":
            print(help_string)
        elif command in commands_list:
            try:
                con = create_connection(db=PATH_TO_DB)

                create_table(con)
                commands_list[command](con, *args_list)
            except BaseException as exc:
                print(exc, file=sys.stderr)
            finally:
                close_connection(con)
        else:
            print("You entered the wrong command. Try again.")
    print("TODO app has been finished.")
            

commands_list = {"add": add_task, "remove": remove_task, "mark": mark_task, "list": list_active_task, "statistic": list_statistic}

help_string = """
It is a simple TODO app with command line interface.

This app supports the following commands:
help - display this information;
add <your_task> - add new task 'your_task'. You can enter multiple tasks 
    separated by a comma;
remove <task_id> - remove task with id 'task_id'. You can enter multiple
    task ids separated by a comma;
list - display active tasks;
mark <task_id> - mark task with id 'task_id' as done;
statistic - display the number of comleted tasks grouped by date;
exit - exit this app.
"""


if __name__ == "__main__":
    main()






