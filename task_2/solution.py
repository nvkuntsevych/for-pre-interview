import sqlite3 as sq
from datetime import date


PATH_TO_DB = "data.db"


def create_connection(db: str) -> sq.Connection:
    print("create_connection")
    con = sq.connect(db)
    return con


def close_connection(con: sq.Connection) -> None:
    print("close_connection")
    con.commit()
    con.close()


def create_table(con: sq.Connection) -> None:
    print("create_table")
    cur = con.cursor()
    query = """CREATE TABLE IF NOT EXISTS tasks(task_id INTEGER PRIMARY KEY,
               task_name VARCHAR(50), task_isactive VARCHAR(1), task_closing_date DATE)"""
    cur.execute(query)





def add_task(con: sq.Connection, *task_names: tuple[str]) -> None:
    print("add_task", task_names)
    flag = check_if_connection(con) and check_if_not_empty(task_names)
    if flag:
        cur = con.cursor()
        for task_name in task_names:
            cur.execute("INSERT INTO tasks (task_name, task_isactive)VALUES (?, 1)", (task_name, ))
        print("The tasks have been added")


def remove_task(con: sq.Connection, *task_ids: tuple[str]) -> None:
    print("remove_task", task_ids)
    flag = check_if_connection(con) and check_if_not_empty(task_ids) and check_if_all_tasks_exist(con, task_ids)
    if flag:
        cur = con.cursor()
        for task_id in task_ids:
            cur.execute("DELETE FROM tasks WHERE task_id == ?", (task_id, ))
        print("The tasks with", *task_ids, "ids have been removed")


def mark_task(con: sq.Connection, task_id: str) -> None:
    print("mark_task")
    flag = check_if_connection(con) and check_if_task_exist_and_isactive(con, task_id)
    if flag:
        cur = con.cursor()
        query = "UPDATE tasks SET task_isactive = 0, task_closing_date = ? WHERE task_id == ?"
        cur.execute(query, (date.today(), task_id))
        print(f"The tasks with {task_id} id has been marked")


def list_active_task(con: sq.Connection) -> None:
    print("list_active_task")
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
    print("list_statistic")
    flag = check_if_connection(con)
    if flag:
        cur = con.cursor()
        cur.execute("SELECT COUNT(task_name) FROM tasks WHERE task_isactive == 0")
        not_active_task_numbers = cur.fetchone()[0]
        if not_active_task_numbers == 0:
            print("There are not completed tasks")
        else:
            print("There is some completed tasks")




def check_if_connection(connection: sq.Connection) -> bool:
    print("check_if_connection")
    if type(connection) != sq.Connection:
        raise ValueError("The first value is not a Connection object")
        return False
    return True


def check_if_not_empty(tpl: tuple[str]) -> bool:
    print("check_if_not_empty")
    if len(tpl) == 0:
        raise ValueError("There is no data")
        return False
    return True


def check_if_all_tasks_exist(con: sq.Connection, task_ids: tuple[str]) -> bool:
    print("check_if_all_task_exist")
    cur = con.cursor()
    for task_id in task_ids:
        cur.execute("SELECT COUNT(task_name) FROM tasks WHERE task_id == ?", (task_id, ))
        task_numbers = cur.fetchone()[0]
        if task_numbers == 0:
            raise ValueError("There is some wrong task_ids")
            return False
    return True


def check_if_task_exist_and_isactive(con: sq.Connection, task_id: str) -> bool:
    print("check_if_task_exist_and_isactive", task_id)
    cur = con.cursor()
    cur.execute("SELECT COUNT(task_name) FROM tasks WHERE task_id == ? AND task_isactive == 1", (task_id))
    task_numbers = cur.fetchone()[0]
    if task_numbers == 0:
        raise ValueError(f"Task with {task_id} doesn't exist or this task is not active")
        return False
    return True




def main():
    con = create_connection(db=PATH_TO_DB)

    list_statistic(con)
    
    close_connection(con)


if __name__ == "__main__":
    main()






