import random
import string

from player_attributes_sqlite import PlayerAttributesSQLite
from player_data import PlayerData


class TestDatabase:

    def __init__(self):
        self.players = []

    @staticmethod
    def populate_table(number_to_add):
        for i in range(number_to_add):
            PlayerAttributesSQLite.create("".join(random.choices(string.ascii_letters + string.digits, k=20)))

    def load_table(self):
        db = PlayerData(PlayerData.DATABASE_NAME)
        for key in db.get_all_ids():
            self.players.append(PlayerAttributesSQLite.load(key))

    def print_table(self):
        for player in self.players:
            print("Player ID {}: name \"{}\", level {}, high score {}, currency {}, and {} lives."
                  .format(player.id, player.name, player.level, player.high_score, player.currency, player.lives))


if __name__ == "__main__":
    test = TestDatabase()
    test.populate_table(3)
    test.load_table()
    test.print_table()