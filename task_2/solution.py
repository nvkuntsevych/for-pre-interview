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




def add_task(con: sq.Connection, *task_names: tuple[str]):
    print("add_task", task_names)
    flag = check_if_connection(con) and check_if_not_empty(task_names)
    if flag:
        cur = con.cursor()
        for task in task_names:
            print(task)
            #cur.execute()
        print("The tasks have been added")
    




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




def main():
    con = create_connection(db=PATH_TO_DB)

    add_task(con, "task1", "task2")
    
    close_connection(con)


if __name__ == "__main__":
    main()






