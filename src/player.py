from player_attributes import PlayerAttributes


class Player:

    def __init__(self, attributes: PlayerAttributes=None):
        self.name = None
        self.score = 0
        self.level = PlayerAttributes.DEFAULT_LEVEL
        self.currency = PlayerAttributes.DEFAULT_CURRENCY
        self.lives = PlayerAttributes.DEFAULT_LIVES
        self.db_attributes = attributes

    @staticmethod
    def from_db(key):
        player = Player()
        attributes = PlayerAttributes.load(key)
        player.name = attributes.name
        player.level = attributes.level
        player.currency = attributes.currency
        player.lives = attributes.lives
        player.db_attributes = attributes
        return player

