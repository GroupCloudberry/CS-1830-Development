from player_data import PlayerData, PlayerFields


class PlayerAttributes:

    DEFAULT_LEVEL = 1
    DEFAULT_SCORE = 0
    DEFAULT_CURRENCY = 0
    DEFAULT_LIVES = 3

    def __init__(self):
        self.name = None
        self.level = None
        self.high_score = None
        self.currency = None
        self.lives = None

        self.db = PlayerData(PlayerData.DATABASE_NAME)
        self.id = None

    def add_to_db(self):
        self.id = self.db.add_player(self.name, self.level, self.high_score, self.currency, self.lives)
        return self.id

    def sync_to_db(self):
        self.db.update_player(self.id, self.name, self.level, self.high_score, self.currency, self.lives)

    def set_params(self, name=None, level=None, high_score=None, currency=None, lives=None):
        self.name = name
        self.level = level
        self.high_score = high_score
        self.currency = currency
        self.lives = lives

    def close(self):
        self.db.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @staticmethod
    def create(name):
        attr = PlayerAttributes()
        attr.set_params(name, PlayerAttributes.DEFAULT_LEVEL, PlayerAttributes.DEFAULT_SCORE,
                        PlayerAttributes.DEFAULT_CURRENCY, PlayerAttributes.DEFAULT_LIVES)
        attr.add_to_db()
        return attr

    @staticmethod
    def load(key):
        attr = PlayerAttributes()
        attr.set_params(attr.db.get_field_by_id(key, PlayerFields.NAME),
                        attr.db.get_field_by_id(key, PlayerFields.LEVEL),
                        attr.db.get_field_by_id(key, PlayerFields.HIGH_SCORE),
                        attr.db.get_field_by_id(key, PlayerFields.CURRENCY),
                        attr.db.get_field_by_id(key, PlayerFields.LIVES))
        attr.id = key
        return attr

    @staticmethod
    def get_ids_with_name(name):
        db = PlayerData(PlayerData.DATABASE_NAME)
        try:
            return db.get_ids_by_name(name)
        finally:
            db.close()

    @staticmethod
    def delete_all_players():
        db = PlayerData(PlayerData.DATABASE_NAME)
        try:
            db.delete_all()
        finally:
            db.close()
