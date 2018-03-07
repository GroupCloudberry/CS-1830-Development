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

    DATABASE_NAME = "players.db"
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
        sql_command = "SELECT id FROM " + PlayerData.TABLE + " WHERE id = " + str(key)
        cursor = self.connection.cursor()
        cursor.execute(sql_command)
        return cursor.fetchone() is not None

    def add_player(self, name, level, high_score, currency, lives):
        sql_command = "INSERT INTO " + PlayerData.TABLE + " (name, level, high_score, currency, lives)" \
                      " VALUES (" + ", ".join(["'{}'".format(name), str(level), str(high_score),
                                              str(currency), str(lives)]) + ");"
        cursor = self.connection.cursor()
        cursor.execute(sql_command)
        self.connection.commit()
        return cursor.lastrowid

    def update_player(self, key, name, level, high_score, currency, lives):
        if not self.id_exists(key):
            raise IdNotFoundError
        sql_command = "UPDATE " + self.TABLE + " SET name = " + "'{}'".format(name) + \
                      ", level = " + str(level) + ", high_score = " + str(high_score) + \
                      ", currency = " + str(currency) + ", lives = " + str(lives) + " WHERE id = " + str(key)
        print(sql_command)
        self.connection.execute(sql_command)
        self.connection.commit()

    def retrieve_by_id(self, key, fields):
        if not self.id_exists(key):
            raise IdNotFoundError
        sql_command = "SELECT " + fields.value + " from " + self.TABLE + " WHERE id = " + str(key)
        cursor = self.connection.cursor()
        cursor.execute(sql_command)
        return cursor.fetchone()

    def get_field_by_id(self, key, field):
        return self.retrieve_by_id(key, field)[0]

    def get_all_by_id(self, key):
        return self.retrieve_by_id(key, "*")

    def get_ids_by_name(self, name):
        sql_command = "SELECT id FROM " + PlayerData.TABLE + " WHERE name = " + name
        cursor = self.connection.cursor()
        cursor.execute(sql_command)
        return [row[0] for row in list(cursor)]

    def get_all_ids(self):
        sql_command = "SELECT id from " + PlayerData.TABLE
        cursor = self.connection.cursor()
        cursor.execute(sql_command)
        return [row[0] for row in list(cursor)]

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
