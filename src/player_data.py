import sqlite3
from enum import Enum


class PlayerFields(Enum):
    ID = "id"
    NAME = "name"
    LEVEL = "level"
    HIGH_SCORE = "high_score"
    CURRENCY = "currency"
    LIVES = "lives"


class IdNotFoundError(Exception):
    pass


class PlayerData:

    TABLE = "players"

    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        sql_command = "CREATE TABLE IF NOT EXISTS " + PlayerData.TABLE + " (" \
                      "id integer PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, level INTEGER DEFAULT 1," \
                      "high_score INTEGER DEFAULT 0," \
                      "currency INTEGER DEFAULT 0, lives INTEGER DEFAULT 3)"
        self.connection.execute(sql_command)
        self.connection.commit()

    def close(self):
        self.connection.close()

    def id_exists(self, key):
        sql_command = "SELECT id FROM " + PlayerData.TABLE + " WHERE id = " + key
        cursor = self.connection.cursor()
        cursor.execute(sql_command)
        return cursor.fetchone() is not None

    def add_player(self, name, level, high_score, currency, lives):
        sql_command = "INSERT INTO " + PlayerData.TABLE + "[(name, level, high_score, currency, lives)]" \
                      "VALUES (" + ", ".join(["'{}'".format(name), level, high_score, currency, lives]) + ");"
        cursor = self.connection.cursor()
        cursor.execute(sql_command)
        self.connection.commit()
        return cursor.lastrowid

    def update_player(self, key, name, level, high_score, currency, lives):
        if not self.id_exists(key):
            raise IdNotFoundError
        sql_command = "UPDATE " + self.TABLE + " SET name = " + "'{}'".format(name) + \
                      ", level = " + level + ", high_score = " + high_score + ", currency = " + currency + \
                      ", lives = " + lives + " WHERE id = " + key
        self.connection.execute(sql_command)
        self.connection.commit()

    def retrieve(self, key, fields):
        if not self.id_exists(key):
            raise IdNotFoundError
        sql_command = "SELECT " + fields + " from " + self.TABLE + " WHERE id = " + key
        cursor = self.connection.cursor()
        cursor.execute(sql_command)
        return cursor.fetchone()

    def get_field(self, key, field):
        return self.retrieve(key, field)[0]

    def get_all(self, key):
        return self.retrieve(key, "*")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()