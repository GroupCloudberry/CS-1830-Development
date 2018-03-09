from player_attributes import PlayerAttributes
from player_data import PlayerData, PlayerFields


class PlayerAttributesSQLite(PlayerAttributes):
    """
    Please refer to player_attributes.py for a brief documentation of this class.
    """

    def __init__(self):
        super().__init__()
        self.db = PlayerData(PlayerData.DATABASE_NAME)
        self.id = None

    def add_to_db(self):
        self.id = self.db.add_player(self.name, self.level, self.high_score, self.currency, self.lives)
        return self.id

    def sync_to_db(self):
        self.db.update_player(self.id, self.name, self.level, self.high_score, self.currency, self.lives)

    def close(self):
        self.db.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @staticmethod
    def load(key):
        attr = PlayerAttributesSQLite()
        attr.set_params(attr.db.get_field_by_id(key, PlayerFields.NAME),
                        attr.db.get_field_by_id(key, PlayerFields.LEVEL),
                        attr.db.get_field_by_id(key, PlayerFields.HIGH_SCORE),
                        attr.db.get_field_by_id(key, PlayerFields.CURRENCY),
                        attr.db.get_field_by_id(key, PlayerFields.LIVES))
        attr.id = key
        return attr

    @staticmethod
    def create(name):
        attr = PlayerAttributesSQLite()
        attr.set_params(name, PlayerAttributes.DEFAULT_LEVEL, PlayerAttributes.DEFAULT_SCORE,
                        PlayerAttributes.DEFAULT_CURRENCY, PlayerAttributes.DEFAULT_LIVES)
        attr.add_to_db()
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
