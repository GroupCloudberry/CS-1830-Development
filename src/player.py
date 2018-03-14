try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui

if simplegui.__name__ == "simpleguitk":
    from player_attributes_sqlite import PlayerAttributesSQLite as PlayerAttributes
else:
    from player_attributes import PlayerAttributes


class Player:
    """
    The Player object represents the player sprite and provides a means of manipulating player
    attributes, using an instance of the PlayerAttributes object to store them.

    The fields name, level, high_score, currency, and lives are available as instance variables
    of PlayerAttributes. They can be updated by assigning a new value to them.

    Note that you should not import this class directly.
    The Player class only should be used for instances where the simplegui import refers to the simplegui module.
    This is because Codeskulptor does not support SQLite3. PlayerSQLite should be used wherever the simplegui import
    refers to the simpleguitk module, in order to support database functionality.

    To make imports easier, use the following snippet:
    if simplegui.__name__ == "simpleguitk":
        from player_sqlite import PlayerSQLite as Player
        from player_attributes_sqlite import PlayerAttributesSQLite as PlayerAttributes
    else:
        from player import Player
        from player_attributes import PlayerAttributes
    """

    def __init__(self, attributes: PlayerAttributes):
        """
        To create a new player, create a PlayerAttributes object using
        PlayerAttributes.create(name) and pass it onto this
        constructor as the attributes parameter.
        """
        self.current_score = 0
        self.attributes = attributes

    def rename(self, name):
        self.attributes.name = name

    def level_up(self):
        self.attributes.level += 1

    def high_score(self):
        if self.current_score > self.attributes.high_score:
            self.attributes.high_score = self.current_score
            return True
        return False

    def spend_money(self, amount):
        self.attributes.currency -= amount

    def receive_money(self, amount):
        self.attributes.currency += amount

    def lose_life(self):
        self.attributes.lives -= 1

    def gain_life(self, lives=1):
        self.attributes.lives += lives
