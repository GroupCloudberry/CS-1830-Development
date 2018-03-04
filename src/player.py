from player_attributes import PlayerAttributes


class Player:

    """
    The Player object represents the player sprite and provides a means of manipulating player
    attributes. An instance of the PlayerAttributes object is used to store attributes, which
    can be synchronised with the database using the latter's sync_to_db() method.
    """

    def __init__(self, attributes: PlayerAttributes):
        """
        To create a new player, create a PlayerAttributes object using
        PlayerAttributes.create(name) and pass it onto this
        constructor as the attributes parameter.

        To load an existing player, pass a PlayerAttributes object as the attributes parameter.
        PlayerAttributes.load(key) will return a PlayerAttributes object with attributes loaded
        from the database. If the key is not known, PlayerAttributes.get_ids_with_name(name) can
        return a list of keys/ids matching a given name.
        """
        self.score = 0
        self.attributes = attributes

    def rename(self, name):
        self.attributes.name = name
        self.attributes.sync_to_db()

    def level_up(self):
        self.attributes.level += 1
        self.attributes.sync_to_db()

    def high_score(self):
        if self.score > self.attributes.high_score:
            self.attributes.high_score = self.score
            self.attributes.sync_to_db()
            return True
        return False

    def spend_money(self, amount):
        self.attributes.currency -= amount
        self.attributes.sync_to_db()

    def receive_money(self, amount):
        self.attributes.currency += amount
        self.attributes.sync_to_db()

    def lose_life(self):
        self.attributes.lives -= 1
        self.attributes.sync_to_db()

    def gain_life(self, lives=1):
        self.attributes.lives += lives
        self.attributes.sync_to_db()
