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




def add_task(con: sq.Connection, *tasks_name: tuple[str]):
    pass




def check_if_connection(connection: sq.Connection) -> bool:
    print("check_if_connection")
    if type(connection) != sq.Connection:
        raise ValueError("The first value is not a Connection object")
        return False
    return True


def check_if_not_empty(tpl: tuple[str]) -> bool:
    if len(tpl) == 0:
        raise ValueError("There is no data")
        return False
    return True




def main():
    connection = create_connection(db=PATH_TO_DB)

    result = check_if_not_empty( (1, 2, 3) )
    print(result)
    
    close_connection(connection)


if __name__ == "__main__":
    main()






