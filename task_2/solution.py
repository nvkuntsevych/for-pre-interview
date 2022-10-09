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


def create_db(con: sq.Connection) -> None:
    print("create_db")
    cur = con.cursor()
    query = ""
    cur.execute(query)


connection = create_connection(db=PATH_TO_DB)
create_db(connection)
close_connection(connection)
