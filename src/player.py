from player_data import PlayerData, PlayerFields


class Player:

    DEFAULT_LEVEL = 1
    DEFAULT_LIVES = 3
    DATABASE_NAME = "players.db"

    def __init__(self):
        self.name = None
        self.level = None
        self.high_score = None
        self.currency = None
        self.lives = None

        self.db = PlayerData(Player.DATABASE_NAME)
        self.id = None

    def rename(self, name):
        self.name = name
        self.sync_to_db()

    def level_up(self):
        self.level += 1
        self.sync_to_db()

    def spend_money(self, amount):
        self.currency -= amount
        self.sync_to_db()

    def receive_money(self, amount):
        self.currency += amount
        self.sync_to_db()

    def lose_life(self):
        self.lives -= 1
        self.sync_to_db()

    def gain_life(self, lives=1):
        self.lives += lives
        self.sync_to_db()

    def add_to_db(self):
        self.id = self.db.add_player(self.name, self.level, self.high_score, self.currency, self.lives)
        return self.id

    def sync_to_db(self):
        self.db.update_player(self.id, self.name, self.level, self.high_score, self.currency, self.lives)

    def set_params(self, name, level, high_score, currency, lives, key=None):
        self.name = name
        self.level = level
        self.high_score = high_score
        self.currency = currency
        self.lives = lives
        self.id = key

    def close(self):
        self.db.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @staticmethod
    def create(name, high_score, currency):
        player = Player()
        player.set_params(name, Player.DEFAULT_LEVEL, high_score, currency, Player.DEFAULT_LIVES)
        player.add_to_db()
        return player

    @staticmethod
    def load(key):
        player = Player()
        player.set_params(player.db.get_field(key, PlayerFields.NAME), player.db.get_field(key, PlayerFields.LEVEL),
                          player.db.get_field(key, PlayerFields.HIGH_SCORE),
                          player.db.get_field(key, PlayerFields.CURRENCY),
                          player.db.get_field(key, PlayerFields.LIVES), key)
        return player
