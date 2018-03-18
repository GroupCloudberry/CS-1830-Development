class PlayerAttributes:
    """
    The PlayerAttributes object is used to store the properties of Player instance.
    Each Player object has its own PlayerAttributes instance, with its own methods to modulate parameters
    of that instance.

    To set a new value for any of the parameters, you can either directly assign the appropriate instance
    variable a new value, or use the set_params(self, name=None, level=None, high_score=None, currency=None, lives=None)
    method, specifying the relevant parameters.

    Note that you should not import this class directly.
    The PlayerAttributes class only should be used for instances where the simplegui import refers to the simplegui
    module. This is because Codeskulptor does not support SQLite3. PlayerSQLite should be used wherever the simplegui
    import refers to the simpleguitk module, in order to support database functionality.

    To make imports easier, use the following snippet:
    if simplegui.__name__ == "simpleguitk":
        from player_sqlite import PlayerSQLite as Player
        from player_attributes_sqlite import PlayerAttributesSQLite as PlayerAttributes
    else:
        from player import Player
        from player_attributes import PlayerAttributes
    """

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

    def set_params(self, name=None, level=None, high_score=None, currency=None, lives=None):
        self.name = name
        self.level = level
        self.high_score = high_score
        self.currency = currency
        self.lives = lives

    """
    @staticmethod  
    def create(name):
        attr = PlayerAttributes()
        attr.set_params(name, PlayerAttributes.DEFAULT_LEVEL, PlayerAttributes.DEFAULT_SCORE,
                        PlayerAttributes.DEFAULT_CURRENCY, PlayerAttributes.DEFAULT_LIVES)
        return attr
    """
