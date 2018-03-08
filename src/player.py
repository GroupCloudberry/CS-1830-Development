from player_attributes import PlayerAttributes


class Player:
    """
    The Player object represents the player sprite and provides a means of manipulating player
    attributes, using an instance of the PlayerAttributes object to store them.

    The fields name, level, high_score, currency, and lives are available as instance variables
    of PlayerAttributes. They can be updated by assigning a new value to them.
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
        # self.attributes.sync_to_db()

    def level_up(self):
        self.attributes.level += 1
        # self.attributes.sync_to_db()

    def high_score(self):
        if self.current_score > self.attributes.high_score:
            self.attributes.high_score = self.current_score
            # self.attributes.sync_to_db()
            return True
        return False

    def spend_money(self, amount):
        self.attributes.currency -= amount
        # self.attributes.sync_to_db()

    def receive_money(self, amount):
        self.attributes.currency += amount
        # self.attributes.sync_to_db()

    def lose_life(self):
        self.attributes.lives -= 1
        # self.attributes.sync_to_db()

    def gain_life(self, lives=1):
        self.attributes.lives += lives
        # self.attributes.sync_to_db()
