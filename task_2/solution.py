import sqlite3 as sq


PATH_TO_DB = "data.db"


def create_connection(db: str) -> sq.Connection:
    con = sq.connect(db)
    return con
