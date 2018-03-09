from player import Player
from player_attributes_sqlite import PlayerAttributesSQLite


class PlayerSQLite(Player):
    """
    Please refer to player.py for a brief documentation of this class.
    """

    def __init__(self, attributes: PlayerAttributesSQLite):
        super().__init__(attributes)

    def rename(self, name):
        super().rename(name)
        self.attributes.sync_to_db()

    def level_up(self):
        super().level_up()
        self.attributes.sync_to_db()

    def high_score(self):
        if self.current_score > self.attributes.high_score:
            self.attributes.high_score = self.current_score
            self.attributes.sync_to_db()
            return True
        return False

    def spend_money(self, amount):
        super().spend_money(amount)
        self.attributes.sync_to_db()

    def receive_money(self, amount):
        super().receive_money(amount)
        self.attributes.sync_to_db()

    def lose_life(self):
        super().lose_life()
        self.attributes.sync_to_db()

    def gain_life(self, lives=1):
        super().gain_life()
        self.attributes.sync_to_db()
