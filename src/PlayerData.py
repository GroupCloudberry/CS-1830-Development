import sqlite3


class PlayerData:

    def __init__(self):
        self.connection = sqlite3.connect('playerdata.db')
        sql_command = "CREATE TABLE IF NOT EXISTS players (" \
                      "id integer PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, high_score INTEGER DEFAULT 0," \
                      "currency INTEGER DEFAULT 0, lives INTEGER DEFAULT 3)"
        self.connection.execute(sql_command)
        self.connection.commit()

    def close(self):
        self.connection.close()


