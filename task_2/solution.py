import sqlite3 as sq


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
        





def main():
    con = create_connection(db=PATH_TO_DB)

    #add_task(con, "task1", "task2", "task3", "task4", "task5", "task6")
    #remove_task(con, 1, 2)
    #remove_task(con, 8, 3)
    close_connection(con)


if __name__ == "__main__":
    main()






