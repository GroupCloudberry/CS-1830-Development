from player_data import PlayerData, PlayerFields


class PlayerAttributes:

    DEFAULT_LEVEL = 1
    DEFAULT_CURRENCY = 0
    DEFAULT_LIVES = 3
    DATABASE_NAME = "players.db"

    def __init__(self):
        self.name = None
        self.level = None
        self.high_score = None
        self.currency = None
        self.lives = None

        self.db = PlayerData(PlayerAttributes.DATABASE_NAME)
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

    def set_params(self, name=None, level=None, high_score=None, currency=None, lives=None, key=None):
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
        attr = PlayerAttributes()
        attr.set_params(name, PlayerAttributes.DEFAULT_LEVEL, high_score, currency, PlayerAttributes.DEFAULT_LIVES)
        attr.add_to_db()
        return attr

    @staticmethod
    def load(key):
        attr = PlayerAttributes()
        attr.set_params(attr.db.get_field_by_id(key, PlayerFields.NAME),
                        attr.db.get_field_by_id(key, PlayerFields.LEVEL),
                        attr.db.get_field_by_id(key, PlayerFields.HIGH_SCORE),
                        attr.db.get_field_by_id(key, PlayerFields.CURRENCY),
                        attr.db.get_field_by_id(key, PlayerFields.LIVES), key)
        return attr

    @staticmethod
    def get_ids_with_name(name):
        db = PlayerData(PlayerAttributes.DATABASE_NAME)
        try:
            return db.get_ids_by_name(name)
        finally:
            db.close()

